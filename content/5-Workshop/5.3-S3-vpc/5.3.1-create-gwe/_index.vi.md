---
title : "Tạo Qdrant Cloud collection"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

## Mục tiêu

Tạo Qdrant Cloud cluster và collection cho luồng workshop cuối cùng.

## Bước 1 - Mở Qdrant Cloud

1. Đăng nhập Qdrant Cloud.
2. Tạo free-tier hoặc low-cost cluster.
3. Chọn region phù hợp cho test.
4. Chờ cluster sẵn sàng.

![Qdrant cluster creation](/images/5-Workshop/workshop-005/01-qdrant-cloud/01-create-cluster.png)

## Bước 2 - Mở cluster dashboard

1. Mở cluster dashboard.
2. Kiểm tra cluster đang chạy.
3. Lưu Qdrant URL ở local, không publish.

![Qdrant cluster dashboard](/images/5-Workshop/workshop-005/01-qdrant-cloud/02-cluster-dashboard.png)

## Bước 3 - Tạo E5 collection

Collection chính:

```text
workshop_vn_recipes_e5_base_cloud
```

Thông số khuyến nghị:

```text
Vector size: 768
Distance: Cosine
```

![Qdrant collection creation](/images/5-Workshop/workshop-005/01-qdrant-cloud/03-collection-creation.png)

## Bước 4 - Kiểm tra collection rỗng

Trước khi load dữ liệu, collection có thể đang rỗng. Đây là trạng thái bình thường.

![Empty collection](/images/5-Workshop/workshop-005/01-qdrant-cloud/05-empty-collection.png)
