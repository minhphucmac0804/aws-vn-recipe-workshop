from __future__ import annotations

import os

import chainlit as cl
import requests


LAMBDA_FUNCTION_URL = os.environ.get("LAMBDA_FUNCTION_URL", "")
TIMEOUT_SECONDS = int(os.environ.get("RECIPE_API_TIMEOUT", "20"))


def format_mode_label(mode_used: str) -> str:
    if mode_used == "lambda_search":
        return "Mode used: Lambda search fallback"
    if mode_used == "rag":
        return "Mode used: RAG retrieval"
    return f"Mode used: {mode_used}"


@cl.on_chat_start
async def on_chat_start() -> None:
    await cl.Message(
        content="Nhap mon ban muon tim, vi du: `mon ga thanh dam`."
    ).send()


@cl.on_message
async def on_message(message: cl.Message) -> None:
    if not LAMBDA_FUNCTION_URL:
        await cl.Message(
            content="Missing `LAMBDA_FUNCTION_URL`. Set it to your deployed Lambda Function URL."
        ).send()
        return

    try:
        response = requests.post(
            LAMBDA_FUNCTION_URL,
            json={"query": message.content},
            timeout=TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        payload = response.json()
    except Exception as exc:
        await cl.Message(content=f"Could not call Lambda Function URL: `{exc}`").send()
        return

    results = payload.get("results", [])
    if not results:
        await cl.Message(content="Chua tim thay mon phu hop.").send()
        return

    mode_used = payload.get("mode_used", "lambda_search")
    lines = [
        f"Ket qua cho: **{payload.get('query', message.content)}**",
        format_mode_label(mode_used),
    ]

    answer = payload.get("answer", "").strip()
    if answer:
        lines.append(answer)

    if payload.get("show_retrieval_results", True):
        for index, recipe in enumerate(results, start=1):
            lines.append(
                "\n".join(
                    [
                        f"{index}. **{recipe.get('dish_name', 'Khong ten')}**",
                        f"   - Diem khop: `{recipe.get('score', 0)}`",
                        f"   - Nguyen lieu chinh: {recipe.get('main_ingredient', '')}",
                        f"   - Kieu mon: {recipe.get('culinary_format', '')}",
                        f"   - Ghi chu: {recipe.get('dish_tags', '')}",
                    ]
                )
            )

    await cl.Message(content="\n\n".join(lines)).send()
