---
title : "Chuẩn bị và kiểm soát chi phí"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

## Region

Sử dụng một region xuyên suốt workshop:

```text
ap-southeast-1
```

## Tài khoản cần có

- AWS account
- Qdrant Cloud account
- Gemini API key
- GitHub account cho repo workshop cuối cùng

## Công cụ local

Kiểm tra các công cụ local:

```bash
python3 --version
aws --version
docker --version
```

Nếu `docker` không chạy trong WSL, mở Docker Desktop trên Windows và bật WSL integration cho distro đang dùng.

## Quyền AWS cần có

Bạn cần quyền tạo hoặc kiểm tra Lambda, ECR, DynamoDB, CloudWatch, EventBridge Scheduler, SNS, IAM role/policy, và S3 nếu fallback recipe JSON nằm trong S3.

## Kiểm soát chi phí

Trong tài khoản AWS dùng cho dự án này, chi phí đã kiểm tra là `$0`, kể cả khi tính phần credits trong billing view.

Dù vậy, workshop vẫn giữ setup nhỏ vì tài khoản khác có thể có Free Tier, credits, region, hoặc thời gian giữ tài nguyên khác nhau: một Lambda, một ECR repository, một DynamoDB table, một SNS topic, một Scheduler, một metric filter/alarm, và Qdrant Cloud free tier hoặc cluster tạm chi phí thấp.

Tránh dùng EC2, NAT Gateway, ECS/Fargate, RDS, OpenSearch, API Gateway, Route 53, hoặc CloudFront trong luồng chính.

## Resource tags

Tags không phải nội dung kỹ thuật chính, nhưng giúp cleanup dễ hơn.

| Key | Value |
| --- | --- |
| `Project` | `aws-vn-recipe-workshop` |
| `Purpose` | `fcj-workshop` |
| `Owner` | `<your-name>` |
| `Environment` | `workshop` |

## Giới hạn tài khoản và hướng cải thiện

Dự án được giữ nhỏ một phần vì tài khoản AWS dùng trong quá trình phát triển có pending activation limitations. Vì vậy workshop tập trung vào Lambda, ECR, DynamoDB, CloudWatch, Scheduler, SNS, Qdrant Cloud, và Gemini thay vì public web architecture lớn hơn.

Lab 117, `Build a Complete serverless Chat Website`, là hướng tham khảo tương lai. Static chat application của lab đó kết nối S3 static hosting với API Gateway, Lambda, DynamoDB, Cognito, và CloudFront. Hướng này chưa được triển khai vì CloudFront và public hosting path nằm ngoài phạm vi tài khoản và workshop hiện tại.

## Quản lý secrets

Không commit secrets. Dùng placeholder trong tài liệu:

```text
<account-id>
<function-url-redacted>
<qdrant-url-redacted>
<qdrant-api-key-redacted>
<gemini-api-key-redacted>
```
