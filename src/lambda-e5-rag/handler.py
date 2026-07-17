from __future__ import annotations

import json
import os
import re
import time
import traceback
import urllib.error
import urllib.request
import uuid
from decimal import Decimal
from typing import Any

import boto3
from fastembed import TextEmbedding
from fastembed.common.model_description import ModelSource, PoolingType


S3_BUCKET = os.environ.get("RECIPE_BUCKET", "")
S3_KEY = os.environ.get("RECIPE_KEY", "data/sample_recipes.json")
LOG_TABLE = os.environ.get("QUERY_LOG_TABLE", "")
TOP_K = int(os.environ.get("TOP_K", "5"))
RETRIEVAL_METHOD = os.environ.get("RETRIEVAL_METHOD", "keyword_s3")

WORKSHOP_QDRANT_URL = os.environ.get("WORKSHOP_QDRANT_URL", "").strip()
WORKSHOP_QDRANT_API_KEY = os.environ.get("WORKSHOP_QDRANT_API_KEY", "").strip()
WORKSHOP_QDRANT_COLLECTION = os.environ.get("WORKSHOP_QDRANT_COLLECTION", "").strip()
WORKSHOP_QDRANT_TOP_K = int(os.environ.get("WORKSHOP_QDRANT_TOP_K", str(TOP_K)))

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite").strip()
GEMINI_TEMPERATURE = float(os.environ.get("GEMINI_TEMPERATURE", "0.2"))
GEMINI_TIMEOUT_SECONDS = int(os.environ.get("GEMINI_TIMEOUT_SECONDS", "20"))

LAMBDA_RAG_ENABLED = os.environ.get("LAMBDA_RAG_ENABLED", "false").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}

WORKSHOP_EMBEDDER_MODEL = os.environ.get("WORKSHOP_EMBEDDER_MODEL", "intfloat/multilingual-e5-base").strip()
WORKSHOP_EMBEDDER_MODEL_HF = os.environ.get("WORKSHOP_EMBEDDER_MODEL_HF", WORKSHOP_EMBEDDER_MODEL).strip()
WORKSHOP_EMBEDDER_MODEL_FILE = os.environ.get("WORKSHOP_EMBEDDER_MODEL_FILE", "model_qint8_avx512_vnni.onnx").strip()
WORKSHOP_EMBEDDER_MODEL_PATH = os.environ.get("WORKSHOP_EMBEDDER_MODEL_PATH", "").strip()
WORKSHOP_EMBEDDER_MODEL_URL = os.environ.get("WORKSHOP_EMBEDDER_MODEL_URL", "").strip() or None
WORKSHOP_EMBEDDER_POOLING = os.environ.get("WORKSHOP_EMBEDDER_POOLING", "MEAN").strip().upper()
WORKSHOP_EMBEDDER_NORMALIZATION = os.environ.get("WORKSHOP_EMBEDDER_NORMALIZATION", "true").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}
WORKSHOP_EMBEDDER_VECTOR_SIZE = int(os.environ.get("WORKSHOP_EMBEDDER_VECTOR_SIZE", "768"))

QDRANT_TIMEOUT_SECONDS = int(os.environ.get("QDRANT_TIMEOUT_SECONDS", "20"))
QDRANT_RETRIEVAL_METHOD = os.environ.get("QDRANT_RETRIEVAL_METHOD", "qdrant_dense").strip()

MODE_LAMBDA_SEARCH = "lambda_search"
MODE_RAG = "rag"

SEARCH_FIELDS = [
    "dish_name",
    "description",
    "ingredients",
    "main_ingredient",
    "culinary_format",
    "dish_tags",
    "text_for_embedding",
]

STOPWORDS = {
    "các",
    "cho",
    "của",
    "món",
    "một",
    "những",
    "tìm",
    "và",
    "với",
}

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
_recipe_cache: list[dict[str, Any]] | None = None
_embedder: TextEmbedding | None = None


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    try:
        payload = parse_payload(event)
        query = (payload.get("query") or "").strip()

        if not query:
            return response(400, {"error": "Missing required field: query"})

        recipes = load_recipes()
        rag_attempted = False
        fallback_reason = ""

        if is_lambda_rag_ready():
            rag_attempted = True
            try:
                rag_payload = try_rag_response(query)
                log_item = write_query_log(
                    query=query,
                    results=rag_payload["results"],
                    mode_used=MODE_RAG,
                    retrieval_method=QDRANT_RETRIEVAL_METHOD,
                    fallback_reason="",
                    answer=rag_payload.get("answer", ""),
                    rag_attempted=True,
                    rag_success=True,
                )
                print(
                    json.dumps(
                        {
                            "event": "query_handled",
                            "query": query,
                            "mode_used": MODE_RAG,
                            "result_count": len(rag_payload["results"]),
                            "retrieval_method": QDRANT_RETRIEVAL_METHOD,
                            "rag_attempted": True,
                            "rag_success": True,
                            "fallback_reason": "",
                            "query_id": log_item.get("query_id") if log_item else None,
                        },
                        ensure_ascii=False,
                    )
                )
                rag_payload["recipe_count"] = len(recipes)
                if log_item:
                    rag_payload["query_id"] = log_item["query_id"]
                return response(200, rag_payload)
            except Exception as exc:
                fallback_reason = f"{type(exc).__name__}: {exc}"
                print(
                    json.dumps(
                        {
                            "event": "rag_branch_failed",
                            "query": query,
                            "rag_attempted": True,
                            "rag_success": False,
                            "fallback_reason": fallback_reason,
                        },
                        ensure_ascii=False,
                    )
                )
                traceback.print_exc()

        results = search_recipes(query, recipes, TOP_K)
        log_item = write_query_log(
            query=query,
            results=results,
            mode_used=MODE_LAMBDA_SEARCH,
            retrieval_method=RETRIEVAL_METHOD,
            fallback_reason=fallback_reason,
            answer="",
            rag_attempted=rag_attempted,
            rag_success=False,
        )
        print(
            json.dumps(
                {
                    "event": "query_handled",
                    "query": query,
                    "mode_used": MODE_LAMBDA_SEARCH,
                    "result_count": len(results),
                    "retrieval_method": RETRIEVAL_METHOD,
                    "rag_attempted": rag_attempted,
                    "rag_success": False,
                    "fallback_reason": fallback_reason,
                    "query_id": log_item.get("query_id") if log_item else None,
                },
                ensure_ascii=False,
            )
        )

        return response(
            200,
            {
                "query": query,
                "mode_used": MODE_LAMBDA_SEARCH,
                "recipe_count": len(recipes),
                "results": results,
                "fallback_reason": fallback_reason or None,
                "query_id": log_item.get("query_id") if log_item else None,
            },
        )
    except Exception as exc:
        print(f"ERROR {type(exc).__name__}: {exc}")
        traceback.print_exc()
        return response(500, {"error": "Internal server error"})


def parse_payload(event: dict[str, Any]) -> dict[str, Any]:
    body = event.get("body")
    if body is None:
        return event
    if event.get("isBase64Encoded"):
        return {}
    if isinstance(body, str) and body:
        return json.loads(body)
    if isinstance(body, dict):
        return body
    return {}


def load_recipes() -> list[dict[str, Any]]:
    global _recipe_cache
    if _recipe_cache is not None:
        return _recipe_cache

    if not S3_BUCKET:
        raise ValueError("RECIPE_BUCKET environment variable is required")

    s3_object = s3_client.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    raw_body = s3_object["Body"].read().decode("utf-8")
    recipes = json.loads(raw_body)
    if not isinstance(recipes, list):
        raise ValueError("Recipe JSON must be a list")

    _recipe_cache = recipes
    return recipes


def search_recipes(query: str, recipes: list[dict[str, Any]], top_k: int) -> list[dict[str, Any]]:
    query_terms = tokenize(query)
    scored = []

    for recipe in recipes:
        haystack = " ".join(str(recipe.get(field, "")) for field in SEARCH_FIELDS).lower()
        score = sum(haystack.count(term) for term in query_terms)
        if score <= 0:
            continue
        scored.append((score, recipe))

    scored.sort(key=lambda item: (-item[0], str(item[1].get("dish_name", ""))))
    return [format_keyword_result(recipe, score) for score, recipe in scored[:top_k]]


def tokenize(text: str) -> list[str]:
    terms = re.findall(r"[\wÀ-ỹ]+", text.lower())
    return [term for term in terms if len(term) > 1 and term not in STOPWORDS]


def format_keyword_result(recipe: dict[str, Any], score: int) -> dict[str, Any]:
    return {
        "food_id": recipe.get("food_id"),
        "dish_name": recipe.get("dish_name"),
        "score": score,
        "description": recipe.get("description", ""),
        "main_ingredient": recipe.get("main_ingredient", ""),
        "culinary_format": recipe.get("culinary_format", ""),
        "dish_tags": recipe.get("dish_tags", ""),
    }


def is_lambda_rag_ready() -> bool:
    return bool(
        LAMBDA_RAG_ENABLED
        and WORKSHOP_QDRANT_URL
        and WORKSHOP_QDRANT_COLLECTION
        and WORKSHOP_QDRANT_API_KEY
        and GEMINI_API_KEY
        and WORKSHOP_EMBEDDER_MODEL_PATH
    )


def try_rag_response(query: str) -> dict[str, Any]:
    query_vector = embed_query_with_e5(query)
    results = query_qdrant(query_vector, WORKSHOP_QDRANT_TOP_K)
    if not results:
        raise ValueError("Qdrant returned no retrieval results.")

    answer = generate_grounded_answer(query, results)
    if not answer.strip():
        raise ValueError("Gemini returned an empty grounded answer.")

    return {
        "query": query,
        "mode_used": MODE_RAG,
        "results": results,
        "answer": answer,
        "show_retrieval_results": False,
    }


def embed_query_with_e5(query: str) -> list[float]:
    embedder = get_e5_embedder()
    vector = next(embedder.embed([f"query: {query}"]))
    return [float(value) for value in vector.tolist()]


def get_e5_embedder() -> TextEmbedding:
    global _embedder
    if _embedder is not None:
        return _embedder

    register_dense_embedding_model()
    kwargs = {}
    if WORKSHOP_EMBEDDER_MODEL_PATH:
        kwargs["specific_model_path"] = WORKSHOP_EMBEDDER_MODEL_PATH
    _embedder = TextEmbedding(model_name=WORKSHOP_EMBEDDER_MODEL, **kwargs)
    return _embedder


def register_dense_embedding_model() -> None:
    supported_models = {model["model"].lower() for model in TextEmbedding.list_supported_models()}
    if WORKSHOP_EMBEDDER_MODEL.lower() in supported_models:
        return

    TextEmbedding.add_custom_model(
        model=WORKSHOP_EMBEDDER_MODEL,
        pooling=resolve_pooling(WORKSHOP_EMBEDDER_POOLING),
        normalization=WORKSHOP_EMBEDDER_NORMALIZATION,
        sources=ModelSource(hf=WORKSHOP_EMBEDDER_MODEL_HF, url=WORKSHOP_EMBEDDER_MODEL_URL),
        dim=WORKSHOP_EMBEDDER_VECTOR_SIZE,
        model_file=WORKSHOP_EMBEDDER_MODEL_FILE,
        description="Custom FastEmbed ONNX dense embedding model for Lambda E5 retrieval.",
    )


def resolve_pooling(value: str) -> PoolingType:
    try:
        return PoolingType[value.upper()]
    except KeyError as exc:
        valid_values = ", ".join(item.name for item in PoolingType)
        raise ValueError(f"WORKSHOP_EMBEDDER_POOLING must be one of: {valid_values}.") from exc


def query_qdrant(query_vector: list[float], limit: int) -> list[dict[str, Any]]:
    payload = {
        "query": query_vector,
        "limit": limit,
        "with_payload": True,
    }
    response = post_json(
        build_qdrant_url(f"/collections/{WORKSHOP_QDRANT_COLLECTION}/points/query"),
        payload,
        {"api-key": WORKSHOP_QDRANT_API_KEY},
        QDRANT_TIMEOUT_SECONDS,
    )
    result = response.get("result")
    points = result.get("points", []) if isinstance(result, dict) else result if isinstance(result, list) else []
    rows = []
    for hit in points:
        payload_data = hit.get("payload") or {}
        rows.append(
            {
                "food_id": payload_data.get("food_id"),
                "dish_name": payload_data.get("dish_name"),
                "description": payload_data.get("description", ""),
                "main_ingredient": payload_data.get("main_ingredient", ""),
                "culinary_format": payload_data.get("culinary_format", ""),
                "dish_tags": payload_data.get("dish_tags", ""),
                "score": float(hit.get("score", 0)),
            }
        )
    return rows


def generate_grounded_answer(query: str, recipes: list[dict[str, Any]]) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": build_grounded_prompt(query, recipes),
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": GEMINI_TEMPERATURE,
        },
    }

    response = post_json(
        build_gemini_url(f"/models/{GEMINI_MODEL}:generateContent"),
        payload,
        {"x-goog-api-key": GEMINI_API_KEY},
        GEMINI_TIMEOUT_SECONDS,
    )

    for candidate in response.get("candidates") or []:
        for part in (candidate.get("content") or {}).get("parts") or []:
            text = str(part.get("text", "")).strip()
            if text:
                return text
    raise ValueError("Gemini generateContent response did not contain answer text.")


def build_grounded_prompt(query: str, recipes: list[dict[str, Any]]) -> str:
    lines = [
        "Ban la tro ly mon an Viet Nam.",
        "Hay tra loi bang tieng Viet.",
        "Chi duoc uu tien su dung cac mon da truy xuat ben duoi.",
        "Neu ngu canh chua du, hay noi ngan gon rang ket qua hien tai chua du de ket luan.",
        "Neu truy van khong lien quan den mon an, nguyen lieu, cach nau, kieu mon, bua an, hoac nhu cau dinh duong, "
        "chi duoc tra loi dung mot cau nay va khong viet them gi: "
        f'Ket qua hien tai chua du de ket luan ve moi lien he giua "{query}" va cac mon an.',
        "",
        f"Truy van nguoi dung: {query}",
        "",
        "Cac mon da truy xuat:",
    ]
    for index, recipe in enumerate(recipes, start=1):
        lines.extend(
            [
                f"{index}. ten_mon={recipe.get('dish_name', 'Khong ro')}",
                f"   food_id={recipe.get('food_id', 'Khong ro')}",
                f"   diem={recipe.get('score', 0):.4f}" if isinstance(recipe.get("score"), (int, float)) else f"   diem={recipe.get('score', 'Khong ro')}",
                f"   nguyen_lieu_chinh={recipe.get('main_ingredient', '')}",
                f"   kieu_mon={recipe.get('culinary_format', '')}",
                f"   ghi_chu={recipe.get('dish_tags', '')}",
                f"   mo_ta={recipe.get('description', '')}",
            ]
        )
    lines.extend(
        [
            "",
            "Yeu cau tra loi:",
            "1. Goi y 1-3 mon phu hop nhat va giai thich ngan gon vi sao.",
            "2. Neu co, neu diem phu hop voi mon thanh dam, mon chay, mon nhieu dam, hoac mon an nhe.",
            "3. Khong duoc che bien them du lieu ngoai cac mon da truy xuat.",
            "4. Khong duoc hien thi danh sach truy xuat, diem truy xuat, hoac metadata tho.",
        ]
    )
    return "\n".join(lines)


def build_qdrant_url(path: str) -> str:
    base = WORKSHOP_QDRANT_URL.rstrip("/")
    return f"{base}{path}" if re.search(r":\d+$", base) else f"{base}:6333{path}"


def build_gemini_url(path: str) -> str:
    return f"https://generativelanguage.googleapis.com/v1beta{path}"


def post_json(url: str, payload: dict[str, Any], headers: dict[str, str], timeout_seconds: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            raw_body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} calling {url}: {exc.read().decode('utf-8', errors='replace')}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error calling {url}: {exc}") from exc
    return json.loads(raw_body)


def write_query_log(
    query: str,
    results: list[dict[str, Any]],
    mode_used: str,
    retrieval_method: str,
    fallback_reason: str,
    answer: str,
    rag_attempted: bool,
    rag_success: bool,
) -> dict[str, Any] | None:
    if not LOG_TABLE:
        print('{"message":"query_log_skipped","reason":"QUERY_LOG_TABLE not configured"}')
        return None
    table = dynamodb.Table(LOG_TABLE)
    item = {
        "query_id": str(uuid.uuid4()),
        "query": query,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "mode_used": mode_used,
        "retrieval_method": retrieval_method,
        "top_recipe_ids": [to_dynamodb_number(result.get("food_id")) for result in results],
        "top_recipe_names": [str(result.get("dish_name", "")) for result in results],
        "scores": [to_dynamodb_number(result.get("score")) for result in results],
        "result_count": len(results),
        "fallback_reason": fallback_reason or "none",
        "rag_attempted": rag_attempted,
        "rag_success": rag_success,
        "answer_preview": answer[:500] if answer else "",
    }
    table.put_item(Item=item)
    print(
        json.dumps(
            {
                "event": "query_log_written",
                "query_id": item["query_id"],
                "mode_used": item["mode_used"],
                "result_count": item["result_count"],
                "retrieval_method": item["retrieval_method"],
                "fallback_reason": item["fallback_reason"],
                "rag_attempted": item["rag_attempted"],
                "rag_success": item["rag_success"],
            },
            ensure_ascii=False,
        )
    )
    return item


def to_dynamodb_number(value: Any) -> Any:
    if isinstance(value, float):
        return Decimal(str(value))
    return value


def response(status_code: int, body: dict[str, Any]) -> dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(body, ensure_ascii=False),
    }
