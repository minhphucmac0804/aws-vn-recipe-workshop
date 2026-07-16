---
title : "Cleanup"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

## Goal

Delete temporary resources so the workshop does not create future cost or leave credentials behind. The checked project cost was `$0`, but cleanup is still required because billing can change if resources remain active.

Cleanup is part of the workshop, not an optional extra step.

## AWS cleanup checklist

Delete or review these resources:

- Lambda function `vnc-rag-query-retriever-e5-image`
- Lambda Function URL
- ECR image and ECR repository
- DynamoDB query log table
- S3 bucket/object used for fallback recipe JSON or package artifacts
- CloudWatch log groups
- CloudWatch metric filters
- CloudWatch alarms
- SNS topic and email subscription
- EventBridge Scheduler schedule
- IAM roles and inline policies created for Lambda or Scheduler
- IAM users and access keys created for ECR push

## External cleanup checklist

Delete or review:

- Qdrant Cloud cluster if it was created only for the workshop
- Qdrant collection if the cluster will be reused
- Gemini API key if it was created only for this project
- Qdrant API key if it was exposed during testing
- local `.env` files containing secrets
- temporary Docker images if local disk space matters


## Cleanup evidence

The following screenshots are optional reviewer evidence. They show the main workshop resources after deletion or in an empty state. Before publishing, keep this evidence redacted and avoid exposing account IDs, ARNs, emails, API keys, or private URLs.

| Evidence | Screenshot |
|---|---|
| EventBridge Scheduler schedule deleted | ![EventBridge Scheduler deleted](/images/5-Workshop/cleanup/01-scheduler-deleted.png) |
| Lambda function deleted | ![Lambda function deleted](/images/5-Workshop/cleanup/02-lambda-deleted.png) |
| CloudWatch alarm deleted | ![CloudWatch alarm deleted](/images/5-Workshop/cleanup/03-alarm-deleted.png) |
| CloudWatch log group deleted | ![CloudWatch log group deleted](/images/5-Workshop/cleanup/04-cloudwatch-log-group-deleted.png) |
| DynamoDB table deletion requested | ![DynamoDB table deletion requested](/images/5-Workshop/cleanup/05-dynamodb-deleted.png) |
| DynamoDB table list empty | ![DynamoDB no tables left](/images/5-Workshop/cleanup/06-dynamodb-no-table-left.png) |
| ECR repository deleted | ![ECR repository deleted](/images/5-Workshop/cleanup/07-ecr-deleted.png) |
| IAM user deleted | ![IAM user deleted](/images/5-Workshop/cleanup/08-iam-user-deleted.png) |

## Cleanup screenshot note

Post cleanup screenshots only if they are redacted and clearly show resources deleted, disabled, or no longer active. Do not include screenshots that expose account IDs, emails, keys, private URLs, or resource ARNs.

## Final redaction check

Before publishing the final GitHub repo, confirm no markdown or screenshot contains:

- AWS account IDs
- Lambda Function URLs
- Gemini API keys
- Qdrant API keys
- Qdrant cluster URLs if private
- AWS access key IDs or secret access keys
- private email addresses
- private repo links

## What you accomplished

You removed the resources that could create cost or expose secrets after the workshop.
