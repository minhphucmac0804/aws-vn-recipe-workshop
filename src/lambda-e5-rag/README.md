# Lambda E5 RAG Backend

This folder contains the source code for the final workshop backend.

## Request Flow

```text
Lambda Function URL
  -> handler.py
  -> multilingual E5 qint8 query embedding
  -> Qdrant Cloud retrieval
  -> Gemini grounded answer
  -> DynamoDB query log
  -> JSON response
```

The same handler also keeps a keyword/S3 fallback path so the workshop can demonstrate controlled fallback behavior and CloudWatch alarm evidence.

## Files

```text
handler.py                    Lambda handler for the final E5 qint8 RAG path
Dockerfile.e5_qint8           Lambda container image definition
requirements-lambda-e5.txt    Python dependencies installed into the image
lambda_e5_env.example         Redacted environment variable checklist
CONTAINER_BUILD.md            Build, ECR push, and Lambda configuration notes
```

## qint8 Model File

The final workshop path uses this qint8 ONNX model file:

```text
model_qint8_avx512_vnni.onnx
```

The model file is not committed because it is large. Prepare it locally under:

```text
src/models/multilingual-e5-base/onnx/
```

## Required External Services

- Amazon S3 for fallback recipe JSON storage
- Amazon DynamoDB for query log items
- Amazon CloudWatch Logs for structured runtime logs
- Amazon ECR for the Lambda container image
- AWS Lambda Function URL for the HTTPS endpoint
- Qdrant Cloud for vector retrieval
- Gemini API for grounded answer generation

## Secrets

Do not commit real values for:

```text
GEMINI_API_KEY
WORKSHOP_QDRANT_API_KEY
WORKSHOP_QDRANT_URL
Lambda Function URL
AWS account ID
AWS access keys
```

Use `lambda_e5_env.example` only as a redacted checklist.
