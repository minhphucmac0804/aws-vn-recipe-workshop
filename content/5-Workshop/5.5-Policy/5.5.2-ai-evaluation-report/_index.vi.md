---
title : "AI Evaluation Report"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.5.2. </b> "
---

## Mục tiêu

Báo cáo này tóm tắt lượt đánh giá chất lượng câu trả lời đầu tiên, ở mức nhẹ và dễ đọc, cho final Lambda RAG backend cuối cùng của workshop.

Luồng đầy đủ được đánh giá là:

```text
Chainlit -> Lambda Function URL -> Lambda RAG backend -> Qdrant Cloud -> Gemini -> response
```

## Phương pháp đánh giá

AI evaluation giữ cách chấm điểm ở mức dễ đọc với con người.

Với mỗi query, câu trả lời cuối được đánh giá theo bốn tiêu chí:

- `Relevant`
- `Grounded`
- `Useful`
- `Honest`

Sau đó mỗi câu trả lời nhận một overall rating nhẹ như `Good`, `Partly good`, hoặc `Poor`, kèm một ghi chú ngắn.

## Kết quả được báo cáo

Baseline hiện tại thường tạo ra câu trả lời relevant và grounded cho các truy vấn món ăn Việt quen thuộc.

Điểm tốt:

- toàn bộ final Lambda RAG backend RAG trả về `mode_used=rag` trên cả 12 evaluation queries
- các truy vấn món cụ thể và nhóm món quen thuộc cho câu trả lời cuối tốt nhất
- ví dụ tốt gồm `canh chua`, `món thịt kho`, `món cuốn`, `món chay đơn giản`, và `bún`

Điểm yếu:

- các truy vấn broad, lifestyle-style, hoặc preference-style có độ ổn định thấp hơn
- ví dụ yếu hơn gồm `món gà thanh đạm`, `món cá nhẹ bụng`, và một số truy vấn theo dịp sử dụng
- trong các trường hợp đó câu trả lời cuối đôi khi tự tin hơn mức bằng chứng retrieve được hỗ trợ

## Diễn giải

Đây là một kết quả workshop đầu tiên khá tốt.

Hệ thống đã chứng minh được khả năng sinh câu trả lời hữu ích và phần lớn có grounding, nhưng lớp trả lời cuối vẫn phụ thuộc rõ vào chất lượng retrieval. Khi retrieval bị lẫn tạp hơn, chất lượng câu trả lời cũng biến động hơn.

## Liên hệ với RAG report

Báo cáo này đánh giá chất lượng câu trả lời cuối.

[RAG Evaluation Report](../5.5.1-rag-evaluation-report/) đánh giá riêng việc lớp retrieval có trả về đúng context ngay từ đầu hay không.
