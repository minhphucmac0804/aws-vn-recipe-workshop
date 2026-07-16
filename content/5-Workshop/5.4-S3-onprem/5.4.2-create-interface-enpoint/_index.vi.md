---
title : "Tạo và cấu hình Lambda function"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.4.2. </b> "
---

## Mục tiêu

Tạo Lambda function mới từ ECR image và cấu hình cho luồng E5 RAG.

## Bước 1 - Tạo function

1. Mở `AWS Lambda`.
2. Chọn `Create function`.
3. Chọn `Container image`.
4. Đặt tên, ví dụ:

```text
vnc-rag-query-retriever-e5-image
```

5. Chọn ECR image đã push.
6. Tạo function.

![Create Lambda function](/images/5-Workshop/workshop-005/02-lambda-rag/14-create-lambda-function.png)
![Image selection](/images/5-Workshop/workshop-005/02-lambda-rag/15-image-selection.png)
![Function creation success](/images/5-Workshop/workshop-005/02-lambda-rag/16-function-creation-success.png)

## Bước 2 - Thêm environment variables

Dựa trên:

```text
project/lambda/lambda_e5_env.example
```

![Environment variables](/images/5-Workshop/workshop-005/02-lambda-rag/17-add-env-variables.png)

## Bước 3 - Cấu hình runtime

Gợi ý ban đầu:

```text
Memory: 2048 MB
Timeout: 60 seconds
Ephemeral storage: 512 MB
```

![Update general config](/images/5-Workshop/workshop-005/02-lambda-rag/18-update-general-config.png)

## Bước 4 - Kiểm tra IAM role

Role cần quyền ghi CloudWatch logs, đọc fallback recipe JSON nếu dùng S3 fallback, và ghi DynamoDB query logs.

![Edit role](/images/5-Workshop/workshop-005/02-lambda-rag/19-edit-role.png)

## Bước 5 - Tạo Function URL

Cấu hình local testing:

```text
Auth type: NONE
Allowed origin: http://localhost:8000
Allowed method: POST
Allowed header: content-type
```

![Function URL created](/images/5-Workshop/workshop-005/02-lambda-rag/20-url-created-cors-configured.png)
