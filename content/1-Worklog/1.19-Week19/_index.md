---
title: "Week 19"
date: 2024-01-01
weight: 19
chapter: false
pre: " <b> 1.19. </b> "
---

**Period:** `13/07/2026 - 16/07/2026`

## Focus

Finalized the reviewer-facing workshop repo, supporting evidence, and final Lambda-based RAG path.

## Work Completed

- Centered the final workshop on the Lambda-based RAG path with E5 query embeddings, Qdrant Cloud retrieval, Gemini answer generation, and AWS observability.
- Added and reviewed screenshots for sensitive information.
- Created the template-based Hugo workshop repo and transformed the technical content into the workshop structure.
- Rewrote the Workshop, Proposal, and Worklog sections for the final project.
- Prepared remaining report sections for final completion.
- Reviewed supporting evidence assets and planned the short demo-video flow for final submission.

## Daily Progress

| Date | Work completed | Evidence / notes |
| --- | --- | --- |
| 13/07/2026 | Attended an office visit for studying, finalized the main RAG architecture, drew/refined the architecture diagram, and reviewed screenshots for redaction. | Final path centered on Chainlit, Lambda Function URL, containerized query embedding, Qdrant Cloud, Gemini, DynamoDB, CloudWatch, EventBridge Scheduler, and SNS. |
| 14/07/2026 | Transformed the Hugo template repo, rewrote the Workshop and Proposal sections, expanded the Worklog, and verified Hugo builds. | This created the reviewer-facing structure for the final submission instead of leaving the project as implementation notes only. |
| 15/07/2026 | Polished worklog references, office/event evidence, final-week reflection, screenshot evidence, and reviewer-facing wording. | Kept the final report aligned with documented evidence, validation steps, cleanup guidance, and Hugo build checks. |
| 16/07/2026 | Reviewed supporting evidence files, clarified the demo-video plan, and updated the worklog end date for final consistency. | Supporting evidence includes the graduation-project repo screenshot and CLEF working note; the demo plan stays screen-recording focused and avoids exposing secrets. |

## Reflection and Lessons Learned

The final architecture became clear as a small RAG application: a local Chainlit UI calls a Lambda Function URL, Lambda creates a query embedding, retrieves relevant recipe context from Qdrant Cloud, and asks Gemini to generate a grounded answer. The supporting AWS services provide query logs, structured logs, scheduled health checks, alarms, and notification evidence. This week turned the implementation into a reviewer-facing workshop structure, with stronger attention to validation, evidence, cost awareness, redaction, demo readiness, and cleanup.

## Overall Internship Summary

| Phase | Period | Key outcome |
| --- | --- | --- |
| Foundation building | Early March - early April | Built background in Data Engineering, AWS fundamentals, recommender systems, RAG, and retrieval concepts. |
| Domain and retrieval exploration | April - May | Worked on the food-recipe graduation project and CLEF CheckThat!, which strengthened the project domain, NLP, retrieval, and embedding background. |
| Dataset processing lessons | May - mid June | Used Gemini and Qwen-based workflows to process recipe data, and learned that source data quality and task design strongly affect retrieval quality. |
| FCJ implementation | Late June - mid July | Returned to FCJ labs, built the project path, and consolidated the final AWS workshop around Lambda, text embeddings, Qdrant Cloud, Gemini, and observability. |
| Workshop finalization | 13/07/2026 - 16/07/2026 | Converted the implementation into a reviewer-facing Hugo workshop with proposal, worklog, validation evidence, supporting artifacts, demo planning, and cleanup guidance. |

## Final Reflection

The internship path was not linear. I started with limited practical experience in AWS, deployment, system design, and production-oriented ML systems, so the first phase required broad learning before the final direction became clear. The graduation project and CLEF work sometimes pulled attention away from FCJ implementation, but they also gave the final workshop its strongest technical foundation: recipe data, retrieval, embeddings, and evaluation.

The main lesson is that an AI project is not only about selecting a model. The final result depended on data quality, retrieval design, deployment constraints, observability, cost control, and clear documentation. By the end, the project became a practical AWS workshop that a reviewer can follow, verify, and clean up safely.
