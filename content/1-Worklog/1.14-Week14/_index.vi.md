---
title: "Tuần 14"
date: 2024-01-01
weight: 14
chapter: false
pre: " <b> 1.14. </b> "
---

**Thời gian:** `08/06/2026 - 14/06/2026`

## Trọng tâm

Triển khai thử nghiệm data-processing version 2 bằng Qwen với GPU của Modal, sau đó đánh giá vì sao output không đạt mục tiêu chất lượng kỳ vọng.

## Công việc đã hoàn thành

- Bắt đầu chạy pipeline data-processing version 2 khoảng ngày 08/06 hoặc 09/06.
- Dùng Qwen model thông qua GPU resources của Modal, trong khi orchestration code vẫn chạy ở Colab.
- Pipeline chạy được và tạo ra dữ liệu ở mức kỹ thuật.
- Nhận thấy chất lượng dữ liệu sinh ra không tốt hơn output version 1 từ Gemini.
- Rút ra rằng infrastructure mạnh hơn và LLM khác không tự động cải thiện chất lượng dataset.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 08/06/2026 | Bắt đầu triển khai hoặc chuẩn bị Qwen-based version 2 processing pipeline. | Việc bắt đầu khá muộn trong giai đoạn hai tuần nên còn ít thời gian để sửa sai. |
| 09/06/2026 | Chạy pipeline xử lý dữ liệu bằng Qwen với GPU thông qua Modal. | Pipeline chạy được và tạo output data. |
| 10/06/2026 | Kiểm tra Qwen-generated outputs từ version 2 pipeline. | Pipeline chạy được về kỹ thuật, nhưng các sample ban đầu làm xuất hiện lo ngại về semantic accuracy và usefulness. |
| 11/06/2026 | So sánh Qwen-generated attributes với output version 1 từ Gemini. | Review cho thấy pipeline mới không cải thiện attribute quality một cách rõ ràng. |
| 12/06/2026 | Kiểm tra các lỗi data-quality trong hướng Qwen-based processing. | Nhận ra model choice và GPU execution không giải quyết được prompt chưa rõ, source data yếu, hoặc evaluation gaps. |
| 13/06/2026 | Tổng hợp findings từ version 2 experiment. | Evaluation cho thấy experiment chạy được về kỹ thuật nhưng không đạt dataset-quality goal. |
| 14/06/2026 | Reflection về kết quả và ghi nhận giới hạn của việc chỉ dựa vào model choice/GPU execution. | Bài học chính: task design và source data quality quan trọng hơn model size/infrastructure. |

## Reflection và bài học rút ra

Thử nghiệm thành công về mặt kỹ thuật vì code chạy và tạo ra dữ liệu, nhưng không đạt mục tiêu data-quality lớn hơn. Việc dùng Modal GPU resources và Qwen model giúp tôi học thêm về chạy LLM workloads ngoài môi trường local. Bài học chính là model size và infrastructure không tự động cải thiện output nếu task design, evaluation criteria, và source data quality chưa tốt.
