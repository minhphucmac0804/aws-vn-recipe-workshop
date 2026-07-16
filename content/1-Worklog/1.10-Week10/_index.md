---
title: "Week 10"
date: 2024-01-01
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

**Period:** `11/05/2026 - 17/05/2026`

## Focus

Diagnosed low retrieval quality in the food-recipe project and tested whether LLM-based dataset enrichment could improve the retrieval foundation.

## Work Completed

- Investigated why the retrieval component produced low-quality results.
- Identified two main causes: model/retrieval limitations and low-quality Vietnamese recipe data.
- Defined the goal of improving retrieval by processing and enriching the dataset.
- Planned new dataset attributes and extraction logic from existing fields.
- Fine-tuned a small Qwen model for the data-processing task, then determined that the fine-tuning result did not add enough value and decided to use Gemini API instead.

## Daily Progress

| Date | Work completed | Evidence / notes |
| --- | --- | --- |
| 11/05/2026 | Started investigating the low retrieval quality in the food-recipe project. | Checked whether the issue came from the retrieval model, Vietnamese data quality, or both. |
| 13/05/2026 | Finished the main diagnosis and changed the plan from only tuning retrieval to improving the dataset itself. | Defined the goal: generate cleaner and more useful recipe attributes to support retrieval. |
| 14/05/2026 | Designed new dataset attributes and mapped which existing recipe fields could provide the needed information. | This became the first concrete data-processing plan for the recipe dataset. |
| 15/05/2026 | Attended an office visit for studying and added a small Qwen fine-tuning experiment to the dataset-processing plan. | The experiment tested whether a smaller language model could process Vietnamese recipe data without relying fully on an external API. |
| 16/05/2026 | Ran and monitored the Qwen fine-tuning experiment for the data-processing task. | The experiment was useful for learning, but still needed validation against output quality and project usefulness. |
| 17/05/2026 | Completed the fine-tuning experiment and decided not to use it as the main processing path. | The result did not add enough value for the broader task, so the next step moved to Gemini API. |

## Reflection and Lessons Learned

This week was a turning point because I stopped treating retrieval as only a model problem. The diagnosis showed that Vietnamese dataset quality, attribute design, and preprocessing were also central to retrieval quality. The Qwen fine-tuning experiment was useful as a learning exercise, but the decision to switch to Gemini API made the data-processing workflow more practical.
