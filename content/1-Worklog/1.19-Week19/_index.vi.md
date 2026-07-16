---
title: "Tuần 19"
date: 2024-01-01
weight: 19
chapter: false
pre: " <b> 1.19. </b> "
---

**Thời gian:** `13/07/2026 - 16/07/2026`

## Trọng tâm

Hoàn thiện repo workshop, supporting evidence, và final Lambda-based RAG path theo hướng reviewer-facing.

## Công việc đã hoàn thành

- Tập trung workshop cuối cùng vào Lambda-based RAG path với E5 query embeddings, Qdrant Cloud retrieval, Gemini answer generation, và AWS observability.
- Thêm và rà soát screenshots để tránh lộ thông tin nhạy cảm.
- Tạo Hugo workshop repo dựa trên template và chuyển nội dung kỹ thuật vào cấu trúc workshop.
- Viết lại phần Workshop, Proposal, và Worklog cho dự án cuối cùng.
- Chuẩn bị các phần báo cáo còn lại để hoàn thiện submission.
- Rà soát supporting evidence assets và lên flow demo video ngắn cho final submission.

## Tiến độ theo ngày

| Ngày | Công việc đã làm | Ghi chú / bằng chứng |
| --- | --- | --- |
| 13/07/2026 | Tham gia office visit for studying, chốt main RAG architecture, vẽ/chỉnh lại architecture diagram, và rà soát screenshots để redact. | Final path tập trung vào Chainlit, Lambda Function URL, containerized query embedding, Qdrant Cloud, Gemini, DynamoDB, CloudWatch, EventBridge Scheduler, và SNS. |
| 14/07/2026 | Transform Hugo template repo, viết lại Workshop và Proposal, mở rộng Worklog, và kiểm tra Hugo build. | Tạo cấu trúc reviewer-facing cho final submission thay vì chỉ để project ở dạng implementation notes. |
| 15/07/2026 | Polish worklog references, office/event evidence, final-week reflection, screenshot evidence, và wording cho reviewer. | Giữ final report khớp với documented evidence, validation steps, cleanup guidance, và Hugo build checks. |
| 16/07/2026 | Rà soát supporting evidence files, làm rõ demo-video plan, và cập nhật worklog end date cho nhất quán cuối kỳ. | Supporting evidence gồm graduation-project repo screenshot và CLEF working note; demo plan tập trung vào screen recording và tránh lộ secrets. |

## Reflection và bài học rút ra

Kiến trúc cuối cùng đã rõ dưới dạng một RAG application nhỏ: Chainlit UI local gọi Lambda Function URL, Lambda tạo query embedding, truy xuất recipe context liên quan từ Qdrant Cloud, rồi dùng Gemini để sinh câu trả lời có căn cứ. Các AWS services hỗ trợ query logs, structured logs, scheduled health checks, alarms, và notification evidence. Tuần này chuyển implementation thành cấu trúc workshop reviewer-facing, với sự chú ý rõ hơn đến validation, evidence, cost awareness, redaction, demo readiness, và cleanup.

## Tổng kết quá trình thực tập

| Giai đoạn | Thời gian | Kết quả chính |
| --- | --- | --- |
| Xây nền tảng | Đầu tháng 3 - đầu tháng 4 | Xây nền tảng về Data Engineering, AWS fundamentals, recommender systems, RAG, và retrieval concepts. |
| Khám phá domain và retrieval | Tháng 4 - tháng 5 | Làm food-recipe graduation project và CLEF CheckThat!, từ đó củng cố domain, NLP, retrieval, và embeddings. |
| Bài học về data processing | Tháng 5 - giữa tháng 6 | Dùng Gemini và Qwen-based workflows để xử lý dữ liệu công thức, và học rằng source data quality cùng task design ảnh hưởng mạnh đến retrieval quality. |
| Triển khai FCJ | Cuối tháng 6 - giữa tháng 7 | Quay lại FCJ labs, xây project path, và gom workshop cuối cùng quanh Lambda, text embeddings, Qdrant Cloud, Gemini, và observability. |
| Hoàn thiện workshop | 13/07/2026 - 16/07/2026 | Chuyển implementation thành Hugo workshop reviewer-facing với proposal, worklog, validation evidence, supporting artifacts, demo planning, và cleanup guidance. |

## Reflection cuối kỳ

Quá trình thực tập không đi theo một đường thẳng. Tôi bắt đầu với ít kinh nghiệm thực tế về AWS, deployment, system design, và production-oriented ML systems, nên giai đoạn đầu cần học rộng trước khi hướng cuối cùng rõ ràng. Đồ án tốt nghiệp và CLEF đôi khi làm giảm thời gian triển khai FCJ trực tiếp, nhưng chúng cũng tạo nền tảng kỹ thuật quan trọng nhất cho workshop cuối cùng: dữ liệu công thức, retrieval, embeddings, và evaluation.

Bài học chính là một AI project không chỉ phụ thuộc vào việc chọn model. Kết quả cuối cùng phụ thuộc vào data quality, retrieval design, deployment constraints, observability, cost control, và documentation rõ ràng. Đến cuối kỳ, project đã trở thành một workshop AWS thực tế mà reviewer có thể theo dõi, kiểm tra, và cleanup an toàn.
