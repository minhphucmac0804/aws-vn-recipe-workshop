---
title: "Tuần 11"
date: 2024-01-01
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

**Thời gian:** `18/05/2026 - 24/05/2026`

## Trọng tâm

Dùng Gemini API để xử lý recipe dataset, sau đó kiểm tra liệu các attributes được sinh ra có đủ đáng tin cậy cho retrieval work hay không.

## Công việc đã hoàn thành

- Dùng Gemini API cho LLM-assisted data processing sau khi quyết định không dựa vào kết quả fine-tune Qwen nhỏ.
- Tạo được một số attributes mới hữu ích cho recipe dataset.
- Thực hiện EDA trên dataset đã xử lý.
- Nhận thấy dữ liệu đã có cấu trúc tốt hơn ở một số phần, nhưng chất lượng dataset gốc vẫn giới hạn task tổng thể.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 18/05/2026 | Bắt đầu dùng Gemini API để xử lý recipe dataset. | Thay hướng fine-tuned small model bằng workflow API thực tế hơn. |
| 19/05/2026 | Sinh các recipe attributes mới từ những field hiện có bằng LLM-assisted extraction. | Tập trung làm ingredient, instruction, và recipe-description information có cấu trúc hơn. |
| 20/05/2026 | Kiểm tra tính nhất quán của generated outputs trong lúc chạy các batch dataset-processing còn lại. | Xem xét liệu các attributes mới có đủ ổn định để hỗ trợ retrieval experiments hay không. |
| 21/05/2026 | Tham gia office visit for studying, rà soát generated attributes, và xử lý thêm recipe records bằng Gemini. | Một số attributes có vẻ hữu ích cho retrieval và analysis sau này, nhưng vẫn cần EDA validation. |
| 22/05/2026 | Thực hành dùng draw.io và vẽ một AWS-style architecture diagram theo hướng dẫn vẽ architecture của FCJ. | Reference: [FCJ architecture drawing guide](https://www.youtube.com/watch?v=l8isyDe-GwY&list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i&index=2). Việc này giúp tôi vẽ kiến trúc workshop của mình rõ hơn về sau. |
| 23/05/2026 | Tham gia FCJ Community Day. | Trọng tâm sự kiện: AI engineering in production, context engineering, security, compliance, và cloud cost control. Reference: [Các sự kiện đã tham gia](../../4-EventParticipated/4.2-Event2/). |

## Reflection và bài học rút ra

Tuần này giúp tôi học cách dùng LLM APIs cho NLP-style data processing, không chỉ dùng như chatbot. Gemini-based processing tạo được một số attributes hữu ích, nhưng EDA cho thấy source dataset vẫn giới hạn chất lượng cuối. Bài học chính là LLM processing có thể hỗ trợ cấu trúc dữ liệu, nhưng không thể bù hoàn toàn cho dữ liệu đầu vào yếu.
