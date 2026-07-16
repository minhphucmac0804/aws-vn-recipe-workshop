---
title: "Tự đánh giá"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

Trong kỳ thực tập này, tôi dần chuyển một ý tưởng gợi ý món ăn Việt Nam thành một AWS workshop hoàn chỉnh, tập trung vào luồng E5 Lambda RAG ở phiên bản cuối.

## Tóm tắt kỳ thực tập

Từ tháng 3/2026 đến giữa tháng 7/2026, công việc thực tập của tôi dần chuyển từ giai đoạn khám phá rộng sang một project AWS workshop có phạm vi rõ ràng hơn. Tôi bắt đầu với nền tảng mạnh hơn về toán, thống kê, và các mô hình machine learning cơ bản so với cloud engineering, application deployment, hoặc production-oriented AI systems, nên giai đoạn đầu cần học thêm nhiều về AWS fundamentals, retrieval-based AI systems, và data workflows. Theo thời gian, project hội tụ thành một workshop Vietnamese Recipe Assistant hướng reviewer, xoay quanh kiến trúc cuối cùng đã hoàn thiện. Kiến trúc đó dùng giao diện local, AWS Lambda backend, vector search với Qdrant Cloud, answer generation bằng Gemini, và các dịch vụ observability hỗ trợ trên AWS.

## Tiêu chí tự đánh giá

Dùng bảng theo phong cách template, nhưng điều chỉnh các dấu đánh giá theo tự nhận xét thực tế của tôi.

| No. | Tiêu chí | Mô tả | Good | Fair | Average |
| --- | --- | --- | --- | --- | --- |
| 1 | **Professional knowledge & skills** | Hiểu biết về AWS, luồng RAG, chất lượng triển khai, và cách dùng công cụ thực tế | ` ` | ` ` | `✅` |
| 2 | **Ability to learn** | Khả năng học dịch vụ mới, khái niệm mới, và cách triển khai trong quá trình thực tập | ` ` | `✅` | ` ` |
| 4 | **Sense of responsibility** | Làm việc cẩn thận và theo đuổi đến cùng đầu ra workshop cuối | ` ` | `✅` | ` ` |
| 5 | **Discipline** | Quản lý thời gian, duy trì tiến độ, và bám dự án trong một khoảng thời gian dài | ` ` | ` ` | `✅` |
| 6 | **Progressive mindset** | Tiếp nhận phản hồi, sửa hướng đi, và cải thiện cấu trúc dự án theo thời gian | ` ` | `✅` | ` ` |
| 8 | **Problem-solving skills** | Nhận diện blocker, thử phương án khác nhau, và hội tụ vào giải pháp làm được | ` ` | `✅` | ` ` |
| 9 | **Professional conduct** | Làm dự án nghiêm túc và tài liệu hóa nó theo hướng reviewer-friendly | `✅` | ` ` | ` ` |
| 10 | **Contribution to the final project** | Biến phần khám phá và thử nghiệm thành một workshop hoàn chỉnh, có thể trình bày được | `✅` | ` ` | ` ` |
| 11 | **Overall** | Đánh giá chung về giai đoạn thực tập và chất lượng sản phẩm cuối | ` ` | `✅` | ` ` |

## Phản ánh chính

Hành trình thực tập không đi theo một đường thẳng. Ở giai đoạn đầu, tôi vẫn đang tìm một hướng project đủ rõ để có thể trở thành AWS workshop, đồng thời học Data Engineering, recommender systems, RAG, và các khái niệm retrieval. Cùng lúc đó, đồ án tốt nghiệp và công việc CLEF CheckThat! chiếm một phần thời gian đáng kể, nhưng cuối cùng lại tạo ra nền tảng kỹ thuật quan trọng nhất cho workshop: bối cảnh recipe domain, tư duy retrieval, embeddings, nhận thức về chất lượng dataset, và thói quen evaluation. Hướng đi cuối cùng chỉ trở nên rõ hơn ở giai đoạn sau, khi tôi quay lại phần triển khai FCJ, kết nối các AWS services cụ thể hơn, và thu hẹp phạm vi reviewer-facing quanh luồng E5 Lambda RAG.

## Những gì tôi cải thiện nhiều nhất

Khi bắt đầu kỳ thực tập, nền tảng của tôi mạnh hơn ở toán, thống kê, và các mô hình machine learning cơ bản so với cloud engineering, software deployment, system design, hoặc production-ready AI systems. Tôi có ít kinh nghiệm thực tế với AWS services, container deployment, Git/GitHub workflows, API-based application design, và cloud monitoring.

Vì vậy, phần lớn hành trình thực tập mang tính khám phá. Tôi học Data Engineering, AWS fundamentals, Retrieval-Augmented Generation (RAG), vector databases, text embeddings, practical Large Language Model (LLM) workflows, và một số chủ đề AI liên quan trong khi cố gắng tìm một hướng project có thể trở thành workshop AWS rõ ràng. Một số chủ đề được học vì ban đầu tôi nghĩ chúng sẽ hữu ích, nhưng về sau tôi nhận ra chúng không liên quan trực tiếp đến kiến trúc AWS cuối cùng. Dù vậy, quá trình khám phá đó giúp tôi thu hẹp project thành một workshop recipe assistant thực tế.

Hướng cuối cùng kết hợp food-recipe domain từ đồ án tốt nghiệp với các kỹ thuật retrieval và language model mà tôi đã học trong kỳ thực tập. Thay vì xây một hệ thống production lớn, tôi tập trung vào một kiến trúc nhỏ nhưng hoàn chỉnh: giao diện chat local gửi câu hỏi món ăn đến AWS Lambda, Lambda truy xuất recipe context liên quan từ Qdrant Cloud bằng text embeddings, Gemini tạo câu trả lời grounded, và các dịch vụ AWS ghi lại logs, health checks, và alerts.

## Những điểm cần cải thiện

- Tôi cần xác định phạm vi cuối của dự án sớm hơn thay vì để giai đoạn khám phá kéo dài quá lâu. Điều này một phần phản ánh việc tôi còn thiếu kỹ năng, kiến thức, và quỹ thời gian ở giai đoạn đầu của kỳ thực tập.
- Tôi cần quản lý tốt hơn việc tập trung, lập kế hoạch, và phân bổ thời gian khi nhiều track lớn diễn ra song song, đặc biệt khi công việc học tập và thực tập chồng lên nhau.
- Tôi cần đánh giá các lựa chọn kỹ thuật sớm hơn bằng các proof-of-concept nhỏ trước khi dành quá nhiều thời gian cho một hướng, đặc biệt với data processing, retrieval quality, và model selection.
- Tôi nên chủ động trao đổi với mentor hoặc support team sớm hơn khi có câu hỏi chưa rõ về kỹ thuật hoặc định hướng project. Làm điều này sớm hơn có thể giúp tôi unblock nhanh hơn, hoàn thành project sớm hơn, và có thêm thời gian để cải thiện quy mô cũng như độ polish của project.

## Ghi chú cuối

Nhìn chung, tôi xem kỳ thực tập này là một giai đoạn phát triển mạnh cả về kỹ thuật lẫn cá nhân. Kỳ thực tập kéo dài hơn dự kiến ban đầu, và hướng cuối cùng trở nên rõ tương đối muộn, nhưng đến cuối cùng tôi đã chuyển được công việc thành một AWS workshop thực tế với kiến trúc rõ ràng, luồng kiểm thử hoạt động được, và observability có bằng chứng. Quan trọng hơn, tôi hiểu rõ hơn nhiều cách cloud engineering và retrieval systems kết hợp với nhau trong một ứng dụng machine learning thực tế.
