---
title: "Tuần 8"
date: 2024-01-01
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

**Thời gian:** `27/04/2026 - 03/05/2026`

## Trọng tâm

Chuyển từ đọc paper CLEF sang fine-tuning multilingual E5 và re-ranker experiments cho scientific source retrieval.

## Công việc đã hoàn thành

- Tập trung fine-tune multilingual E5 và re-ranker model cho CLEF CheckThat! task.
- Kết nối bài học retrieval từ CLEF với hướng recipe-assistant retrieval sau này.
- Giữ [Qdrant](https://qdrant.tech/documentation/) và RAG làm nền tảng kỹ thuật khả thi cho workshop FCJ sau này.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 27/04/2026 | Kết thúc giai đoạn đọc tập trung chính về các CheckThat! 2025 papers liên quan đến [CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/). | Phần đọc tập trung vào truy xuất source papers từ implicit scientific claims. |
| 28/04/2026 | Chuyển trọng tâm CLEF từ paper review sang fine-tuning multilingual E5 và re-ranker. | Đây là điểm bắt đầu giai đoạn experiment tập trung cho CheckThat! task. |
| 29/04/2026 | Setup và chạy fine-tuning experiments cho CLEF với multilingual E5, đồng thời planning cho re-ranker stage. | Tập trung cải thiện candidate retrieval quality cho scientific source-retrieval task. |
| 30/04/2026 | Làm CLEF model fine-tuning và retrieval experiment planning. | Công việc tập trung vào embedding và re-ranking choices thay vì AWS implementation. |
| 01/05/2026 | Theo dõi focused CLEF fine-tuning workflow và review hướng experiment. | Trọng tâm chính vẫn là multilingual E5 và re-ranker experimentation. |
| 02/05/2026 | Tổng hợp ghi chú fine-tuning CLEF và các quan sát về retrieval task. | Giữ entry cuối tuần vì liên quan đến giai đoạn CLEF tập trung. |
| 03/05/2026 | Phác thảo các retrieval experiments tiếp theo cho CLEF và rà soát khả năng chuyển bài học sang recipe retrieval. | Kết quả chính là hiểu rõ hơn về retrieval/evaluation mindset. |

## Reflection và bài học rút ra

Tuần này chủ yếu là giai đoạn fine-tuning cho CLEF. Tôi tập trung vào multilingual E5 và re-ranker experiments cho CheckThat! retrieval task, từ đó hiểu rõ hơn vai trò của embeddings, candidate retrieval, và ranking quality. Đây chưa phải tuần implementation AWS, nhưng củng cố retrieval/evaluation mindset cho RAG path của recipe assistant sau này.
