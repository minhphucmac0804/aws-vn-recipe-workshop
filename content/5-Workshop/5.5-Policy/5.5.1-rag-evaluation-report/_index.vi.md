---
title : "RAG Evaluation Report"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.5.1. </b> "
---

## Mục tiêu

Báo cáo này tóm tắt lượt đánh giá retrieval đầu tiên, theo hướng reviewer-friendly, cho final Lambda RAG backend cuối cùng của workshop.

Lớp retrieval được đánh giá là:

```text
E5 query embedding -> Qdrant Cloud retrieval -> top-k recipe results
```

## Phương pháp đánh giá

Lượt đánh giá này dùng cách làm RAG evaluation đơn giản:

- dùng một query set cố định
- chạy retrieval trên cùng bộ benchmark queries ở mỗi lần đánh giá
- kiểm tra top `K=5` kết quả
- đánh dấu relevant và not relevant
- tính `Precision@5`
- ghi một reviewer note ngắn cho mỗi query

Cách này được cố ý tách khỏi đánh giá câu trả lời cuối.

## Metric chính

```text
Precision@5 = relevant results in top 5 / 5
```

Metric này là đủ cho báo cáo retrieval đầu tiên của workshop vì nó dễ giải thích và reviewer có thể lặp lại dễ dàng.

## Kết quả được báo cáo

Baseline hiện tại của workshop đủ tốt để chứng minh một cloud RAG system hoạt động và có retrieval quality đo được.

Điểm tốt:

- final Lambda RAG backend RAG hoạt động ổn định trên cả 12 evaluation queries
- các câu hỏi theo tên món cụ thể hoặc nhóm món quen thuộc cho kết quả tốt nhất
- ví dụ tốt gồm `canh chua`, `món thịt kho`, `món cuốn`, `món chay đơn giản`, và `bún`

Điểm yếu:

- các câu hỏi broad hoặc theo intent mềm kém ổn định hơn
- ví dụ yếu hơn gồm `món gà thanh đạm`, `món cá nhẹ bụng`, và một số yêu cầu theo dịp sử dụng
- trong các trường hợp đó retrieval đôi khi trả về tập ứng viên lẫn tạp hơn, thay vì top-5 sạch

## Diễn giải

Kết quả này phù hợp với một workshop baseline đầu tiên.

Lớp retrieval đã hữu ích và dễ giải thích, nhưng đáng tin cậy hơn với các truy vấn món ăn cụ thể hoặc quen thuộc so với các truy vấn preference-style mềm hơn. Điều này cho reviewer thấy cả điểm mạnh lẫn giới hạn hiện tại.

## Liên hệ với AI report

Báo cáo này đánh giá hệ thống có retrieve đúng context hay không.

[AI Evaluation Report](../5.5.2-ai-evaluation-report/) đánh giá riêng việc Gemini có biến context đó thành câu trả lời cuối tốt hay không.
