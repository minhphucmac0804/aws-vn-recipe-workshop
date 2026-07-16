---
title : "Preparation and Cost Control"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

## Region

Use this AWS region throughout the workshop:

```text
ap-southeast-1
```

Keeping one region avoids confusion when you look for Lambda logs, ECR images, DynamoDB tables, Scheduler, alarms, and SNS topics.

## Required accounts

Prepare these before you start:

- AWS account
- Qdrant Cloud account
- Gemini API key
- GitHub account for the final workshop repository

## Local tools

Confirm these tools are available locally:

```bash
python3 --version
aws --version
docker --version
```

What you should see:

- Python is available.
- AWS CLI is available.
- Docker is available inside the WSL distro where this repo lives.

If `docker` is not found in WSL, open Docker Desktop on Windows and enable WSL integration for the distro you are using.

## AWS permissions needed

You need permission to create or inspect:

- Lambda function and Function URL
- ECR repository and image
- DynamoDB table
- CloudWatch log groups, metric filters, and alarms
- EventBridge Scheduler schedule
- SNS topic and email subscription
- IAM roles or policies for Lambda and Scheduler
- S3 object only if your fallback recipe JSON is stored there

## Cost control

In the AWS account used for this project, the checked project cost was `$0`, even when credits were included in the billing view.

The workshop was still designed with cost control in mind because another account may have different Free Tier, credits, region, or resource-lifetime behavior.

Use a small setup:

- one Lambda function for the final E5 path
- one ECR repository and one image tag
- one DynamoDB table
- one SNS topic
- one EventBridge schedule
- one metric filter and one alarm
- Qdrant Cloud free tier or a low-cost temporary cluster

Avoid these in the main path:

- EC2
- NAT Gateway
- ECS/Fargate
- RDS
- OpenSearch
- API Gateway
- Route 53
- CloudFront

## Resource tags

Tags are not the main technical topic, but they make cleanup easier.

Recommended tags:

| Key | Value |
| --- | --- |
| `Project` | `aws-vn-recipe-workshop` |
| `Purpose` | `fcj-workshop` |
| `Owner` | `<your-name>` |
| `Environment` | `workshop` |

## Account constraint and future improvement

The project stayed intentionally small partly because the AWS account used during development had pending activation limitations. This constraint made it safer to focus on Lambda, ECR, DynamoDB, CloudWatch, Scheduler, SNS, Qdrant Cloud, and Gemini instead of a larger public web architecture.

Lab 117, `Build a Complete serverless Chat Website`, is a useful future reference. Its static chat application path connects S3 static hosting with API Gateway, Lambda, DynamoDB, Cognito, and CloudFront. That improvement was not implemented here because CloudFront and the broader public hosting path were outside the current account and workshop scope.

## Secret handling

Never commit real secrets. Keep these values only in local `.env` files or Lambda environment variables:

- Gemini API key
- Qdrant API key
- Qdrant URL
- Lambda Function URL
- AWS access keys
- AWS account ID

Use placeholders in documentation:

```text
<account-id>
<function-url-redacted>
<qdrant-url-redacted>
<qdrant-api-key-redacted>
<gemini-api-key-redacted>
```

## What you accomplish in this section

You know the region, tools, permissions, `$0` measured cost result, tagging convention, account constraint, and redaction rules before creating resources.
