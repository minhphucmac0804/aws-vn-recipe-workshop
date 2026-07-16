---
title: "Self-Assessment"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

During this internship, I gradually turned a Vietnamese recipe recommendation idea into a reviewer-facing AWS workshop. By the end of the project, that idea had become a practical cloud-based assistant built around AWS Lambda, vector search, answer generation, and supporting observability services.

## Internship summary

From March 2026 to mid July 2026, my internship work gradually evolved from broad exploration into a focused AWS workshop project. I began with a stronger background in mathematics, statistics, and core machine learning than in cloud engineering, application deployment, or production-oriented AI systems, so the early stage involved significant learning across AWS fundamentals, retrieval-based AI systems, and data workflows. Over time, the project converged on a reviewer-facing Vietnamese Recipe Assistant workshop built around the finalized architecture. That final architecture used a local user interface, an AWS Lambda backend, vector search with Qdrant Cloud, answer generation with Gemini, and supporting observability services on AWS.

## Self-assessment criteria

Use the following table in the template style, but adjust the check marks to match your real self-assessment.

| No. | Criteria | Description | Good | Fair | Average |
| --- | --- | --- | --- | --- | --- |
| 1 | **Professional knowledge & skills** | Understanding AWS, RAG workflow, implementation quality, and practical use of tools | ` ` | ` ` | `✅` |
| 2 | **Ability to learn** | Learning new services, concepts, and implementation patterns during the internship | ` ` | `✅` | ` ` |
| 4 | **Sense of responsibility** | Completing tasks with care and following through on the final workshop output | ` ` | `✅` | ` ` |
| 5 | **Discipline** | Managing time, maintaining work continuity, and staying committed through a long project timeline | ` ` | ` ` | `✅` |
| 6 | **Progressive mindset** | Accepting feedback, correcting direction, and improving the project structure over time | ` ` | `✅` | ` ` |
| 8 | **Problem-solving skills** | Identifying blockers, testing alternatives, and converging on workable solutions | ` ` | `✅` | ` ` |
| 9 | **Professional conduct** | Treating the project seriously and documenting it in a reviewer-friendly way | `✅` | ` ` | ` ` |
| 10 | **Contribution to the final project** | Turning exploratory work into a clean, presentable final workshop | `✅` | ` ` | ` ` |
| 11 | **Overall** | General evaluation of the internship period and final submission quality | ` ` | `✅` | ` ` |

## Main reflection

The internship path was not linear. In the first phase, I was still searching for a project direction clear enough to become an AWS workshop, while also learning Data Engineering, recommender systems, RAG, and retrieval concepts. At the same time, my graduation project and CLEF CheckThat! work consumed a significant share of time, but they also ended up providing the strongest technical foundation for the final workshop: recipe-domain context, retrieval thinking, embeddings, dataset quality awareness, and evaluation habits. The final direction became clear only later, when I returned to FCJ implementation work, connected the AWS services more concretely, and narrowed the final reviewer-facing scope around the E5 Lambda RAG path.

## What I improved most

When I started the internship, my background was stronger in mathematics, statistics, and basic machine learning models than in cloud engineering, software deployment, system design, or production-ready AI systems. I had limited practical experience with AWS services, container deployment, Git/GitHub workflows, API-based application design, and cloud monitoring.

Because of that, much of the internship journey was exploratory. I studied Data Engineering, AWS fundamentals, Retrieval-Augmented Generation (RAG), vector databases, text embeddings, practical Large Language Model (LLM) workflows, and several adjacent AI topics while trying to find a project direction that could become a clear AWS workshop. Some topics were studied because I initially thought they would be useful, but later I learned that they were not directly relevant to the final AWS architecture. Even so, that exploration helped narrow the project into a practical recipe-assistant workshop.

The final direction combined the food-recipe domain from my graduation project with the retrieval and language-model techniques I studied during the internship. Instead of building a large production system, I focused on a small but complete architecture: a local chat interface sends a recipe question to AWS Lambda, Lambda retrieves relevant recipe context from Qdrant Cloud using text embeddings, Gemini generates a grounded answer, and AWS services record logs, health checks, and alerts.

## Needs improvement

- I should become stronger at defining a narrower final project scope earlier, instead of spending too long in broad exploration before converging. This partly reflected my own lack of skill, knowledge, and available time at the start of the internship.
- I should manage time and parallel commitments more tightly when multiple major tracks are running at once, especially when academic and internship work overlap.
- I should evaluate technical choices earlier with small proof-of-concept tests before committing too much time to a direction, especially for data processing, retrieval quality, and model selection.
- I should proactively reach out to mentors or the support team earlier when I have unclear technical or project-direction questions. Doing this sooner could help me unblock problems faster, finish the project earlier, and possibly leave more time to improve the project scale and polish.

## Final note

Overall, I consider this internship a strong period of technical and personal growth. The internship took longer than I originally expected, and the final direction became clear relatively late, but by the end I was able to turn the work into a practical AWS workshop with a clear architecture, working validation path and visible observability. More importantly, I now understand much better how cloud engineering and retrieval systems come together in a real machine learning application.
