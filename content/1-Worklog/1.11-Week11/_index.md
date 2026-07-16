---
title: "Week 11"
date: 2024-01-01
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

**Period:** `18/05/2026 - 24/05/2026`

## Focus

Used Gemini API to process the recipe dataset, then inspected whether the generated attributes were reliable enough for retrieval work.

## Work Completed

- Used Gemini API for LLM-assisted data processing after deciding not to rely on the small Qwen fine-tuning result.
- Generated useful new attributes for the recipe dataset.
- Performed EDA on the processed dataset.
- Found that the processed data improved some structure, but the original dataset quality still limited the broader task.

## Daily Progress

| Date | Work completed | Evidence / notes |
| --- | --- | --- |
| 18/05/2026 | Started using Gemini API for recipe dataset processing. | Replaced the fine-tuned small-model approach with a more practical API-based workflow. |
| 19/05/2026 | Generated new recipe attributes from existing fields using LLM-assisted extraction. | Focused on making ingredient, instruction, and recipe-description information more structured. |
| 20/05/2026 | Checked generated outputs for consistency while running the remaining dataset-processing batches. | Looked for whether the new attributes were stable enough to support retrieval experiments. |
| 21/05/2026 | Attended an office visit for studying, reviewed generated attributes, and processed additional recipe records with Gemini. | Some attributes looked useful for later retrieval and analysis, but still needed EDA validation. |
| 22/05/2026 | Practiced using draw.io and drew an AWS-style architecture diagram by following the FCJ architecture drawing guide. | Reference: [FCJ architecture drawing guide](https://www.youtube.com/watch?v=l8isyDe-GwY&list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i&index=2). This later helped me draw my own workshop architecture more clearly. |
| 23/05/2026 | Attended FCJ Community Day. | Event focus: AI engineering in production, context engineering, security, compliance, and cloud cost control. Reference: [Events Participated](../../4-EventParticipated/4.2-Event2/). |

## Reflection and Lessons Learned

This week helped me learn how to use LLM APIs for NLP-style data processing, not only as chat assistants. Gemini-based processing generated some useful attributes, but EDA showed that the source dataset still limited the final quality. The main lesson was that LLM processing can help structure data, but it cannot fully compensate for weak input data.
