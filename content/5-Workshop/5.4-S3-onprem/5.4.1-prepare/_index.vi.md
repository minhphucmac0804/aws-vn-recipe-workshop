---
title : "Build và push Lambda image"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.4.1. </b> "
---

## Mục tiêu

Build Lambda container image ở local và push lên Amazon ECR.

## Bước 1 - Kiểm tra file local

```bash
ls project/lambda/handler.py
ls project/lambda/Dockerfile.e5
ls project/lambda/requirements-lambda-e5.txt
ls project/extensions/rag/models/multilingual-e5-base/onnx/model.onnx
```

## Bước 2 - Build image

```bash
docker build -f project/lambda/Dockerfile.e5 -t vnc-rag-query-retriever-e5:qint8 .
```

Nếu `docker` không tìm thấy, sửa Docker Desktop WSL integration trước.

## Bước 3 - Tạo hoặc mở ECR repository

Repository gợi ý:

```text
aws-workshop/vnc-rag-query-retriever-e5
```

![ECR repository tags](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/02-add-repo-tags.png)

## Bước 4 - Dùng View push commands

![View push commands](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/11-view-push-commands.png)
![View push commands continued](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/12-view-push-commands.png)

## Bước 5 - Kiểm tra active image

![Active image](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/02-lambda-rag/13-active-image.png)
