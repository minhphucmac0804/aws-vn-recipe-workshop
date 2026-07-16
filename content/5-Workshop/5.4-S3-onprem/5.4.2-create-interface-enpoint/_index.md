---
title : "Create and Configure the Lambda Function"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.4.2. </b> "
---

## Goal

Create a new Lambda function from the ECR image and configure it for the E5 RAG path.

## Step 1 - Create the function

In AWS Console:

1. open `AWS Lambda`
2. choose `Create function`
3. choose `Container image`
4. enter a function name such as:

```text
vnc-rag-query-retriever-e5-image
```

5. select the ECR image you pushed
6. create the function

What you should see:

![Create Lambda function](/images/5-Workshop/workshop-005/02-lambda-rag/14-create-lambda-function.png)
![Image selection](/images/5-Workshop/workshop-005/02-lambda-rag/15-image-selection.png)
![Function creation success](/images/5-Workshop/workshop-005/02-lambda-rag/16-function-creation-success.png)

## Step 2 - Add environment variables

Open:

```text
Lambda -> Configuration -> Environment variables
```

Add values based on the local example file:

```text
project/lambda/lambda_e5_env.example
```

Important variables:

```text
QUERY_LOG_TABLE=RecipeQueryLogs
RECIPE_BUCKET=<recipe-bucket-redacted>
RECIPE_KEY=data/sample_recipes.json
TOP_K=5
WORKSHOP_QDRANT_URL=<qdrant-url-redacted>
WORKSHOP_QDRANT_API_KEY=<qdrant-api-key-redacted>
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud
WORKSHOP_QDRANT_TOP_K=5
GEMINI_API_KEY=<gemini-api-key-redacted>
LAMBDA_RAG_ENABLED=true
QDRANT_RETRIEVAL_METHOD=qdrant_dense
WORKSHOP_EMBEDDER_VECTOR_SIZE=768
```

What you should see:

![Environment variables](/images/5-Workshop/workshop-005/02-lambda-rag/17-add-env-variables.png)

Redaction rule: screenshot values must be redacted before publishing.

## Step 3 - Update general configuration

Open:

```text
Lambda -> Configuration -> General configuration
```

Recommended first-pass settings:

```text
Memory: 2048 MB
Timeout: 60 seconds
Ephemeral storage: 512 MB
```

What you should see:

![Update general config](/images/5-Workshop/workshop-005/02-lambda-rag/18-update-general-config.png)

## Step 4 - Confirm IAM role permissions

Open the function execution role.

The role should allow:

- writing CloudWatch logs
- reading the fallback recipe JSON if S3 fallback is enabled
- writing DynamoDB query log items

What you should see:

![Edit role](/images/5-Workshop/workshop-005/02-lambda-rag/19-edit-role.png)

## Step 5 - Create or verify Function URL

Open:

```text
Lambda -> Configuration -> Function URL
```

Recommended local testing settings:

```text
Auth type: NONE for temporary workshop testing
Allowed origin: http://localhost:8000
Allowed method: POST
Allowed header: content-type
```

What you should see:

![Function URL created](/images/5-Workshop/workshop-005/02-lambda-rag/20-url-created-cors-configured.png)

Do not publish the real Function URL.

## What you accomplished

You created the image-based Lambda RAG backend function, configured runtime settings, added environment variables, and exposed a local-testing Function URL.
