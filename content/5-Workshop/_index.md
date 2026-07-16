---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# AWS Vietnamese Recipe Assistant Workshop

This workshop is the final reviewer-facing guide for the Vietnamese Recipe Assistant project. It walks through the final Lambda RAG backend from setup to validation, observability, evaluation, and cleanup. This backend uses multilingual E5 embeddings inside a Lambda container.

## What you will build

```text
Local Chainlit UI
  -> Lambda Function URL
  -> Lambda container with multilingual E5 embeddings
  -> E5 qint8 query embedding
  -> Qdrant Cloud
  -> Gemini grounded answer
  -> Chainlit response
```

Supporting observability:

```text
Lambda -> DynamoDB query logs
Lambda -> CloudWatch structured logs
EventBridge Scheduler -> Lambda health check
CloudWatch metric filter/alarm -> SNS email notification
```

## Workshop path

1. [Introduction and architecture](5.1-Workshop-overview/)
2. [Preparation and cost control](5.2-Prerequiste/)
3. [Prepare Qdrant Cloud](5.3-S3-vpc/)
4. [Build, deploy, and validate the Lambda RAG backend](5.4-S3-onprem/)
5. [Evaluation reports](5.5-Policy/)
6. [Cleanup](5.6-Cleanup/)

## Scope rule

The final Lambda RAG backend is the main workshop. The baseline serverless branch, local Qdrant branch, and fallback branch are included only as project-history context. This matters because the project evolved from baseline -> local Qdrant retrieval validation -> hosted Qdrant Cloud -> Lambda container backend; some screenshots come from that staged progression.

## Completion standard

You are finished when you can show:

- Chainlit returns a grounded answer through Lambda.
- Lambda response or logs show `mode_used=rag`.
- Qdrant Cloud contains the E5 recipe collection.
- DynamoDB stores a query log item.
- CloudWatch stores structured Lambda logs.
- EventBridge Scheduler can invoke the health check.
- CloudWatch alarm and SNS email work for controlled fallback.
- Evaluation reports are visible on the site.
- Cleanup checklist is complete.
