---
title : "AI Evaluation Report"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.5.2. </b> "
---

## Purpose

This report summarizes the first lightweight answer-quality evaluation for the final Lambda RAG backend workshop path.

The full path under review is:

```text
Chainlit -> Lambda Function URL -> Lambda RAG backend -> Qdrant Cloud -> Gemini -> response
```

## Evaluation method

The AI evaluation keeps the scoring human-readable.

For each query, the final answer is judged on four criteria:

- `Relevant`
- `Grounded`
- `Useful`
- `Honest`

Then each answer receives a lightweight overall rating such as `Good`, `Partly good`, or `Poor`, plus one short note.

## Reported outcome

The current baseline usually produces relevant and grounded answers for known Vietnamese food queries.

What worked well:

- the full Lambda RAG backend RAG path returned `mode_used=rag` across all 12 evaluation queries
- exact dish prompts and familiar dish-family prompts produced the strongest final answers
- strong examples included `canh chua`, `món thịt kho`, `món cuốn`, `món chay đơn giản`, and `bún`

What was weaker:

- broader lifestyle-style or preference-style prompts were more variable
- weaker examples included `món gà thanh đạm`, `món cá nhẹ bụng`, and some occasion-based prompts
- in those cases the final answer could sound more confident than the retrieved evidence fully justified

## Interpretation

This is a good first workshop result.

The system already demonstrates useful and mostly grounded answer generation, but the answer layer is still noticeably dependent on retrieval quality. When retrieval becomes mixed, answer quality also becomes more variable.

## Relationship to the RAG report

This report judges final answer quality.

The [RAG Evaluation Report](../5.5.1-rag-evaluation-report/) separately judges whether the retrieval layer returned the right context in the first place.
