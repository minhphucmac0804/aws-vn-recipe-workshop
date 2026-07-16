---
title : "Load và kiểm tra recipe vectors"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

## Mục tiêu

Load recipe vectors vào Qdrant Cloud và kiểm tra retrieval trả về kết quả hợp lý.

Trang này cũng giải thích lịch sử local Qdrant. Trước khi final Lambda RAG backend hoàn thiện, dự án dùng local Qdrant branch để kiểm tra E5 retrieval. Nhánh này không phải deployment path cuối, nhưng giúp giải thích vì sao retrieval evidence xuất hiện trước các bước Lambda backend.

## Bước 1 - Cấu hình Qdrant settings

Trong `.env` local:

```text
WORKSHOP_QDRANT_URL=<qdrant-url-redacted>
WORKSHOP_QDRANT_API_KEY=<qdrant-api-key-redacted>
WORKSHOP_QDRANT_COLLECTION=workshop_vn_recipes_e5_base_cloud
```

Không commit `.env`.

## Bước 2 - Load vectors

Chạy loader từ project root:

```bash
python3 -m project.extensions.rag.local_qdrant.loader
```

## Bước 3 - Kiểm tra collection

![Loaded collection](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/06-loaded-collection.png)

![Collection items](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/07-collection-items.png)

## Bước 4 - Test retrieval trực tiếp

Dùng query như:

```text
gỏi mít thịt ba chỉ
```

Kết quả mong đợi: có ít nhất một recipe liên quan trong kết quả.

![Qdrant query result 1](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/08-result-01.png)
![Qdrant query result 2](/aws-vn-recipe-workshop/images/5-Workshop/workshop-005/01-qdrant-cloud/09-result-02.png)
