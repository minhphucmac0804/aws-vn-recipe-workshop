---
title : "Introduction and Architecture"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

## Goal

In this workshop, you deploy and verify a small Vietnamese recipe assistant that uses retrieval augmented generation. The application runs locally in Chainlit, but the main backend runs on AWS Lambda as a containerized RAG backend.

## Architecture

![Final architecture](/aws-vn-recipe-workshop/images/5-Workshop/aws-workshop-architecture-final.png)

Main request path:

```text
User asks a recipe question
  -> Chainlit sends the query to Lambda Function URL
  -> Lambda creates a multilingual E5 query embedding
  -> Lambda searches Qdrant Cloud for top-k recipe context
  -> Lambda asks Gemini to answer using the retrieved context
  -> Chainlit displays the response
```

## Service roles

- `Chainlit`: local user interface for asking recipe questions.
- `Lambda Function URL`: HTTPS endpoint for the local app.
- `AWS Lambda`: containerized backend that runs multilingual E5 retrieval and Gemini answer generation.
- `Amazon ECR`: private container image storage for the Lambda image.
- `Qdrant Cloud`: hosted vector database for recipe embeddings.
- `Gemini`: answer generator that uses retrieved recipe context.
- `DynamoDB`: query log table for reviewer evidence.
- `CloudWatch Logs`: structured runtime logs.
- `EventBridge Scheduler`: scheduled health-check invocations.
- `CloudWatch Metric Filter and Alarm`: detects fallback events.
- `SNS`: sends email notification when the fallback alarm fires.

## What you should understand before continuing

You do not need to be an AWS expert. The important mental model is:

```text
ECR stores the container image.
Lambda runs the image as the final RAG backend.
Function URL lets Chainlit call Lambda.
Qdrant retrieves relevant recipe context.
Gemini writes the final answer.
DynamoDB and CloudWatch prove what happened.
```

## Demo video

<video controls preload="metadata" style="max-width: 100%; border: 1px solid #ddd; border-radius: 4px;">
  <source src="/aws-vn-recipe-workshop/videos/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Demo Video Notes

This short screen recording demonstrates the main working path of the workshop:

1. Architecture overview: local Chainlit UI -> Lambda Function URL -> Lambda container -> Qdrant Cloud -> Gemini.
2. Chainlit success: a Vietnamese recipe question is submitted and answered.
3. Lambda evidence: the backend response uses the RAG path.
4. DynamoDB evidence: the query is recorded in the query log table.

Observability evidence such as CloudWatch logs, Scheduler health check, SNS alarm, and fallback behavior is provided separately in the evidence checklist screenshots.

## Cleanup evidence

Cleanup evidence is provided in [5.6 Cleanup](/5-workshop/5.6-cleanup/). The screenshots show the main workshop resources after deletion or in an empty state, while the cleanup checklist remains the step-by-step artifact for verifying that no resource is left behind.

## What you accomplish in this section

You now know the final architecture and which services are part of the workshop. Continue to preparation before creating cloud resources.
