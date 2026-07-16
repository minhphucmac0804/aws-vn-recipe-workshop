---
title: "Tuần 13"
date: 2024-01-01
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

**Thời gian:** `01/06/2026 - 07/06/2026`

## Trọng tâm

Quay lại xử lý dữ liệu food-recipe bằng cách kiểm tra các attributes version 1 do Gemini tạo và lập kế hoạch cải thiện dataset version 2.

## Công việc đã hoàn thành

- Rà soát các attributes đã được Gemini API tạo trước đó, xem như version 1 dataset.
- Thực hiện EDA và kiểm tra kỹ hơn các generated attributes mà trước đó chưa có thời gian review sâu trong tuần viết CLEF note.
- Xác định các vấn đề chất lượng còn lại trong recipe dataset đã xử lý.
- Lập kế hoạch tạo attributes version 2 dựa trên các field hiện có trong dataset.
- Chuẩn bị thử pipeline xử lý dữ liệu bằng Qwen với GPU thông qua Modal.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 01/06/2026 | Quay lại task xử lý food-recipe data và rà soát các attributes version 1 do Gemini tạo. | Tập trung hiểu output của lần xử lý trước. |
| 02/06/2026 | Kiểm tra từng field trong các generated attributes version 1. | Tách các recipe attributes có khả năng hữu ích khỏi các field nhiễu hoặc chưa đáng tin cậy. |
| 03/06/2026 | Kiểm tra dataset quality và attribute consistency trên các recipe records đã xử lý. | Xác nhận retrieval improvement sẽ bị giới hạn nếu generated attributes vẫn nhiễu. |
| 04/06/2026 | Lập kế hoạch các attributes version 2 dựa trên field hiện có. | Chuyển từ inspection sang thiết kế lần xử lý tiếp theo. |
| 05/06/2026 | Lập kế hoạch version 2 data-processing và rà soát Qwen như model option tiếp theo. | Cân nhắc dùng GPU-backed infrastructure vì experiment tiếp theo cần LLM inference nặng hơn. |
| 06/06/2026 | Tham gia sự kiện kỹ thuật Saturday Meet-up. | Trọng tâm sự kiện: Docker, GraphRAG, operations, troubleshooting, và định hướng nghề nghiệp trong AI/cloud. Reference: [Các sự kiện đã tham gia](../../4-EventParticipated/4.3-Event3/). |
| 07/06/2026 | Tổng hợp version 2 attribute plan trước khi triển khai. | Kế hoạch rõ hơn version 1 nhưng vẫn rủi ro vì output quality phụ thuộc vào task design và model behavior. |

## Reflection và bài học rút ra

Tuần này cho thấy kiểm tra generated attributes cũng quan trọng như việc tạo ra chúng. Output version 1 từ Gemini có một số cấu trúc hữu ích, nhưng EDA và inspection cho thấy vẫn còn vấn đề chất lượng. Điều này khiến kế hoạch version 2 có chủ đích hơn, dù vẫn còn rủi ro.
