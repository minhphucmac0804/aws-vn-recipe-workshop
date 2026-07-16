---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# AWS Vietnamese Recipe Assistant
## A Low-cost AWS RAG Workshop for Vietnamese Recipe Search and Grounded Answers

### 1. Executive Summary
This project proposes a practical AWS-based Vietnamese recipe assistant that demonstrates a complete retrieval-augmented generation workflow without requiring a large or expensive cloud stack. The final implementation uses a local Chainlit interface, an AWS Lambda Function URL, a containerized Lambda RAG backend with multilingual E5 embeddings, Qdrant Cloud for vector search, and Gemini for grounded answer generation.

The project is intentionally scoped as a focused workshop deliverable. It presents one end-to-end architecture that is easy to understand, practical to validate with screenshots, logs, and evaluation results, and realistic to complete within the constraints of an internship project. In my AWS account, the checked project cost was `$0`, even when credits were included in the account view.

### 2. Supporting Background Evidence
The final workshop use case is based on a graduation food-recipe project. Because the original project repository is private, the public workshop includes supporting evidence instead of the full private source repository: a [redacted thesis reference](/files/evidence/thesis-reference.pdf), a [private repository screenshot](/images/evidence/graduation-project-repo.png), and a short [Supporting Evidence](../8-SupportingEvidence/) page.

These files are background evidence only. They explain the project domain and learning path, while the workshop implementation remains focused on the final Lambda-based RAG architecture.

### 3. Problem Statement
Vietnamese recipe content is often scattered across notebooks, datasets, ad hoc scripts, and local experiments. A user may want to ask a natural-language question such as `Gợi ý món ăn với thịt gà và rau củ` and receive an answer grounded in recipe data rather than only a generic model response.

The project addresses three practical problems:

- there is no simple reviewer-friendly AWS architecture that demonstrates Vietnamese recipe retrieval end to end
- local-only experiments are useful for learning but harder to present as a clean cloud workshop
- a broader fully AWS-native generative AI architecture can introduce more services, operational overhead, and account requirements than were appropriate for this internship submission

### 4. Proposed Solution
The proposed solution is an AWS workshop centered on the final Lambda RAG backend. In practical terms, the plan was to recreate the core value of the original local project in a cloud-based, reviewer-friendly form rather than reproduce every earlier branch or experiment one-to-one.


```text
Local Chainlit UI -> Lambda Function URL -> Lambda container with multilingual E5 embeddings -> Qdrant Cloud -> Gemini grounded answer -> Chainlit response
```

Supporting observability is kept lightweight and practical:

- Lambda writes query logs to DynamoDB
- Lambda writes structured logs to CloudWatch
- EventBridge Scheduler invokes a health-check path
- CloudWatch metric filter and alarm detect controlled fallback events
- SNS sends reviewer-visible email notification

The final workshop path came from a progression of smaller branches: baseline serverless prototype, local Qdrant retrieval validation, and then the hosted Qdrant Cloud plus Lambda container backend. The local Qdrant branch remains useful context because it explains how retrieval was validated before the cloud backend was complete. The fallback branch remains useful because it shows how the system behaves when hosted retrieval fails. Neither branch replaces the final cloud path.

### 5. Why This Architecture
This architecture was selected because it balances cost, clarity, account constraints, and technical value.

- `AWS Lambda` provides a clear AWS compute layer without keeping a server running.
- `Lambda Function URL` keeps the entry point simple and avoids API Gateway overhead for this workshop.
- `multilingual E5 embeddings` provide a retrieval-focused representation for Vietnamese recipe search.
- `Qdrant Cloud` keeps vector search practical without introducing a heavier AWS-native vector stack.
- `Gemini` provides grounded answer generation from retrieved context.
- `DynamoDB`, `CloudWatch`, `EventBridge Scheduler`, and `SNS` add reviewer-friendly operational evidence.

#### Service Choices and Alternatives

| Workshop decision | Alternative considered | Why this workshop chose the current approach |
| --- | --- | --- |
| `AWS Lambda` for compute | `Amazon EC2` | Lambda matched the workshop workload because the backend only needs to run when a request, health check, or validation call happens. AWS describes Lambda as serverless compute with pay-per-use billing, while EC2 On-Demand instances are billed for provisioned instance capacity by hour or second while they run. For a small internship workshop, Lambda reduced always-on server management and helped keep cost easier to control. |
| `Lambda Function URL` for the HTTPS entry point | `Amazon API Gateway` | Function URL was enough for a reviewer-friendly HTTP endpoint from local Chainlit to Lambda. API Gateway is still a strong future option if the project needs richer routing, authorization, throttling, or a public production API. |
| `Qdrant Cloud` for vector retrieval | `OpenSearch Serverless` | Qdrant had already been validated in the local retrieval branch and then moved to a hosted cloud collection with less setup complexity. OpenSearch Serverless remains a possible future AWS-native vector-search path, but it was not necessary to prove the final RAG workflow. |
| `Gemini` for answer generation | `Amazon Bedrock` | Gemini was available during development and worked with the existing recipe retrieval flow. Bedrock would be a more AWS-native generative AI option, but account activation/access constraints made it less practical for the completed workshop timeline. |
| Local `Chainlit` UI | Cloud-hosted frontend with `CloudFront`, `Cognito`, or similar services | The workshop intentionally focused on the backend RAG path, validation evidence, and observability first. A hosted frontend can be added later after the core Lambda retrieval path is stable. |
| `DynamoDB`, `CloudWatch`, `EventBridge Scheduler`, and `SNS` for observability | Larger logging, analytics, or monitoring stack | These services were enough to show query logs, structured Lambda logs, scheduled health checks, fallback detection, and reviewer-visible email notification without adding unnecessary services. |

The project scale was also shaped by the practical limitation that the AWS account used during development had pending activation limitations. Because of that, the workshop intentionally avoids services that would make the architecture larger or harder to validate under account constraints. This especially affected the ability to use some services that might otherwise have been more directly relevant to a cloud-native generative AI path, such as Amazon Bedrock.

### 6. Objectives
The project objectives are:

- build a working Vietnamese recipe assistant with grounded answers
- present one final workshop path that a reviewer can follow from zero context
- keep the measured AWS account cost at `$0` for the completed project
- provide clear evidence for successful RAG execution and fallback observability
- include cleanup guidance so all resources can be removed after review

### 7. Scope
### In Scope
- local Chainlit user interface
- Lambda Function URL backend entry point
- Lambda container with multilingual E5 query embeddings
- Qdrant Cloud collection for recipe retrieval
- Gemini grounded answer generation
- DynamoDB query logs
- CloudWatch structured logs
- EventBridge Scheduler health check
- CloudWatch alarm and SNS email notification
- small evaluation set with simple retrieval metrics
- local Qdrant and fallback branch notes as project-history context

### Out of Scope
- public production hosting for Chainlit
- CloudFront/static web deployment for the current workshop
- large-scale ingestion pipelines
- ECS/Fargate hosting
- OpenSearch Serverless migration
- advanced automated evaluation as a requirement

### 8. Solution Architecture
The final reviewer-facing architecture is shown below.

![AWS Vietnamese Recipe Assistant Architecture](/images/5-Workshop/aws-workshop-architecture-final.png)

### AWS Services Used
- `AWS Lambda`: main backend compute and orchestration
- `Amazon ECR`: stores the Lambda container image
- `Lambda Function URL`: HTTPS endpoint for the local app
- `Amazon DynamoDB`: query log storage
- `Amazon CloudWatch Logs`: structured application logs
- `Amazon EventBridge Scheduler`: scheduled health-check trigger
- `Amazon CloudWatch Alarm`: alerting on controlled fallback events
- `Amazon SNS`: email notification for alarm evidence

### External Components
- `Chainlit`: local user interface
- `Qdrant Cloud`: vector database
- `Gemini`: answer generation model API

### 9. Technical Implementation Plan
The project implementation is organized around a final workshop path:

1. prepare the Vietnamese recipe dataset and vector collection
2. validate retrieval locally with Qdrant as a development baseline
3. load the recipe collection into Qdrant Cloud
4. build and push the Lambda container image to ECR
5. deploy the Lambda function and configure environment variables
6. expose the Lambda Function URL and connect Chainlit locally
7. validate successful RAG behavior
8. add observability, fallback detection, and evaluation evidence
9. clean up all resources after testing

### 10. Evaluation Plan
Evaluation is intentionally simple and reviewer-friendly.

Smoke tests confirm that the system works end to end:
- Chainlit sends a query successfully
- Lambda returns a response with `mode_used=rag`
- DynamoDB and CloudWatch contain evidence

A small uniform query set is then used for real evaluation:
- Vietnamese recipe recommendation queries
- top-k retrieval review
- simple metrics such as `Precision@3` and `Precision@5`
- short relevance notes per query

RAGAS is optional and not required for the workshop.

### 11. Budget and Cost Control
The measured project cost in my AWS account was `$0`, even when credits were included in the billing view.

Cost stayed at `$0` because the implementation used a small, short-lived workshop setup:
- one Lambda function
- one ECR repository
- one DynamoDB table
- minimal CloudWatch, Scheduler, SNS, and alarm usage
- no NAT Gateway, EC2, RDS, API Gateway, CloudFront, or always-on infrastructure
- cleanup after validation

Qdrant Cloud used a free-tier or equivalent low-cost setup where possible. Future users should still check their own account billing because AWS Free Tier, credits, region, and resource lifetime can differ by account.

### 12. Resource Management
Resource tags are recommended for cleanup and review, even though they are not the main technical topic.

Recommended tags:

| Key | Value |
| --- | --- |
| `Project` | `aws-vn-recipe-workshop` |
| `Purpose` | `fcj-workshop` |
| `Owner` | `<your-name>` |
| `Environment` | `workshop` |

These tags make it easier to find temporary resources before cleanup.

### 13. Constraints and Future Improvement
A future improvement is inspired by [AWS Study Group Lab 117](https://000117.awsstudygroup.com/2-static-s3/2.2-access-data/), `Build a Complete serverless Chat Website`. The relevant idea is a static chat application that uses S3 static hosting and JavaScript access to static data, within a broader serverless architecture using API Gateway, Lambda, DynamoDB, Cognito, and CloudFront.

That path was not implemented in this workshop. CloudFront and the broader public web architecture were left as future work because the current project prioritized the final Lambda RAG backend, the measured `$0` cost result, and the practical limitation of pending AWS account activation status during development. This also means that future extensions such as moving more of the frontend into the cloud, or expanding into API Gateway and Cognito, may be slower or more constrained until account access and available time become less restrictive.

A reasonable scale-up path would keep the current backend logic but move the user-facing layer into a more public cloud architecture, for example with CloudFront, Cognito, and an API layer in front of the assistant workflow. AWS has described Lambda container-image support as being able to handle much larger dependencies while still supporting rapid scale and very high request rates, which means the current backend direction can still remain viable for bursty traffic as the project grows ([AWS authors, 2023](https://arxiv.org/abs/2305.13162)). If usage grows further, asynchronous indexing, evaluation, and maintenance jobs can be separated from the user request path so that the interactive assistant remains smaller and easier to operate.

Longer-term improvements can extend the project in three directions, but they are not required for the current workshop acceptance path:

- `Agent direction`: turn the assistant from a RAG question-answering app into a more agentic cooking helper with tool use, meal-planning steps, pantry constraints, shopping-list generation, or multi-turn planning.
- `Data engineering direction`: make recipe ingestion, cleaning, normalization, validation, and dataset rebuilds more repeatable.
- `Data analytics and data science direction`: build dashboards or analysis around recipe data, query logs, retrieval quality, and evaluation results.

Another future research direction is retrieval-model improvement. The current workshop uses [`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base) as a practical multilingual embedding baseline, but later work could compare or fine-tune embedding models for Vietnamese recipe retrieval. This would connect naturally with the source-retrieval and ranking experience from [CLEF CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/), and could include Vietnamese-oriented models such as [`dangvantuan/vietnamese-embedding`](https://huggingface.co/dangvantuan/vietnamese-embedding) or [`VoVanPhuc/sup-SimCSE-VietNamese-phobert-base`](https://huggingface.co/VoVanPhuc/sup-SimCSE-VietNamese-phobert-base).

The current submission intentionally stays smaller. The goal is to prove one working AWS RAG backend clearly, keep the measured cost at `$0`, and avoid making future DE/DA/agent ideas look like missing requirements.

A demo video can be added later as supporting evidence if it is short, redacted, and focused on the main path. Cleanup screenshots can also be added if they clearly show resources removed, but the cleanup checklist remains the required evidence.

### 14. Risks and Mitigation
- `Cold start and model load latency`: mitigated by using a small, focused workshop workload and validating with simple queries.
- `Vector retrieval failure`: mitigated by controlled fallback testing and CloudWatch/SNS evidence.
- `Secret exposure in screenshots or docs`: mitigated by strict redaction and avoiding committed secrets.
- `Reader confusion from project history`: mitigated by explaining the baseline -> local Qdrant -> hosted Qdrant Cloud progression before the final backend steps.
- `Architecture drift from exploratory branches`: mitigated by centering the final workshop on the Lambda RAG backend while treating local Qdrant and fallback as supporting context.

### 15. Expected Outcomes
The expected outcomes are:

- a clean reviewer-facing AWS workshop repo
- a working Vietnamese recipe assistant using RAG
- visible evidence for successful retrieval, answer grounding, and observability
- a compact architecture that can be explained, validated, and cleaned up easily
