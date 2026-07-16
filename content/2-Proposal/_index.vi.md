---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# AWS Vietnamese Recipe Assistant
## Workshop RAG chi phí thấp trên AWS cho tìm kiếm công thức món Việt và câu trả lời có grounding

### 1. Tóm tắt điều hành
Dự án này đề xuất một trợ lý món ăn Việt Nam chạy trên AWS, nhằm minh họa một luồng retrieval-augmented generation hoàn chỉnh mà không cần một hệ thống cloud quá lớn hoặc quá đắt. Luồng cuối cùng sử dụng Chainlit local, AWS Lambda Function URL, Lambda container có multilingual E5 embeddings, Qdrant Cloud cho vector search, và Gemini cho grounded answer generation.

Dự án được giới hạn có chủ đích như một workshop deliverable tập trung. Nó trình bày một kiến trúc end-to-end đủ rõ để reviewer theo dõi, đủ thực tế để kiểm tra bằng screenshots, logs, và evaluation results, đồng thời vẫn phù hợp với phạm vi của một dự án thực tập. Trong tài khoản AWS được dùng để phát triển, chi phí đã kiểm tra là `$0`, kể cả khi tính phần credits trong giao diện billing.

### 2. Bằng chứng bối cảnh hỗ trợ
Use case cuối cùng của workshop dựa trên đồ án tốt nghiệp về food-recipe. Vì repository gốc của project vẫn private, workshop public đưa vào supporting evidence thay cho toàn bộ source repository private: [thesis reference đã redact](/files/evidence/thesis-reference.pdf), [private repository screenshot](/images/evidence/graduation-project-repo.png), và trang [Bằng chứng hỗ trợ](../8-SupportingEvidence/).

Các file này chỉ đóng vai trò background evidence. Chúng giải thích domain và learning path của project, còn phần implementation của workshop vẫn tập trung vào final Lambda-based RAG architecture.

### 3. Bài toán
Nội dung công thức món ăn Việt Nam thường bị phân tán giữa notebooks, datasets, scripts thử nghiệm, và local experiments. Người dùng có thể muốn hỏi `Gợi ý món ăn với thịt gà và rau củ` và nhận câu trả lời dựa trên dữ liệu công thức, thay vì chỉ là phản hồi chung chung từ mô hình.

Dự án giải quyết ba vấn đề thực tế:

- chưa có một kiến trúc AWS đơn giản, dễ review, để minh họa recipe retrieval end to end cho tiếng Việt
- local-only experiments hữu ích cho việc học nhưng khó trình bày thành một workshop cloud rõ ràng
- một kiến trúc generative AI hoàn toàn AWS-native, ở quy mô rộng hơn, có thể đưa vào nhiều dịch vụ, độ phức tạp vận hành, và yêu cầu tài khoản vượt quá mức phù hợp cho submission thực tập hiện tại

### 4. Giải pháp đề xuất
Giải pháp được đề xuất là một workshop AWS tập trung vào final Lambda RAG backend. Về mặt thực tế, kế hoạch là tái tạo giá trị cốt lõi của local project gốc dưới dạng một hệ thống cloud dễ review hơn, thay vì sao chép toàn bộ các nhánh hoặc thử nghiệm trước đó theo kiểu một-một.


```text
Local Chainlit UI -> Lambda Function URL -> Lambda container with multilingual E5 embeddings -> Qdrant Cloud -> Gemini grounded answer -> Chainlit response
```

Observability được giữ gọn và thực tế:

- Lambda ghi query logs vào DynamoDB
- Lambda ghi structured logs vào CloudWatch
- EventBridge Scheduler gọi health-check path theo lịch
- CloudWatch metric filter và alarm phát hiện controlled fallback events
- SNS gửi email notification để reviewer kiểm tra

Workshop cuối cùng được hình thành qua các bước nhỏ hơn: baseline serverless prototype, local Qdrant retrieval validation, rồi hosted Qdrant Cloud và Lambda container backend. Local Qdrant branch giải thích cách retrieval được kiểm tra trước khi cloud backend hoàn thiện. Fallback branch cho thấy hệ thống xử lý thế nào khi hosted retrieval lỗi. Hai nhánh này là bối cảnh hỗ trợ, không thay thế final cloud path.

### 5. Vì sao chọn kiến trúc này
Kiến trúc này cân bằng giữa chi phí, độ rõ ràng, giới hạn tài khoản, và giá trị kỹ thuật.

- `AWS Lambda` cung cấp compute layer rõ ràng mà không cần server chạy liên tục.
- `Lambda Function URL` giữ entry point đơn giản và tránh API Gateway cho workshop này.
- `multilingual E5 embeddings` phù hợp cho retrieval của công thức món Việt.
- `Qdrant Cloud` giúp vector search thực tế hơn mà không cần vector stack AWS nặng hơn.
- `Gemini` tạo câu trả lời có grounding từ retrieved context.
- `DynamoDB`, `CloudWatch`, `EventBridge Scheduler`, và `SNS` tạo bằng chứng vận hành rõ ràng.

#### Lựa chọn dịch vụ và phương án thay thế

| Lựa chọn trong workshop | Phương án thay thế | Lý do chọn hướng hiện tại |
| --- | --- | --- |
| `AWS Lambda` cho compute | `Amazon EC2` | Lambda phù hợp với workshop vì backend chỉ cần chạy khi có request, health check, hoặc validation call. AWS mô tả Lambda là serverless compute với cơ chế trả phí theo mức sử dụng, còn EC2 On-Demand tính phí cho compute capacity của instance theo giờ hoặc theo giây khi instance chạy. Với một workshop internship nhỏ, Lambda giúp giảm nhu cầu vận hành server chạy liên tục và giúp kiểm soát chi phí dễ hơn. |
| `Lambda Function URL` cho HTTPS entry point | `Amazon API Gateway` | Function URL đã đủ để tạo HTTP endpoint dễ kiểm tra từ Chainlit local đến Lambda. API Gateway vẫn là hướng mở rộng tốt nếu dự án cần routing, authorization, throttling, hoặc public production API đầy đủ hơn. |
| `Qdrant Cloud` cho vector retrieval | `OpenSearch Serverless` | Qdrant đã được kiểm tra ở nhánh local retrieval rồi chuyển sang hosted cloud collection với ít độ phức tạp hơn. OpenSearch Serverless vẫn có thể là hướng AWS-native trong tương lai, nhưng chưa cần thiết để chứng minh workflow RAG cuối cùng. |
| `Gemini` cho answer generation | `Amazon Bedrock` | Gemini sẵn sàng dùng trong quá trình phát triển và hoạt động với retrieval flow hiện tại. Bedrock là lựa chọn generative AI AWS-native hơn, nhưng giới hạn activation/access của tài khoản làm cho Bedrock kém thực tế hơn trong timeline hoàn thiện workshop. |
| Giao diện `Chainlit` local | Frontend cloud-hosted với `CloudFront`, `Cognito`, hoặc dịch vụ tương tự | Workshop ưu tiên backend RAG path, validation evidence, và observability trước. Frontend hosted có thể được bổ sung sau khi Lambda retrieval path đã ổn định. |
| `DynamoDB`, `CloudWatch`, `EventBridge Scheduler`, và `SNS` cho observability | Logging, analytics, hoặc monitoring stack lớn hơn | Các dịch vụ này đủ để thể hiện query logs, structured Lambda logs, scheduled health checks, fallback detection, và email notification cho reviewer mà không thêm dịch vụ không cần thiết. |

Quy mô dự án cũng bị ảnh hưởng bởi trạng thái pending activation của tài khoản AWS dùng trong quá trình phát triển. Vì vậy workshop cố ý tránh các dịch vụ làm kiến trúc lớn hơn hoặc khó xác thực hơn trong điều kiện tài khoản còn hạn chế. Điều này đặc biệt ảnh hưởng đến khả năng dùng một số dịch vụ vốn có thể phù hợp hơn với hướng generative AI trên cloud, chẳng hạn như Amazon Bedrock.

### 6. Mục tiêu
Các mục tiêu của dự án là:

- xây dựng một trợ lý món ăn Việt có grounded answers
- trình bày một workshop path cuối cùng mà reviewer có thể theo dõi từ zero context
- giữ chi phí AWS đã kiểm tra ở mức `$0`
- cung cấp bằng chứng rõ ràng cho RAG execution thành công và fallback observability
- có hướng dẫn cleanup để xóa toàn bộ tài nguyên sau khi review

### 7. Phạm vi
### Trong phạm vi
- giao diện Chainlit local
- backend entry point bằng Lambda Function URL
- Lambda container với multilingual E5 query embeddings
- Qdrant Cloud collection cho recipe retrieval
- Gemini grounded answer generation
- DynamoDB query logs
- CloudWatch structured logs
- EventBridge Scheduler health check
- CloudWatch alarm và SNS email notification
- bộ evaluation nhỏ với retrieval metrics đơn giản
- ghi chú về local Qdrant và fallback branch như bối cảnh lịch sử dự án

### Ngoài phạm vi
- public production hosting cho Chainlit
- CloudFront/static web deployment cho workshop hiện tại
- large-scale ingestion pipelines
- ECS/Fargate hosting
- chuyển sang OpenSearch Serverless
- automated evaluation nâng cao như một yêu cầu bắt buộc

### 8. Kiến trúc giải pháp
Kiến trúc reviewer-facing cuối cùng được thể hiện bên dưới.

![AWS Vietnamese Recipe Assistant Architecture](/images/5-Workshop/aws-workshop-architecture-final.png)

### Dịch vụ AWS sử dụng
- `AWS Lambda`: compute chính và điều phối backend
- `Amazon ECR`: lưu container image cho Lambda
- `Lambda Function URL`: HTTPS endpoint cho ứng dụng local
- `Amazon DynamoDB`: lưu query logs
- `Amazon CloudWatch Logs`: lưu structured application logs
- `Amazon EventBridge Scheduler`: trigger health-check theo lịch
- `Amazon CloudWatch Alarm`: cảnh báo khi có controlled fallback events
- `Amazon SNS`: gửi email notification làm bằng chứng

### Thành phần bên ngoài AWS
- `Chainlit`: giao diện người dùng local
- `Qdrant Cloud`: vector database
- `Gemini`: model API cho answer generation

### 9. Kế hoạch triển khai kỹ thuật
Việc triển khai được tổ chức theo workshop path cuối cùng:

1. chuẩn bị dataset món ăn Việt và vector collection
2. kiểm tra retrieval bằng local Qdrant như development baseline
3. nạp recipe collection lên Qdrant Cloud
4. build và push Lambda container image lên ECR
5. deploy Lambda function và cấu hình environment variables
6. mở Lambda Function URL và kết nối Chainlit local
7. kiểm tra hành vi RAG thành công
8. thêm observability, fallback detection, và evaluation evidence
9. cleanup toàn bộ tài nguyên sau khi test

### 10. Kế hoạch đánh giá
Evaluation được giữ đơn giản và dễ review.

Smoke tests xác nhận hệ thống chạy end to end:
- Chainlit gửi query thành công
- Lambda trả response với `mode_used=rag`
- DynamoDB và CloudWatch có bằng chứng

Sau đó dùng query set nhỏ, thống nhất cho evaluation thật:
- câu hỏi gợi ý món ăn bằng tiếng Việt
- kiểm tra top-k retrieval
- metrics đơn giản như `Precision@3` và `Precision@5`
- ghi chú relevance ngắn cho từng query

RAGAS là optional, không bắt buộc cho workshop.

### 11. Ngân sách và kiểm soát chi phí
Chi phí đã kiểm tra trong tài khoản AWS dùng cho dự án là `$0`, kể cả khi tính phần credits trong billing view.

Chi phí được giữ ở `$0` nhờ setup nhỏ và ngắn hạn:
- một Lambda function
- một ECR repository
- một DynamoDB table
- mức sử dụng CloudWatch, Scheduler, SNS, và alarm rất nhỏ
- không dùng NAT Gateway, EC2, RDS, API Gateway, CloudFront, hoặc hạ tầng chạy liên tục
- cleanup sau validation

Người làm lại workshop vẫn nên kiểm tra billing của tài khoản riêng vì Free Tier, credits, region, và thời gian giữ tài nguyên có thể khác nhau.

### 12. Resource Management
Tags được khuyến nghị để dễ cleanup và review, dù không phải nội dung kỹ thuật chính.

| Key | Value |
| --- | --- |
| `Project` | `aws-vn-recipe-workshop` |
| `Purpose` | `fcj-workshop` |
| `Owner` | `<your-name>` |
| `Environment` | `workshop` |

### 13. Giới hạn và hướng cải thiện
[AWS Study Group Lab 117](https://000117.awsstudygroup.com/2-static-s3/2.2-access-data/), `Build a Complete serverless Chat Website`, là hướng tham khảo tương lai. Ý tưởng liên quan là static chat application dùng S3 static hosting và JavaScript access to static data, trong kiến trúc serverless rộng hơn gồm API Gateway, Lambda, DynamoDB, Cognito, và CloudFront.

Hướng này chưa được triển khai trong workshop hiện tại. CloudFront và public web architecture được để lại cho tương lai vì project hiện tại ưu tiên final Lambda RAG backend, kết quả chi phí đo được là `$0`, và giới hạn thực tế từ trạng thái pending activation của tài khoản AWS. Điều đó cũng có nghĩa là các hướng mở rộng sau này, như đưa nhiều phần frontend hơn lên cloud hoặc mở rộng sang API Gateway và Cognito, có thể sẽ chậm hơn hoặc bị ràng buộc hơn cho đến khi điều kiện tài khoản và quỹ thời gian thuận lợi hơn.

Một hướng scale-up hợp lý là giữ lại phần logic backend hiện tại, nhưng chuyển lớp giao diện người dùng sang một kiến trúc public cloud đầy đủ hơn, chẳng hạn kết hợp CloudFront, Cognito, và một API layer đứng trước assistant workflow. AWS đã mô tả việc hỗ trợ Lambda container images như một hướng có thể mang dependencies lớn hơn mà vẫn giữ khả năng scale nhanh và xử lý lưu lượng cao, nên hướng backend hiện tại vẫn có thể tiếp tục phù hợp với các workload tăng theo đợt ([AWS authors, 2023](https://arxiv.org/abs/2305.13162)). Nếu mức sử dụng tăng thêm nữa, các tác vụ indexing, evaluation, và maintenance theo kiểu bất đồng bộ có thể được tách khỏi user request path để phần assistant tương tác vẫn gọn và dễ vận hành hơn.

Các hướng cải thiện dài hạn có thể mở rộng project theo ba hướng, nhưng không phải yêu cầu bắt buộc cho workshop hiện tại:

- `Agent direction`: phát triển assistant từ một RAG question-answering app thành cooking helper có tool use, meal-planning steps, pantry constraints, shopping-list generation, hoặc multi-turn planning.
- `Data engineering direction`: làm recipe ingestion, cleaning, normalization, validation, và dataset rebuilds rõ ràng và lặp lại được hơn.
- `Data analytics and data science direction`: xây dashboard hoặc phân tích recipe data, query logs, retrieval quality, và evaluation results.

Một hướng nghiên cứu tiếp theo là cải thiện retrieval model. Workshop hiện tại dùng [`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base) như một multilingual embedding baseline thực tế, nhưng các bước sau có thể so sánh hoặc fine-tune embedding models cho Vietnamese recipe retrieval. Hướng này liên hệ tự nhiên với kinh nghiệm source retrieval và ranking từ [CLEF CheckThat! 2026 Task 1](https://checkthat.gitlab.io/clef2026/task1/), đồng thời có thể thử các Vietnamese-oriented models như [`dangvantuan/vietnamese-embedding`](https://huggingface.co/dangvantuan/vietnamese-embedding) hoặc [`VoVanPhuc/sup-SimCSE-VietNamese-phobert-base`](https://huggingface.co/VoVanPhuc/sup-SimCSE-VietNamese-phobert-base).

Submission hiện tại cố ý giữ phạm vi nhỏ hơn. Mục tiêu là chứng minh một AWS RAG backend hoạt động rõ ràng, giữ chi phí đo được ở `$0`, và tránh làm các ý tưởng DE/DA/agent trong tương lai trông như yêu cầu còn thiếu.

Demo video có thể được thêm sau như bằng chứng hỗ trợ nếu ngắn, đã redact, và tập trung vào main path. Cleanup screenshots cũng có thể thêm nếu thể hiện rõ tài nguyên đã được xóa, nhưng cleanup checklist vẫn là bằng chứng chính.

### 14. Rủi ro và hướng giảm thiểu
- `Cold start và model load latency`: giảm thiểu bằng phạm vi workshop nhỏ và validation với câu hỏi đơn giản.
- `Vector retrieval failure`: giảm thiểu bằng controlled fallback testing và bằng chứng CloudWatch/SNS.
- `Lộ secrets trong screenshots hoặc docs`: giảm thiểu bằng redaction nghiêm ngặt và không commit secrets.
- `Reader confusion từ lịch sử dự án`: giảm thiểu bằng cách giải thích progression baseline -> local Qdrant -> hosted Qdrant Cloud trước các bước backend cuối cùng.
- `Kiến trúc bị lệch khỏi nhánh cuối cùng`: giảm thiểu bằng việc tập trung vào final Lambda RAG backend, còn local Qdrant và fallback chỉ là bối cảnh hỗ trợ.

### 15. Kết quả kỳ vọng
Các kết quả kỳ vọng là:

- một workshop repo reviewer-facing rõ ràng trên AWS
- một trợ lý món ăn Việt hoạt động bằng RAG
- bằng chứng rõ ràng cho retrieval thành công, grounded answer, và observability
- một kiến trúc nhỏ gọn, dễ giải thích, dễ kiểm tra, và dễ cleanup
