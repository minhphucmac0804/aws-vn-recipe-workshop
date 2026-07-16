---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# AWS Vietnamese Recipe Assistant Workshop

Đây là hướng dẫn cuối cùng cho dự án Vietnamese Recipe Assistant. Phần này đi theo final Lambda RAG backend từ chuẩn bị, triển khai, kiểm thử, observability, evaluation, đến cleanup. Backend này dùng multilingual E5 embeddings trong Lambda container.

## Bạn sẽ xây dựng gì

```text
Local Chainlit UI
  -> Lambda Function URL
  -> Lambda container with multilingual E5 embeddings
  -> E5 qint8 query embedding
  -> Qdrant Cloud
  -> Gemini grounded answer
  -> Chainlit response
```

Observability hỗ trợ:

```text
Lambda -> DynamoDB query logs
Lambda -> CloudWatch structured logs
EventBridge Scheduler -> Lambda health check
CloudWatch metric filter/alarm -> SNS email notification
```

## Luồng workshop

1. [Giới thiệu và kiến trúc](5.1-Workshop-overview/)
2. [Chuẩn bị và kiểm soát chi phí](5.2-Prerequiste/)
3. [Chuẩn bị Qdrant Cloud](5.3-S3-vpc/)
4. [Build, deploy, và kiểm thử Lambda RAG backend](5.4-S3-onprem/)
5. [Evaluation reports](5.5-Policy/)
6. [Cleanup](5.6-Cleanup/)

## Phạm vi chính

Final Lambda RAG backend là luồng chính. Baseline serverless branch, local Qdrant branch, và fallback branch chỉ là bối cảnh lịch sử dự án. Điều này quan trọng vì dự án đi theo tiến trình baseline -> local Qdrant retrieval validation -> hosted Qdrant Cloud -> Lambda container backend.
