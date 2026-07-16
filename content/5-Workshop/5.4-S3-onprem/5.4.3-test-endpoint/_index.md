---
title : "Validate Chainlit, Lambda, DynamoDB, and CloudWatch"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

## Goal

Prove that the live Lambda RAG backend works end to end and leaves reviewer evidence.

## Step 1 - Create a Lambda console test event

Open the Lambda function and create a test event.

Use an HTTP-shaped event if your handler expects Function URL format:

```json
{
  "requestContext": {
    "http": {
      "method": "POST"
    }
  },
  "headers": {
    "content-type": "application/json"
  },
  "body": "{\"query\":\"Gỏi\"}",
  "isBase64Encoded": false
}
```

Run the test.

What you should see:

![Lambda test success](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/21-test-success.png)
![Lambda response evidence](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/22-test-success.png)

Expected result:

- status is successful
- response body is valid JSON
- `mode_used` exists
- successful RAG tests should show `mode_used=rag`

## Step 2 - Check DynamoDB query log

Open the query log table, for example:

```text
RecipeQueryLogs
```

Look for a recent item from your test query.

What you should see:

![DynamoDB item test success](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/23-item-test-success.png)

Useful fields include:

- query text or redacted query text
- `mode_used`
- retrieval method
- result count
- fallback reason if any
- timestamp

## Step 3 - Check CloudWatch structured logs

Open:

```text
CloudWatch -> Logs -> Log groups -> /aws/lambda/vnc-rag-query-retriever-e5-image
```

What you should see:

![CloudWatch structured log](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/24-cloudwatch.png)

Useful log evidence:

- invocation happened
- branch selection is visible
- errors or fallback reasons are visible
- DynamoDB log-write events are visible

## Step 4 - Validate Chainlit response

Point local Chainlit to the Lambda Function URL using a local `.env` value.

Run Chainlit locally, then ask a known recipe query such as:

```text
Gợi ý món ăn với thịt gà và rau củ.
```

Expected result:

- Chainlit displays a grounded answer
- Lambda logs show the request
- DynamoDB stores a query log item

Evidence examples:

![Grounded answer example 1](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/25-answer-false.png)
![Grounded answer example 2](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/26-answer-true.png)

## What you accomplished

You proved the end-to-end path works from Lambda and Chainlit, and you captured DynamoDB and CloudWatch evidence.
