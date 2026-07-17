# Lambda E5 Container Build Guide

This guide builds the container image used by the final Lambda E5 qint8 RAG backend.

## Files In This Folder

```text
handler.py
Dockerfile.e5_qint8
requirements-lambda-e5.txt
lambda_e5_env.example
```

The Lambda receives a recipe query, creates a multilingual E5 qint8 query embedding, retrieves matching recipes from Qdrant Cloud, asks Gemini for a grounded answer, writes optional query logs to DynamoDB, and returns the response through Lambda Function URL.

## Model Files

The qint8 ONNX model file is not committed to this repository because it is large. Before building the Docker image, prepare the multilingual E5 qint8 ONNX file and tokenizer files locally under:

```text
src/models/multilingual-e5-base/onnx/
```

Expected files:

```text
model_qint8_avx512_vnni.onnx
config.json
tokenizer.json
tokenizer_config.json
special_tokens_map.json
sentencepiece.bpe.model
```

The Lambda environment variable should point to the packaged model path:

```text
WORKSHOP_EMBEDDER_MODEL_PATH=/var/task/models/multilingual-e5-base/onnx
```

## Build Locally

Run from the repository root:

```bash
docker build \
  -f src/lambda-e5-rag/Dockerfile.e5_qint8 \
  -t vnc-rag-query-retriever-e5:qint8 .
```

Confirm the image exists:

```bash
docker images | grep vnc-rag-query-retriever-e5
```

## Push To ECR

Use the exact ECR push commands shown in your AWS console. They usually have this shape:

```bash
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.ap-southeast-1.amazonaws.com

docker tag vnc-rag-query-retriever-e5:qint8 <account-id>.dkr.ecr.ap-southeast-1.amazonaws.com/aws-workshop/vnc-rag-query-retriever-e5:qint8

docker push <account-id>.dkr.ecr.ap-southeast-1.amazonaws.com/aws-workshop/vnc-rag-query-retriever-e5:qint8
```

Replace `<account-id>` with your own AWS account ID. Do not commit account-specific values.

## Lambda Configuration

Recommended starting values:

```text
Memory: 2048 MB
Timeout: 60 seconds
Ephemeral storage: 512 MB
```

Set environment variables using `lambda_e5_env.example` as a checklist. Keep real secrets in Lambda environment variables or local `.env` files only.
