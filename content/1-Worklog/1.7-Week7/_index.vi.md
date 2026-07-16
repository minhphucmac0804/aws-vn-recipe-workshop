---
title: "Tuần 7"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

**Thời gian:** `20/04/2026 - 26/04/2026`

## Trọng tâm

Hoàn thành phần học RAG và đọc các paper CLEF về scientific source retrieval để hiểu retrieval pipeline thực tế.

## Công việc đã hoàn thành

- Hoàn thành khóa [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) và ghi nhận cần ôn lại sau.
- Đọc các CheckThat! 2025 papers liên quan đến scientific source-retrieval task, dùng [CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/) làm reference gần nhất cho task hiện tại.
- Push code trong buổi họp nhóm và làm rõ các task tiếp theo cho đồ án tốt nghiệp.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 20/04/2026 | Học khóa [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) và rà soát yêu cầu retrieval của CLEF CheckThat!. | Kết nối pattern RAG gồm query, context retrieval, và grounded answer generation với bài toán scientific source retrieval của CLEF. |
| 21/04/2026 | Sắp xếp backlog task đang mở giữa RAG, Qdrant, CLEF, và đồ án tốt nghiệp. | Làm rõ các work streams song song để ưu tiên task kỹ thuật tiếp theo. |
| 22/04/2026 | Hoàn thành khóa [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) và bắt đầu đọc tập trung các CheckThat! 2025 papers về scientific source retrieval. | References chính gồm [AIRwaves](https://arxiv.org/pdf/2509.19509), [Deep Retrieval](https://ceur-ws.org/Vol-4038/paper_89.pdf), và [Claim2Source](https://ceur-ws.org/Vol-4038/paper_94.pdf). |
| 23/04/2026 | Đọc các CheckThat! papers cùng dạng task từ [CLEF 2025 Working Notes Vol. 4038](https://ceur-ws.org/Vol-4038/). | Tập trung vào retrieval pipeline để nối scientific claims trên social media với source papers. |
| 24/04/2026 | So sánh sparse retrieval, dense retrieval, hybrid retrieval, và re-ranking ideas từ các CLEF papers. | Giúp tôi hiểu rõ hơn vì sao retrieval quality phụ thuộc vào cả candidate generation và re-ranking. |
| 25/04/2026 | Tổng hợp ghi chú từ các CheckThat! retrieval papers thành ý tưởng triển khai cho competition task. | Giữ entry cuối tuần vì liên quan trực tiếp đến chuẩn bị CLEF task. |
| 26/04/2026 | Review nội dung RAG và CheckThat! retrieval đã học trong tuần, rồi chọn task tiếp theo cho experiments. | Kết quả chính là hiểu rõ hơn về retrieval pipelines và evaluation-driven development. |

## Reflection và bài học rút ra

Tuần này làm hướng retrieval trở nên cụ thể hơn. Khóa RAG giúp tôi hiểu rõ hơn quan hệ giữa query, context, và answer generation, còn việc đọc paper CheckThat! cho thấy các hệ thống scientific source retrieval thường kết hợp BM25, dense embeddings, hard negatives, và re-ranking. Workshop AWS cuối cùng không phải là một hệ thống CLEF, nhưng phần đọc này củng cố cách nghĩ về retrieval và evaluation cho RAG path của recipe assistant.
