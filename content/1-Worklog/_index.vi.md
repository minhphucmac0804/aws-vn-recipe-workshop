---
title: "Nhật ký công việc"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

Phần này tóm tắt quá trình thực tập AWS FCJ của tôi từ `05/03/2026` đến `16/07/2026`. Tôi đăng ký chương trình vào đầu tháng 3, nhưng worklog chính bắt đầu từ tuần làm việc đầy đủ đầu tiên để phù hợp hơn với format theo tuần của template.

## Nền tảng ban đầu và quá trình học

Khi bắt đầu thực tập, nền tảng của tôi mạnh hơn ở toán, thống kê, và các mô hình machine learning cơ bản hơn là cloud engineering, software deployment, system design, hoặc production-oriented ML systems. Tôi có ít kinh nghiệm thực tế với AWS services, container deployment, Git/GitHub workflows, API-based application design, và cloud observability.

Vì vậy, phần lớn hành trình thực tập có tính khám phá. Tôi học Data Engineering, AWS fundamentals, RAG, vector databases, embeddings, practical LLM workflows, và một số chủ đề ML lân cận trong quá trình tìm hướng project đủ rõ để phát triển thành AWS workshop. Một số chủ đề được học vì ban đầu tôi nghĩ chúng hữu ích, nhưng sau đó tôi nhận ra chúng không trực tiếp liên quan đến kiến trúc AWS cuối cùng. Dù vậy, quá trình khám phá này giúp thu hẹp project thành một workshop recipe-assistant thực tế.

Đến cuối kỳ thực tập, các hướng học này hội tụ thành một workshop AWS thực tế cho Vietnamese recipe assistant, dùng local UI, Lambda Function URL, containerized E5 query embedding, Qdrant Cloud retrieval, Gemini answer generation, và các dịch vụ observability trên AWS.

## Các phần học trước đó đóng góp như thế nào cho workshop cuối cùng

| Learning / Work Area | Đóng góp cho final project | Reference / Evidence |
| --- | --- | --- |
| Data Engineering learning | Xây nền tảng theo hướng cloud để hiểu data pipelines, data quality, storage choices, và AWS-based data workflows. | [DeepLearning.AI Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/data-engineering?utm_medium=sem&utm_source=gg&utm_campaign=b2c_apac_x_multi_ftcof_career-academy_cx_dr_bau_gg_pmax_gc_s2_all_m_hyb_24-08_desktop&campaignid=21573875733&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&creativeid=&assetgroupid=6511386418&targetid=&extensionid=&placement=&gad_source=1&gad_campaignid=21584159401&gclid=Cj0KCQjw39zSBhDhARIsANammDtjU2seBrKpT2enc2Lh624NXanWILTkwLGc2gvZ95AeI_rdLDS5TwYaAoKbEALw_wcB) |
| AWS/FCJ theory and labs | Giúp tôi hiểu các AWS services dùng trong workshop cuối cùng, đặc biệt là Lambda, ECR, DynamoDB, CloudWatch, EventBridge, SNS, và IAM. | [FCJ theory videos](https://www.youtube.com/watch?v=AQlsd0nWdZk&list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i) và [AWS Study Group labs](https://cloudjourney.awsstudygroup.com/) |
| Graduation food-recipe project | Cung cấp domain, dataset context, và motivation để xây Vietnamese recipe assistant. | [Thesis reference](/aws-vn-recipe-workshop/files/evidence/thesis-reference.pdf), [private repo screenshot](/aws-vn-recipe-workshop/images/evidence/graduation-project-repo.png), và [Bằng chứng hỗ trợ](../8-SupportingEvidence/) |
| Recommender-system exploration | Giúp định hình bài toán food recommendation ban đầu, dù phần này không nằm trong kiến trúc AWS cuối cùng. | [A New Dataset and Empirical Evaluation for Vietnamese Food Recommendation System](https://aclanthology.org/2024.paclic-1.4.pdf) và project discussions liên quan |
| Retrieval-Augmented Generation course | Giúp tôi hiểu cách retrieval, context construction, và answer generation kết hợp trong một RAG application. | [Retrieval Augmented Generation (RAG)](https://www.coursera.org/learn/retrieval-augmented-generation-rag) |
| Claude API / agent course | Mở rộng hiểu biết của tôi về API-based LLM application design và tool-using assistant workflows. | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) |
| CLEF CheckThat! work | Củng cố hiểu biết về NLP, scientific source retrieval, embeddings, re-ranking, và evaluation. Team của tôi, BoPC, xếp top 15 ở phần CheckThat! Task 1 liên quan, và trải nghiệm này giúp tôi tiếp xúc với các ý tưởng retrieval/embedding sau này có ích cho hướng RAG của recipe assistant. | [CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/) |
| Qdrant and RAG learning | Trực tiếp liên quan đến kiến trúc retrieval cuối cùng và quyết định dùng vector search để truy xuất recipe context. | [Qdrant documentation](https://qdrant.tech/documentation/) và RAG notes |

## Office Visits và Events

Phần này tóm tắt các office visits for studying và các sự kiện AWS/FCJ đã tham gia trong thời gian thực tập. Tôi đưa phần này vào như supporting context cho việc tham gia trực tiếp và hoạt động học tập, còn các trang theo tuần vẫn tập trung vào tiến độ kỹ thuật.

| Ngày | Loại | Ghi chú |
| --- | --- | --- |
| 05/03/2026 | Office visit for studying | Đăng ký giai đoạn thực tập và bắt đầu chuẩn bị tại văn phòng. |
| 10/03/2026 | Office visit for studying | Lần đầu hình thành nhịp làm việc trực tiếp cho FCJ. |
| 20/03/2026 | Office visit for studying | Review paper về Vietnamese food recommendation và làm rõ project framing ban đầu. |
| 21/03/2026 | AWS/FCJ event | FCJ Community Day: platform engineering, DevOps, cloud architecture, và AI/LLM operations. |
| 25/03/2026 | Office visit for studying | Học retrieval/ranking concepts và tạo slide tóm tắt cho team. |
| 31/03/2026 | Office visit for studying | Học AI/CLEF-related concepts và tinh chỉnh project direction. |
| 15/05/2026 | Office visit for studying | Lập kế hoạch dataset-processing attributes và thử hướng small-model fine-tuning. |
| 21/05/2026 | Office visit for studying | Review recipe attributes do Gemini sinh ra và xử lý thêm recipe records. |
| 23/05/2026 | AWS/FCJ event | FCJ Community Day: AI engineering in production, context engineering, security, compliance, và cloud cost control. |
| 06/06/2026 | AWS/FCJ event | Saturday Meet-up: Docker, GraphRAG, operations, troubleshooting, và định hướng nghề nghiệp trong AI/cloud. |
| 13/07/2026 | Office visit for studying | Chốt workshop cuối cùng, vẽ architecture diagram, rà soát redaction, và soạn reviewer-facing content. |

## Timeline theo tuần

- **Tuần 1 (09/03/2026 - 15/03/2026)**: [Xây dựng nền tảng ban đầu về AWS/Data Engineering và bắt đầu tìm hiểu recommender systems cũng như hướng food recommendation.](1.1-Week1/)
- **Tuần 2 (16/03/2026 - 22/03/2026)**: [Tiếp tục học recommender systems và tham gia sự kiện kickoff FCJ, từ đó định hướng dự án theo hướng thực tế hơn.](1.2-Week2/)
- **Tuần 3 (23/03/2026 - 29/03/2026)**: [Học RAG, Information Retrieval, ranking concepts, và ML production để hỗ trợ kiến trúc assistant sau này.](1.3-Week3/)
- **Tuần 4 (30/03/2026 - 05/04/2026)**: [Tiếp tục học Generative AI và Data Engineering, đồng thời chuẩn bị môi trường và hướng đề tài cho đồ án tốt nghiệp.](1.4-Week4/)
- **Tuần 5 (06/04/2026 - 12/04/2026)**: [Thực hiện các task đầu tiên của đồ án tốt nghiệp, học Qdrant, và cải thiện workflow phát triển với VS Code/GitHub.](1.5-Week5/)
- **Tuần 6 (13/04/2026 - 19/04/2026)**: [Cân bằng công việc CLEF CheckThat! với việc học Qdrant và thử nghiệm embedding models.](1.6-Week6/)
- **Tuần 7 (20/04/2026 - 26/04/2026)**: [Hoàn thành phần học RAG và đọc các paper CLEF về scientific source retrieval để hiểu retrieval pipeline thực tế.](1.7-Week7/)
- **Tuần 8 (27/04/2026 - 03/05/2026)**: [Chuyển từ đọc paper CLEF sang fine-tuning multilingual E5 và re-ranker experiments cho scientific source retrieval.](1.8-Week8/)
- **Tuần 9 (04/05/2026 - 10/05/2026)**: [Kết thúc giai đoạn fine-tuning CLEF tập trung, sau đó quay lại Data Engineering learning và vấn đề retrieval quality của food-recipe project.](1.9-Week9/)
- **Tuần 10 (11/05/2026 - 17/05/2026)**: [Điều tra chất lượng retrieval thấp trong food-recipe project và thiết kế kế hoạch xử lý dataset bằng LLM.](1.10-Week10/)
- **Tuần 11 (18/05/2026 - 24/05/2026)**: [Xử lý recipe dataset bằng Gemini API và đánh giá chất lượng dataset sau xử lý thông qua EDA.](1.11-Week11/)
- **Tuần 12 (25/05/2026 - 31/05/2026)**: [Viết working note cho CLEF CheckThat! task và tổng hợp lại các bài học về retrieval/NLP.](1.12-Week12/)
- **Tuần 13 (01/06/2026 - 07/06/2026)**: [Quay lại xử lý dữ liệu food-recipe bằng cách kiểm tra các attributes version 1 do Gemini tạo và lập kế hoạch cải thiện dataset version 2.](1.13-Week13/)
- **Tuần 14 (08/06/2026 - 14/06/2026)**: [Triển khai thử nghiệm data-processing version 2 bằng Qwen với GPU của Modal, sau đó đánh giá vì sao output không đạt mục tiêu chất lượng kỳ vọng.](1.14-Week14/)
- **Tuần 15 (15/06/2026 - 21/06/2026)**: [Quay lại tập trung vào lý thuyết FCJ, đồng thời tìm hiểu agent và local model topics.](1.15-Week15/)
- **Tuần 16 (22/06/2026 - 28/06/2026)**: [Cân bằng việc học lý thuyết FCJ, thử nghiệm local model, và viết báo cáo đồ án tốt nghiệp.](1.16-Week16/)
- **Tuần 17 (29/06/2026 - 05/07/2026)**: [Bắt đầu làm lab FCJ mạnh hơn trong khi vẫn tiếp tục báo cáo đồ án tốt nghiệp.](1.17-Week17/)
- **Tuần 18 (06/07/2026 - 12/07/2026)**: [Tiếp tục triển khai project FCJ, khôi phục AWS access, và thu hẹp project từ baseline exploration sang final Lambda-based RAG workshop path.](1.18-Week18/)
- **Tuần 19 (13/07/2026 - 16/07/2026)**: [Hoàn thiện repo workshop, evidence package, và final Lambda-based RAG path theo hướng reviewer-facing.](1.19-Week19/)
