---
title : "Cleanup"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

## Mục tiêu

Xóa tài nguyên tạm thời để workshop không phát sinh chi phí về sau hoặc để lại credentials. Chi phí đã kiểm tra là `$0`, nhưng cleanup vẫn cần thiết vì billing có thể thay đổi nếu tài nguyên còn active.

## AWS cleanup checklist

Xóa hoặc kiểm tra:

- Lambda function `vnc-rag-query-retriever-e5-image`
- Lambda Function URL
- ECR image và ECR repository
- DynamoDB query log table
- S3 bucket/object dùng cho fallback recipe JSON hoặc package artifacts
- CloudWatch log groups
- CloudWatch metric filters
- CloudWatch alarms
- SNS topic và email subscription
- EventBridge Scheduler schedule
- IAM roles và inline policies
- IAM users và access keys tạo cho ECR push

## External cleanup checklist

Xóa hoặc kiểm tra:

- Qdrant Cloud cluster nếu chỉ tạo cho workshop
- Qdrant collection nếu cluster vẫn dùng lại
- Gemini API key nếu chỉ tạo cho project này
- Qdrant API key nếu từng bị lộ khi test
- local `.env` files chứa secrets
- Docker images tạm nếu cần dọn dung lượng


## Bằng chứng cleanup

Các ảnh dưới đây là bằng chứng tùy chọn cho reviewer. Chúng cho thấy các tài nguyên chính của workshop đã được xóa hoặc không còn active. Trước khi publish, cần giữ ảnh đã redact và tránh lộ account ID, ARN, email, API key, hoặc private URL.

| Bằng chứng | Ảnh chụp |
|---|---|
| EventBridge Scheduler đã xóa | ![EventBridge Scheduler đã xóa](/images/5-Workshop/cleanup/01-scheduler-deleted.png) |
| Lambda function đã xóa | ![Lambda function đã xóa](/images/5-Workshop/cleanup/02-lambda-deleted.png) |
| CloudWatch alarm đã xóa | ![CloudWatch alarm đã xóa](/images/5-Workshop/cleanup/03-alarm-deleted.png) |
| CloudWatch log group đã xóa | ![CloudWatch log group đã xóa](/images/5-Workshop/cleanup/04-cloudwatch-log-group-deleted.png) |
| DynamoDB table đã gửi yêu cầu xóa | ![DynamoDB table đã gửi yêu cầu xóa](/images/5-Workshop/cleanup/05-dynamodb-deleted.png) |
| DynamoDB không còn table | ![DynamoDB không còn table](/images/5-Workshop/cleanup/06-dynamodb-no-table-left.png) |
| ECR repository đã xóa | ![ECR repository đã xóa](/images/5-Workshop/cleanup/07-ecr-deleted.png) |
| IAM user đã xóa | ![IAM user đã xóa](/images/5-Workshop/cleanup/08-iam-user-deleted.png) |

## Ghi chú cleanup screenshots

Chỉ đăng cleanup screenshots nếu đã redact và thể hiện rõ tài nguyên đã xóa, disable, hoặc không còn active. Không dùng ảnh lộ account IDs, emails, keys, private URLs, hoặc resource ARNs.

## Kiểm tra redaction cuối

Không để markdown hoặc screenshot chứa AWS account IDs, Function URLs, API keys, access keys, email riêng tư, hoặc private repo links.
