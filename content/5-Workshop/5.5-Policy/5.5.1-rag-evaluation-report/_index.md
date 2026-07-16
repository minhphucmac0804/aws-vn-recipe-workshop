---
title : "RAG Evaluation Report"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.5.1. </b> "
---

## Purpose

This report summarizes the first retrieval-focused evaluation for the final Lambda RAG backend workshop path.

The retrieval layer under review is:

```text
E5 query embedding -> Qdrant Cloud retrieval -> top-k recipe results
```

## Evaluation method

This pass uses a lightweight and reviewer-friendly process:

- use a fixed query set
- run retrieval on the same benchmark queries each time
- inspect the top `K=5` results
- mark relevant vs not relevant
- compute `Precision@5`
- record one short note per query

This is intentionally different from final answer evaluation.

## Main metric

```text
Precision@5 = relevant results in top 5 / 5
```

That is enough for a first workshop retrieval report because it is easy to explain and easy to repeat.

## Reported outcome

The current workshop baseline is strong enough to demonstrate a working cloud RAG system with measurable retrieval quality.

What worked well:

- the Lambda RAG backend RAG path stayed healthy across all 12 evaluation queries
- exact dish or familiar dish-family prompts performed best
- strong examples included `canh chua`, `món thịt kho`, `món cuốn`, `món chay đơn giản`, and `bún`

What was weaker:

- broader intent-style prompts were less stable
- weaker examples included `món gà thanh đạm`, `món cá nhẹ bụng`, and some occasion-style requests
- in those cases retrieval sometimes returned mixed candidates rather than a clean top-5 set

## Interpretation

This is a good first workshop baseline.

The retrieval layer is already useful and explainable, but it is more reliable on exact or familiar food queries than on softer preference-style prompts. That gives the reviewer both a success case and an honest limitation.

## Relationship to the AI report

This report judges whether the system retrieved the right context.

The [AI Evaluation Report](../5.5.2-ai-evaluation-report/) separately judges whether Gemini turned that context into a good final answer.
