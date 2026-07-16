---
title : "Giới thiệu và kiến trúc"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

## Mục tiêu

Trong workshop này, bạn triển khai và kiểm tra một Vietnamese recipe assistant nhỏ theo hướng RAG. Giao diện chạy local bằng Chainlit, còn backend chính chạy trên AWS Lambda dưới dạng containerized RAG backend.

## Kiến trúc

![Final architecture](/images/5-Workshop/aws-workshop-architecture-final.png)

Luồng request chính:

```text
User hỏi món ăn
  -> Chainlit gửi query đến Lambda Function URL
  -> Lambda tạo multilingual E5 query embedding
  -> Lambda tìm top-k recipe context trong Qdrant Cloud
  -> Lambda gọi Gemini để trả lời dựa trên context
  -> Chainlit hiển thị kết quả
```

## Vai trò dịch vụ

- `Chainlit`: giao diện local để hỏi món ăn.
- `Lambda Function URL`: HTTPS endpoint cho local app.
- `AWS Lambda`: backend dạng container chạy multilingual E5 retrieval và Gemini answer generation.
- `Amazon ECR`: nơi lưu container image cho Lambda.
- `Qdrant Cloud`: vector database lưu recipe embeddings.
- `Gemini`: tạo câu trả lời dựa trên recipe context.
- `DynamoDB`: lưu query logs làm bằng chứng.
- `CloudWatch Logs`: lưu structured runtime logs.
- `EventBridge Scheduler`: gọi health check theo lịch.
- `CloudWatch Metric Filter and Alarm`: phát hiện fallback event.
- `SNS`: gửi email khi alarm được kích hoạt.


## Demo video

<video controls preload="metadata" style="max-width: 100%; border: 1px solid #ddd; border-radius: 4px;">
  <source src="/videos/demo.mp4" type="video/mp4">
  Trình duyệt của bạn không hỗ trợ video tag.
</video>

### Demo Video Notes

Video ngắn này minh họa main working path của workshop:

1. Architecture overview: local Chainlit UI -> Lambda Function URL -> Lambda container -> Qdrant Cloud -> Gemini.
2. Chainlit success: một câu hỏi món ăn tiếng Việt được gửi và trả lời.
3. Lambda evidence: backend response dùng RAG path.
4. DynamoDB evidence: query được ghi vào query log table.

Các bằng chứng observability như CloudWatch logs, Scheduler health check, SNS alarm, và fallback behavior được cung cấp riêng trong evidence checklist screenshots.

## Bằng chứng cleanup

Bằng chứng cleanup được đặt trong [5.6 Cleanup](/vi/5-workshop/5.6-cleanup/). Các ảnh chụp cho thấy tài nguyên chính của workshop đã được xóa hoặc không còn active, còn cleanup checklist vẫn là artifact từng bước để kiểm tra rằng không còn tài nguyên bị bỏ sót.
