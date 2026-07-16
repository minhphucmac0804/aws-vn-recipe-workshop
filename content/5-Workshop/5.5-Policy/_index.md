---
title : "Evaluation Reports"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

## Goal

This section separates operational smoke tests from evaluation.

Smoke tests answer:

```text
Does the system run end to end?
```

Evaluation answers:

```text
How good are retrieval and final answer quality?
```

## Posted reports

Read these pages after validating the live path:

1. [RAG Evaluation Report](5.5.1-rag-evaluation-report/)
2. [AI Evaluation Report](5.5.2-ai-evaluation-report/)
3. [Evaluation Query Set](5.5.3-evaluation-query-set/)

## Beginner scoring rule

For retrieval, use:

```text
Precision@5 = relevant results in top 5 / 5
```

For answer quality, use simple human ratings:

```text
Good
Partly good
Poor
```

with short notes for relevance, groundedness, usefulness, and honesty.

## RAGAS note

RAGAS is optional. It is not required for the workshop acceptance path.
