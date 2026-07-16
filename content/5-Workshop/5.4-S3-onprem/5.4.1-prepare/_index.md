---
title : "Build and Push the Lambda Image"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.4.1. </b> "
---

## Goal

Build the Lambda container image locally and push it to Amazon ECR.

## Step 1 - Confirm local files

From the implementation repo root, confirm these files exist:

```bash
ls project/lambda/handler.py
ls project/lambda/Dockerfile.e5
ls project/lambda/requirements-lambda-e5.txt
ls project/extensions/rag/models/multilingual-e5-base/onnx/model.onnx
```

What you should see:

- each command prints a file path
- if a file is missing, stop and fix the local implementation before continuing

## Step 2 - Build the image

Run:

```bash
docker build -f project/lambda/Dockerfile.e5 -t vnc-rag-query-retriever-e5:qint8 .
```

What success means:

```text
Docker created a local image containing the Lambda handler, dependencies, and E5 model files.
```

If `docker` is not found, fix Docker Desktop WSL integration before debugging the Dockerfile.

## Step 3 - Create or open the ECR repository

In AWS Console:

1. open `Amazon ECR`
2. open `Repositories`
3. create or select a private repository such as:

```text
aws-workshop/vnc-rag-query-retriever-e5
```

The original first ECR repository screenshot was removed during redaction, so this guide starts from the safe post-creation evidence.

What you should see:

![ECR repository tags](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/02-add-repo-tags.png)

## Step 4 - Use View push commands

In the ECR repository page:

1. choose `View push commands`
2. copy the commands shown by AWS
3. run them locally after replacing only local image names if needed

Why this is safer:

```text
The console provides the exact account-specific repository URI.
Typing the URI manually is more error-prone.
```

Redaction rule: never publish the real account ID or repository URI.

Evidence:

![View push commands](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/11-view-push-commands.png)
![View push commands continued](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/12-view-push-commands.png)

## Step 5 - Confirm active image

After pushing, confirm the image exists in ECR.

What you should see:

![Active image](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/13-active-image.png)

## What you accomplished

You built a local Lambda RAG backend image and uploaded it to ECR so Lambda can create a function from it.
