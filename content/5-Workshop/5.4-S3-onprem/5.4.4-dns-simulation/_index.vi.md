---
title : "Thêm Scheduler, alarm, và SNS fallback evidence"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4.4. </b> "
---

## Mục tiêu

Thêm observability nhẹ để reviewer thấy health check theo lịch và email notification khi controlled fallback xảy ra.

## Bước 1 - Tạo EventBridge Scheduler health check

```text
Amazon EventBridge -> Schedules -> Create schedule
```

Giá trị gợi ý:

```text
Name: workshop-e5-daily-healthcheck
Target: AWS Lambda Invoke
Lambda: vnc-rag-query-retriever-e5-image
Payload: {"query":"Gỏi"}
```

![Create schedule step 1](/images/5-Workshop/workshop-005/02-lambda-rag/27-create-schedule-step-1.png)
![Create schedule step 2](/images/5-Workshop/workshop-005/02-lambda-rag/28-create-schedule-step-2.png)
![Create schedule step 3](/images/5-Workshop/workshop-005/02-lambda-rag/29-create-schedule-step-3.png)
![Create schedule step 4](/images/5-Workshop/workshop-005/02-lambda-rag/30-create-schedule-step-4.png)
![Schedule created](/images/5-Workshop/workshop-005/02-lambda-rag/32-schedule-created.png)

## Bước 2 - Tạo SNS topic và email subscription

![Create SNS topic](/images/5-Workshop/workshop-005/02-lambda-rag/31-create-sns-topic.png)
![Topic created](/images/5-Workshop/workshop-005/02-lambda-rag/33-topic-created.png)
![Create subscription](/images/5-Workshop/workshop-005/02-lambda-rag/34-create-subscription.png)
![Subscription created](/images/5-Workshop/workshop-005/02-lambda-rag/35-subscription-created.png)

## Bước 3 - Tạo fallback metric filter

```text
Filter pattern: "rag_branch_failed"
Metric namespace: Workshop/RAG
Metric name: FallbackDetected
Metric value: 1
```

![Metric filter](/images/5-Workshop/workshop-005/02-lambda-rag/45-metric-filter.png)
![Filter created](/images/5-Workshop/workshop-005/02-lambda-rag/49-filter-created.png)

## Bước 4 - Tạo fallback alarm

![Create alarm](/images/5-Workshop/workshop-005/02-lambda-rag/36-create-alarms.png)
![Select metric](/images/5-Workshop/workshop-005/02-lambda-rag/38-select-metric.png)
![Alarm created](/images/5-Workshop/workshop-005/02-lambda-rag/43-alarm-created.png)

## Bước 5 - Trigger controlled fallback

Tạm thời đổi:

```text
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud_broken
```

Sau khi test xong, đổi lại:

```text
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud
```

![Fallback triggered](/images/5-Workshop/workshop-005/02-lambda-rag/44-scheduler-run-fallback-triggered.png)
![SNS email sent](/images/5-Workshop/workshop-005/02-lambda-rag/55-mail-sent.jpg)
