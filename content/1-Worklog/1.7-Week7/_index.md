---
title: "Week 7"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

**Period:** `20/04/2026 - 26/04/2026`

## Focus

Completed RAG learning and studied CLEF scientific source-retrieval papers to understand practical retrieval pipelines.

## Work Completed

- Completed the [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) course and marked it for later review.
- Read CheckThat! 2025 papers related to the scientific source-retrieval task, using [CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/) as the closest current task reference.
- Pushed project code during a team meeting and clarified follow-up tasks for the graduation project.

## Daily Progress

| Date | Work completed | Evidence / notes |
| --- | --- | --- |
| 20/04/2026 | Studied the [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) course and reviewed CLEF CheckThat! retrieval requirements. | Connected the RAG pattern of query, context retrieval, and grounded answer generation with the CLEF scientific source-retrieval problem. |
| 21/04/2026 | Organized the active task backlog across RAG, Qdrant, CLEF, and the graduation project. | Made the parallel work streams visible so the next technical tasks could be prioritized. |
| 22/04/2026 | Completed the [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) course and started focused reading of CheckThat! 2025 scientific source-retrieval papers. | Main references included [AIRwaves](https://arxiv.org/pdf/2509.19509), [Deep Retrieval](https://ceur-ws.org/Vol-4038/paper_89.pdf), and [Claim2Source](https://ceur-ws.org/Vol-4038/paper_94.pdf). |
| 23/04/2026 | Studied similar-task CheckThat! papers from [CLEF 2025 Working Notes Vol. 4038](https://ceur-ws.org/Vol-4038/). | Focused on retrieval pipelines for linking social-media scientific claims to source papers. |
| 24/04/2026 | Compared sparse retrieval, dense retrieval, hybrid retrieval, and re-ranking ideas from the CLEF papers. | This clarified why retrieval quality depends on both candidate generation and re-ranking. |
| 25/04/2026 | Consolidated notes from the CheckThat! retrieval papers into implementation ideas for the competition task. | Weekend entry is included because it directly supported CLEF task preparation. |
| 26/04/2026 | Reviewed the week’s RAG and CheckThat! retrieval learning and selected next tasks for experiments. | The main outcome was a clearer understanding of retrieval pipelines and evaluation-driven development. |

## Reflection and Lessons Learned

This week made the retrieval direction more concrete. Completing the RAG course gave me a clearer mental model of query, context, and answer generation, while the CheckThat! paper reading showed how scientific source retrieval systems combine BM25, dense embeddings, hard negatives, and re-ranking. The final AWS workshop was not a CLEF system, but this reading strengthened the retrieval and evaluation thinking that later shaped the recipe-assistant RAG path.
