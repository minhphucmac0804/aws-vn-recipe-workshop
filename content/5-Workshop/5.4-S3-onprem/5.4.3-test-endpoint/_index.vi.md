---
title : "Kiểm thử Chainlit, Lambda, DynamoDB, và CloudWatch"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

## Mục tiêu

Chứng minh final Lambda RAG backend chạy end to end và để lại bằng chứng cho reviewer.

## Bước 1 - Tạo Lambda test event

Dùng event dạng HTTP nếu handler cần Function URL format:

```json
{
  "requestContext": {"http": {"method": "POST"}},
  "headers": {"content-type": "application/json"},
  "body": "{\"query\":\"Gỏi\"}",
  "isBase64Encoded": false
}
```

![Lambda test success](/images/5-Workshop/workshop-005/02-lambda-rag/21-test-success.png)
![Lambda response evidence](/images/5-Workshop/workshop-005/02-lambda-rag/22-test-success.png)

## Bước 2 - Kiểm tra DynamoDB query log

![DynamoDB item test success](/images/5-Workshop/workshop-005/02-lambda-rag/23-item-test-success.png)

## Bước 3 - Kiểm tra CloudWatch logs

![CloudWatch structured log](/images/5-Workshop/workshop-005/02-lambda-rag/24-cloudwatch.png)

## Bước 4 - Kiểm thử Chainlit

Hỏi một câu như:

```text
Gợi ý món ăn với thịt gà và rau củ.
```

![Grounded answer example 1](/images/5-Workshop/workshop-005/02-lambda-rag/25-answer-false.png)
![Grounded answer example 2](/images/5-Workshop/workshop-005/02-lambda-rag/26-answer-true.png)
