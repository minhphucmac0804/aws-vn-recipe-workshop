---
title : "Build, Deploy, and Validate Lambda RAG backend"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

## Goal

In this section, you build the Lambda container with multilingual E5 embeddings, push it to ECR, create the Lambda function, expose it through a Function URL, validate the RAG path, and add lightweight observability.

## Pages in this section

1. [Build and push the Lambda image](5.4.1-prepare/)
2. [Create and configure the Lambda function](5.4.2-create-interface-enpoint/)
3. [Validate Chainlit, Lambda, DynamoDB, and CloudWatch](5.4.3-test-endpoint/)
4. [Add Scheduler, alarm, and SNS fallback evidence](5.4.4-dns-simulation/)

## Completion target

By the end of this section, you should have evidence for:

- ECR image exists.
- Lambda function is created from the image.
- Function URL is configured.
- Chainlit receives a grounded answer.
- Lambda response uses `mode_used=rag`.
- DynamoDB and CloudWatch show query evidence.
- Scheduler and SNS fallback alarm evidence exist.
