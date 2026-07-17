# AWS Vietnamese Recipe Assistant Workshop

This repository contains the First Cloud Journey workshop materials and source package for an AWS Vietnamese Recipe Assistant. The workshop site is built with Hugo using the FCJ workshop template style. A deployed workshop page exists for review and presentation purposes, while this repository keeps the source code and content needed to understand the implementation.

## Overview

The workshop documents a small Vietnamese recipe assistant built around a Lambda-based retrieval augmented generation path. A local Chainlit UI sends recipe questions to an AWS Lambda Function URL. The Lambda backend runs as a container, creates multilingual E5 query embeddings, retrieves relevant recipe context from Qdrant Cloud, asks Gemini to generate a grounded answer, and returns the response to Chainlit.

The workshop also includes validation and observability evidence using DynamoDB, CloudWatch, EventBridge Scheduler, CloudWatch alarms, and SNS email notification.

## Architecture

Main request path:

```text
Local Chainlit UI
  -> Lambda Function URL
  -> Lambda container with multilingual E5 embeddings
  -> Qdrant Cloud retrieval
  -> Gemini grounded answer
  -> Chainlit response
```

Supporting observability:

```text
Lambda -> DynamoDB query logs
Lambda -> CloudWatch structured logs
EventBridge Scheduler -> Lambda health check
CloudWatch metric filter/alarm -> SNS email notification
```

## Repository Structure

```text
aws-vn-recipe-workshop/
├── README.md                         # Repository overview and source guide
├── config.toml                       # Hugo site configuration
├── content/                          # Workshop pages in English and Vietnamese
│   ├── 1-Worklog/                    # Internship worklog pages
│   ├── 2-Proposal/                   # Project proposal and architecture rationale
│   ├── 3-BlogsPosted/                # AWS blog summaries
│   ├── 4-EventParticipated/          # Event participation summaries
│   ├── 5-Workshop/                   # Main hands-on workshop guide
│   ├── 6-Self-evaluation/            # Self-assessment
│   ├── 7-Feedback/                   # Feedback and reflection
│   └── 8-SupportingEvidence/         # Supporting evidence links and notes
├── src/                              # Minimal source package for the final path
│   ├── chainlit-ui/                  # Local Chainlit UI that calls Lambda Function URL
│   │   ├── chainlit_app.py
│   │   └── README.md
│   ├── lambda-e5-rag/                # Lambda container backend source
│   │   ├── handler.py
│   │   ├── Dockerfile.e5_qint8
│   │   ├── requirements-lambda-e5.txt
│   │   ├── lambda_e5_env.example
│   │   ├── CONTAINER_BUILD.md
│   │   └── README.md
│   └── data/
│       └── sample_recipes.json       # Sample Vietnamese recipe data
├── static/                           # Images, videos, PDFs, CSS, and other static assets
├── layouts/                          # Hugo layout overrides and shortcodes
├── themes/                           # Vendored Hugo Learn theme files
└── .github/workflows/                # GitHub Actions workflow for Hugo build
```

## Source Guide

The `src/` folder contains only the final workshop path. Earlier local RAG, baseline, and experimental branches are intentionally excluded so the public repository stays focused and reproducible.

### Prerequisites

Install or prepare:

```text
Python 3.12+
Docker
AWS CLI
Hugo
Chainlit
requests
```

You also need:

```text
AWS account
Qdrant Cloud account
Gemini API key
```

### Clone And Enter The Repository

```bash
git clone https://github.com/minhphucmac0804/aws-vn-recipe-workshop.git
cd aws-vn-recipe-workshop
```

### Preview The Hugo Workshop Locally

```bash
hugo server
```

Open the local URL printed by Hugo, usually:

```text
http://localhost:1313/
```

### Run The Local Chainlit UI

Install local UI dependencies:

```bash
pip install chainlit requests
```

Set your deployed Lambda Function URL:

```bash
export LAMBDA_FUNCTION_URL="<function-url-redacted>"
export RECIPE_API_TIMEOUT="20"
```

Run Chainlit from the repository root:

```bash
chainlit run src/chainlit-ui/chainlit_app.py
```

### Configure The Lambda Backend

Use the environment template as a checklist:

```text
src/lambda-e5-rag/lambda_e5_env.example
```

Real secrets and account-specific values must be configured locally or in Lambda environment variables. Do not commit:

```text
GEMINI_API_KEY
WORKSHOP_QDRANT_API_KEY
WORKSHOP_QDRANT_URL
Lambda Function URL
AWS account ID
AWS access keys
```

### Prepare E5 qint8 Model Files

The E5 qint8 ONNX model file is not committed because it is large. Before building the Lambda container image, prepare the qint8 model file and tokenizer files locally under:

```text
src/models/multilingual-e5-base/onnx/
```

Expected files include:

```text
model_qint8_avx512_vnni.onnx
config.json
tokenizer.json
tokenizer_config.json
special_tokens_map.json
sentencepiece.bpe.model
```

### Build The Lambda Container

Follow the detailed guide:

```text
src/lambda-e5-rag/CONTAINER_BUILD.md
```

The high-level build command is:

```bash
docker build \
  -f src/lambda-e5-rag/Dockerfile.e5_qint8 \
  -t vnc-rag-query-retriever-e5:qint8 .
```

Then push the image to Amazon ECR using the account-specific commands shown in the AWS console.

## Bilingual Coverage

The workshop content is provided in English and Vietnamese. The main sections include the worklog, proposal, blog/event summaries, workshop guide, self-assessment, feedback, and supporting evidence.

## Purpose

This repository is for educational and internship submission purposes. It documents the final workshop path, project background, implementation evidence, evaluation notes, and cleanup evidence.
