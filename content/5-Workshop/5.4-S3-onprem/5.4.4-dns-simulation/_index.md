---
title : "Add Scheduler, Alarm, and SNS Fallback Evidence"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4.4. </b> "
---

## Goal

Add lightweight observability so the reviewer can see scheduled health checks and email notification for controlled fallback.

## Step 1 - Create an EventBridge Scheduler health check

Open:

```text
Amazon EventBridge -> Schedules -> Create schedule
```

Recommended values:

```text
Name: workshop-e5-daily-healthcheck
Target: AWS Lambda Invoke
Lambda: vnc-rag-query-retriever-e5-image
Payload: {"query":"Gỏi"}
```

For short validation, `rate(1 minute)` is acceptable briefly. After testing, slow it down or disable it.

What you should see:

![Create schedule step 1](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/27-create-schedule-step-1.png)
![Create schedule step 2](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/28-create-schedule-step-2.png)
![Create schedule step 3](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/29-create-schedule-step-3.png)
![Create schedule step 4](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/30-create-schedule-step-4.png)
![Schedule created](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/32-schedule-created.png)

## Step 2 - Create SNS topic and email subscription

Open:

```text
Amazon SNS -> Topics -> Create topic
```

Recommended topic name:

```text
workshop-e5-lambda-alerts
```

Then create an email subscription and confirm the email.

What you should see:

![Create SNS topic](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/31-create-sns-topic.png)
![Topic created](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/33-topic-created.png)
![Create subscription](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/34-create-subscription.png)
![Subscription created](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/35-subscription-created.png)

## Step 3 - Create fallback metric filter

Open the Lambda log group:

```text
CloudWatch -> Logs -> Log groups -> /aws/lambda/vnc-rag-query-retriever-e5-image
```

Create a metric filter with:

```text
Filter pattern: "rag_branch_failed"
Metric namespace: Workshop/RAG
Metric name: FallbackDetected
Metric value: 1
```

What you should see:

![Metric filter](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/45-metric-filter.png)
![Create filter step 1](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/46-create-filter-step-1.png)
![Create filter step 2](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/47-create-filter-step-2.png)
![Create filter step 3](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/48-create-filter-step-3.png)
![Filter created](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/49-filter-created.png)

## Step 4 - Create fallback alarm

Open:

```text
CloudWatch -> Alarms -> Create alarm
```

Use the custom metric:

```text
Namespace: Workshop/RAG
Metric: FallbackDetected
Statistic: Sum
Period: 5 minutes
Condition: Greater/Equal 1
Action: send to workshop-e5-lambda-alerts SNS topic
```

What you should see:

![Create alarm](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/36-create-alarms.png)
![Create alarm step 1](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/37-create-alarm-step-1.png)
![Select metric](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/38-select-metric.png)
![Create alarm review](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/39-create-alarm-step-1-review.png)
![Create alarm step 2](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/40-create-alarm-step-2.png)
![Create alarm step 3](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/41-create-alarm-step-3.png)
![Create alarm step 4](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/42-create-alarm-step-4.png)
![Alarm created](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/43-alarm-created.png)

## Step 5 - Trigger controlled fallback

Temporarily change only this Lambda environment variable:

```text
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud_broken
```

Then invoke the Lambda through Scheduler or a direct test.

Expected result:

- Lambda attempts the RAG branch
- Qdrant collection lookup fails
- Lambda logs `rag_branch_failed`
- handler falls back to the internal keyword path
- CloudWatch metric increments
- alarm enters `ALARM`
- SNS sends an email

Evidence:

![Fallback triggered](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/44-scheduler-run-fallback-triggered.png)
![SNS email sent](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/55-mail-sent.jpg)

Immediately restore:

```text
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud
```

## What you accomplished

You proved not only that the application works, but that a controlled degradation is visible in logs, metrics, alarms, and email.
