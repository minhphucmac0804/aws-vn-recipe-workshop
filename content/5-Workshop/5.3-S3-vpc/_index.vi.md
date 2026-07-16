---
title : "Chuẩn bị Qdrant Cloud"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

## Mục tiêu

Trong phần này, bạn chuẩn bị hosted vector database cho final Lambda RAG backend.

Qdrant Cloud lưu recipe vectors. Sau đó Lambda gửi multilingual E5 query embedding đến Qdrant và nhận top-k recipe matches.

## Ghi chú về tiến trình dự án

Dự án không bắt đầu trực tiếp từ cloud backend. Nó đi theo các bước:

```text
baseline serverless prototype -> local Qdrant retrieval validation -> hosted Qdrant Cloud -> final Lambda RAG backend
```

Điều này giúp giải thích vì sao một số screenshots/validation xuất hiện trước khi backend cloud cuối cùng hoàn thiện. Workshop cuối vẫn tập trung vào hosted Qdrant Cloud và Lambda backend path.

## Các trang trong phần này

1. [Tạo Qdrant Cloud collection](5.3.1-create-gwe/)
2. [Load và kiểm tra recipe vectors](5.3.2-test-gwe/)

## Collection chính

```text
workshop_vn_recipes_e5_base_cloud
```

Collection lỗi chỉ dùng cho fallback alarm test:

```text
workshop_vn_recipes_e5_base_cloud_broken
```

![Loaded collection](/images/5-Workshop/workshop-005/01-qdrant-cloud/06-loaded-collection.png)
