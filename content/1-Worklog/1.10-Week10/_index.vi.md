---
title: "Tuần 10"
date: 2024-01-01
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

**Thời gian:** `11/05/2026 - 17/05/2026`

## Trọng tâm

Chẩn đoán chất lượng retrieval thấp trong food-recipe project và thử xem LLM-based dataset enrichment có thể cải thiện nền tảng retrieval hay không.

## Công việc đã hoàn thành

- Điều tra nguyên nhân retrieval component trả kết quả chất lượng thấp.
- Xác định hai nguyên nhân chính: hạn chế của model/retrieval và chất lượng thấp của dữ liệu công thức tiếng Việt.
- Đặt mục tiêu cải thiện retrieval bằng cách xử lý và làm giàu dataset.
- Lập kế hoạch tạo attributes mới và trích xuất thông tin từ các field hiện có.
- Fine-tune một Qwen model nhỏ cho data-processing task, sau đó nhận thấy kết quả fine-tuning không đem lại đủ giá trị cho task tổng thể và quyết định dùng Gemini API.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 11/05/2026 | Bắt đầu điều tra retrieval quality thấp trong food-recipe project. | Kiểm tra vấn đề đến từ retrieval model, chất lượng dữ liệu tiếng Việt, hay cả hai. |
| 13/05/2026 | Hoàn thành phần chẩn đoán chính và đổi kế hoạch từ chỉ chỉnh retrieval sang cải thiện chính dataset. | Xác định mục tiêu: tạo recipe attributes sạch và hữu ích hơn để hỗ trợ retrieval. |
| 14/05/2026 | Thiết kế các dataset attributes mới và mapping các recipe fields hiện có với thông tin cần trích xuất. | Đây là kế hoạch data-processing cụ thể đầu tiên cho recipe dataset. |
| 15/05/2026 | Tham gia office visit for studying và thêm thử nghiệm fine-tune Qwen nhỏ vào kế hoạch dataset processing. | Thử nghiệm nhằm kiểm tra liệu một language model nhỏ có thể xử lý dữ liệu công thức tiếng Việt mà không phụ thuộc hoàn toàn vào external API hay không. |
| 16/05/2026 | Chạy và theo dõi Qwen fine-tuning experiment cho data-processing task. | Thử nghiệm hữu ích cho việc học, nhưng vẫn cần đánh giá lại theo chất lượng output và giá trị với project. |
| 17/05/2026 | Hoàn thành fine-tuning experiment và quyết định không dùng nó làm processing path chính. | Kết quả chưa đem lại đủ giá trị cho task tổng thể, nên bước tiếp theo chuyển sang Gemini API. |

## Reflection và bài học rút ra

Tuần này là bước ngoặt vì tôi không còn xem retrieval chỉ là vấn đề model. Việc chẩn đoán cho thấy chất lượng dữ liệu tiếng Việt, thiết kế attributes, và preprocessing cũng rất quan trọng. Qwen fine-tuning hữu ích cho việc học, nhưng quyết định dùng Gemini API giúp workflow xử lý dữ liệu thực tế hơn.
