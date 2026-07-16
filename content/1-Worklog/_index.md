---
title: "Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

This worklog summarizes my AWS FCJ internship progress from `05/03/2026` to `16/07/2026`. I registered for the program at the beginning of March, but the main worklog starts from the first full working week so the report stays consistent with the weekly format used in the template.

## Background and Learning Path

When I started the internship, my background was stronger in mathematics, statistics, and basic machine learning models than in cloud engineering, software deployment, system design, or production-ready AI systems. I had limited practical experience with AWS services, container deployment, Git/GitHub workflows, API-based application design, and cloud monitoring.

Because of that, much of the internship journey was exploratory. I studied Data Engineering, AWS fundamentals, Retrieval-Augmented Generation (RAG), vector databases, text embeddings, practical Large Language Model (LLM) workflows, and several adjacent AI topics while trying to find a project direction that could become a clear AWS workshop. Some topics were studied because I initially thought they would be useful, but later I learned that they were not directly relevant to the final AWS architecture. Even so, that exploration helped narrow the project into a practical recipe-assistant workshop.

The final direction combined the food-recipe domain from my graduation project with the retrieval and language-model techniques I studied during the internship. Instead of building a large production system, I focused on a small but complete architecture: a local chat interface sends a recipe question to AWS Lambda, Lambda retrieves relevant recipe context from Qdrant Cloud using text embeddings, Gemini generates a grounded answer, and AWS services record logs, health checks, and alerts.

## How Earlier Work Contributed to the Final Workshop

| Learning / Work Area | Contribution to Final Project | Reference / Evidence |
| --- | --- | --- |
| Data Engineering learning | Built cloud-oriented foundations for data pipelines, data quality, storage choices, and AWS-based data workflows. | [DeepLearning.AI Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/data-engineering?utm_medium=sem&utm_source=gg&utm_campaign=b2c_apac_x_multi_ftcof_career-academy_cx_dr_bau_gg_pmax_gc_s2_all_m_hyb_24-08_desktop&campaignid=21573875733&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&creativeid=&assetgroupid=6511386418&targetid=&extensionid=&placement=&gad_source=1&gad_campaignid=21584159401&gclid=Cj0KCQjw39zSBhDhARIsANammDtjU2seBrKpT2enc2Lh624NXanWILTkwLGc2gvZ95AeI_rdLDS5TwYaAoKbEALw_wcB) |
| AWS/FCJ theory and labs | Helped me understand the AWS services used in the final workshop, especially Lambda, ECR, DynamoDB, CloudWatch, EventBridge, SNS, and IAM. | [FCJ theory videos](https://www.youtube.com/watch?v=AQlsd0nWdZk&list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) and [AWS Study Group labs](https://cloudjourney.awsstudygroup.com/) |
| Graduation food-recipe project | Provided the domain, dataset context, and motivation for building a Vietnamese recipe assistant. | [Thesis reference](/aws-vn-recipe-workshop/files/evidence/thesis-reference.pdf), [private repo screenshot](/aws-vn-recipe-workshop/images/evidence/graduation-project-repo.png), and [Supporting Evidence](../8-SupportingEvidence/) |
| Recommender-system exploration | Helped frame the early food recommendation problem, although it was not part of the final AWS architecture. | [A New Dataset and Empirical Evaluation for Vietnamese Food Recommendation System](https://aclanthology.org/2024.paclic-1.4.pdf) and related project discussions |
| Retrieval-Augmented Generation course | Helped me understand how retrieval, context construction, and answer generation fit together in a RAG application. | [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) |
| Claude API / agent course | Broadened my understanding of API-based LLM application design and tool-using assistant workflows. | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) |
| CLEF CheckThat! work | Strengthened my understanding of NLP, scientific source retrieval, embeddings, re-ranking, and evaluation. My team, BoPC, ranked in the top 15 for the related CheckThat! Task 1 work, and the experience exposed me to retrieval and embedding ideas that later informed the recipe-assistant RAG direction. | [CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/) |
| Qdrant and RAG learning | Became directly relevant to the final retrieval architecture and the decision to use vector search for recipe context retrieval. | [Qdrant documentation](https://qdrant.tech/documentation/) and RAG notes |

## Office Visits and Events

This section summarizes documented office visits for studying and AWS/FCJ event participation during the internship. It is included as supporting context for in-person participation and learning activity, while the weekly pages remain focused on technical progress.

| Date | Type | Note |
| --- | --- | --- |
| 05/03/2026 | Office visit for studying | Registered for the internship period and started in-person preparation. |
| 10/03/2026 | Office visit for studying | First documented in-person FCJ working rhythm. |
| 20/03/2026 | Office visit for studying | Reviewed the Vietnamese food recommendation paper and clarified early project framing. |
| 21/03/2026 | AWS/FCJ event | FCJ Community Day: platform engineering, DevOps, cloud architecture, and AI/LLM operations. |
| 25/03/2026 | Office visit for studying | Studied retrieval/ranking concepts and produced a team-facing summary slide. |
| 31/03/2026 | Office visit for studying | Studied AI/CLEF-related concepts and refined the project direction. |
| 15/05/2026 | Office visit for studying | Planned dataset-processing attributes and explored a small-model fine-tuning option. |
| 21/05/2026 | Office visit for studying | Reviewed Gemini-generated recipe attributes and processed additional recipe records. |
| 23/05/2026 | AWS/FCJ event | FCJ Community Day: AI engineering in production, context engineering, security, compliance, and cloud cost control. |
| 06/06/2026 | AWS/FCJ event | Saturday Meet-up: Docker, GraphRAG, operations, troubleshooting, and career development in AI/cloud. |
| 13/07/2026 | Office visit for studying | Final workshop consolidation, architecture drawing, redaction, and reviewer-preparation work. |

## Weekly timeline

- **Week 1 (09/03/2026 - 15/03/2026)**: [Built initial AWS and Data Engineering foundations while starting to explore recommender systems and food recommendation ideas.](1.1-Week1/)
- **Week 2 (16/03/2026 - 22/03/2026)**: [Continued studying recommender systems and attended the FCJ kickoff event, which helped push the project toward a more practical direction.](1.2-Week2/)
- **Week 3 (23/03/2026 - 29/03/2026)**: [Studied RAG, Information Retrieval, ranking concepts, and ML production topics to support the future assistant architecture.](1.3-Week3/)
- **Week 4 (30/03/2026 - 05/04/2026)**: [Continued Generative AI and Data Engineering learning while preparing the graduation project environment and topic adjustment.](1.4-Week4/)
- **Week 5 (06/04/2026 - 12/04/2026)**: [Worked on early graduation project tasks, learned Qdrant, and improved practical development workflow with VS Code and GitHub.](1.5-Week5/)
- **Week 6 (13/04/2026 - 19/04/2026)**: [Balanced CLEF CheckThat! work with Qdrant learning and embedding experiments.](1.6-Week6/)
- **Week 7 (20/04/2026 - 26/04/2026)**: [Completed RAG learning and studied CLEF scientific source-retrieval papers to understand practical retrieval pipelines.](1.7-Week7/)
- **Week 8 (27/04/2026 - 03/05/2026)**: [Moved from CLEF paper reading into fine-tuning multilingual E5 and re-ranker experiments for scientific source retrieval.](1.8-Week8/)
- **Week 9 (04/05/2026 - 10/05/2026)**: [Finished the focused CLEF fine-tuning period, then returned to Data Engineering learning and the food-recipe retrieval-quality issue.](1.9-Week9/)
- **Week 10 (11/05/2026 - 17/05/2026)**: [Investigated low retrieval quality in the food-recipe project and designed a dataset-processing plan using LLMs.](1.10-Week10/)
- **Week 11 (18/05/2026 - 24/05/2026)**: [Processed the recipe dataset with Gemini API and evaluated the resulting dataset quality through EDA.](1.11-Week11/)
- **Week 12 (25/05/2026 - 31/05/2026)**: [Wrote the working note for the CLEF CheckThat! task and consolidated retrieval/NLP lessons.](1.12-Week12/)
- **Week 13 (01/06/2026 - 07/06/2026)**: [Returned to food-recipe data processing by inspecting the Gemini-generated version 1 attributes and planning a version 2 dataset improvement attempt.](1.13-Week13/)
- **Week 14 (08/06/2026 - 14/06/2026)**: [Implemented a Qwen-based version 2 data-processing experiment using Modal GPU resources, then evaluated why the output did not meet the expected quality target.](1.14-Week14/)
- **Week 15 (15/06/2026 - 21/06/2026)**: [Returned focus to FCJ theory learning while also exploring agent and local model topics.](1.15-Week15/)
- **Week 16 (22/06/2026 - 28/06/2026)**: [Balanced FCJ theory, local model exploration, and graduation report writing.](1.16-Week16/)
- **Week 17 (29/06/2026 - 05/07/2026)**: [Started stronger FCJ lab work while continuing the graduation report.](1.17-Week17/)
- **Week 18 (06/07/2026 - 12/07/2026)**: [Resumed FCJ project implementation, recovered AWS access, and narrowed the project from baseline exploration toward the final Lambda-based RAG workshop path.](1.18-Week18/)
- **Week 19 (13/07/2026 - 16/07/2026)**: [Finalized the reviewer-facing workshop repo, evidence package, and final Lambda-based RAG path.](1.19-Week19/)
