---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Xây dựng giải pháp agentic AI tại Bluesight với Amazon Bedrock

> **Bài viết gốc**: [AWS Blog](https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-solution-at-bluesight-with-amazon-bedrock/)  
> **Tác giả**: Vijay Venkatesh, Chae Clark, Jiju R Sarojini, Sam You  
> **Ngày xuất bản**: 13/07/2026  
> **Nguồn**: AWS Machine Learning Blog  
> **Định dạng trong repo này**: Bản diễn giải kỹ thuật bằng tiếng Việt, không phải bản dịch nguyên văn toàn bộ.

## 📋 Tóm tắt

Bài viết mô tả cách Bluesight xây dựng một hệ thống agentic AI cho bài toán compliance trong lĩnh vực hospital pharmacy bằng Amazon Bedrock. Đây không phải là một use case chatbot phổ thông, mà là một quy trình ra quyết định có ràng buộc cao, nơi hệ thống phải tổng hợp nhiều tín hiệu vận hành để đánh giá một giao dịch mua thuốc có hợp lệ hay không. Ở quy mô hàng trăm bệnh viện, việc kiểm tra thủ công tiêu tốn rất nhiều thời gian, tạo áp lực lên đội ngũ compliance, và khó giữ được tính nhất quán khi khối lượng công việc tăng mạnh.

Điều đáng chú ý là Bluesight không dùng AI theo kiểu gắn thêm một lớp hội thoại lên sản phẩm sẵn có. Họ thiết kế một kiến trúc trong đó agent đóng vai trò điều phối, truy cập công cụ, thu thập ngữ cảnh, và hỗ trợ trình bày kết quả; còn phần kết luận compliance cốt lõi vẫn được giữ trong một deterministic scoring pipeline có thể kiểm tra và audit. Đây là một điểm rất đáng học vì nó cho thấy AI được đưa vào enterprise theo cách thận trọng: tận dụng khả năng reasoning của model nhưng không đánh đổi tính giải trình của business logic.

## 1. Bài toán thực tế: AI không thể đứng một mình

Trong các hệ thống enterprise, giá trị của AI không nằm ở việc model trả lời hay đến mức nào, mà nằm ở khả năng xử lý đúng một bài toán thật với dữ liệu thật và ràng buộc thật. Với Bluesight, agent không thể chỉ dựa vào kiến thức tĩnh của mô hình vì bài toán compliance phụ thuộc vào dữ liệu nội bộ và trạng thái vận hành thay đổi liên tục. Nếu không truy cập được hệ thống dữ liệu liên quan, AI chỉ có thể đưa ra câu trả lời nghe có vẻ hợp lý nhưng không đủ cơ sở để sử dụng trong môi trường production.

Điểm này rất quan trọng vì nó phản ánh giới hạn phổ biến của nhiều hệ thống LLM khi chuyển từ demo sang ứng dụng thật. Mô hình có thể suy luận tốt, nhưng nếu không có quyền truy cập đúng vào dữ liệu, không có lớp orchestration phù hợp, và không có cơ chế kiểm soát rõ ràng, chất lượng đầu ra sẽ không đủ để hỗ trợ quyết định nghiệp vụ. Trong môi trường healthcare hoặc compliance, sai sót như vậy không chỉ là lỗi kỹ thuật mà còn có thể tạo rủi ro vận hành và rủi ro pháp lý.

## 2. Cách Bluesight tiếp cận bài toán

Bluesight xử lý bài toán bằng cách phân tách hệ thống thành các lớp có trách nhiệm rõ ràng. Agent được dùng để điều hướng quy trình, gọi công cụ, gom dữ liệu, và tạo phần giải thích có tính ngôn ngữ tự nhiên. Tuy nhiên, phần quyết định cốt lõi không bị giao hoàn toàn cho model. Kết quả cuối cùng vẫn được neo vào một scoring pipeline có tính quyết định, nghĩa là hệ thống có thể lý giải vì sao một giao dịch bị gắn cờ, dựa trên những tín hiệu nào, và theo quy tắc nào.

Cách tiếp cận này cho thấy một tư duy rất thực dụng khi xây AI trong production. Thay vì cố ép model làm toàn bộ công việc, họ chỉ giao cho AI phần mà AI thực sự mạnh: reasoning đa bước, tổng hợp ngữ cảnh, và hỗ trợ giải thích. Còn phần nào cần tính nhất quán, khả năng kiểm chứng, hoặc dễ audit thì được giữ lại trong lớp logic rõ ràng hơn. Đây là một mô hình thiết kế rất phù hợp với những hệ thống có yêu cầu compliance hoặc governance cao.

## 3. Vai trò của Amazon Bedrock AgentCore

Bài viết cũng nhấn mạnh giá trị của Amazon Bedrock AgentCore trong việc biến một AI assistant thành một agent system có thể vận hành được. AgentCore Runtime cung cấp môi trường chạy serverless với session isolation, giúp kiểm soát cách agent thực thi trong từng phiên làm việc. AgentCore Gateway hỗ trợ đưa các API hiện có của doanh nghiệp vào dạng công cụ mà agent có thể gọi một cách chuẩn hóa hơn, đồng thời mở ra hướng tích hợp theo chuẩn MCP-compatible tools.

Điều quan trọng ở đây không phải là AgentCore làm cho model “thông minh hơn”, mà là nó cung cấp lớp hạ tầng để agent có thể hoạt động như một thành phần hệ thống thật. Khi kết hợp với VPC, encryption, authentication, observability, và audit trail, agent không còn là một demo đứng riêng lẻ mà trở thành một thành phần có thể được kiểm soát, theo dõi, và tích hợp vào hạ tầng enterprise hiện hữu.

## 4. Từ một use case sang một platform direction

Một bài học có giá trị khác là Bluesight không dừng lại ở một sản phẩm AI đơn lẻ. Họ bắt đầu từ ControlCheck, sau đó mở rộng thành Prism, một lớp AI thống nhất có thể phối hợp dữ liệu từ nhiều sản phẩm compliance khác nhau. Điều này thể hiện một tư duy platform rất rõ: nếu phần orchestration, tooling, và governance được thiết kế đúng, cùng một nền tảng có thể phục vụ nhiều use case thay vì phải xây từng assistant riêng lẻ từ đầu.

Đây là một điểm đặc biệt đáng chú ý đối với các dự án internship hoặc workshop. Nhiều dự án dừng ở mức một demo chạy được, nhưng rất ít dự án nghĩ đến việc lớp hạ tầng hoặc kiến trúc của mình có thể được tái sử dụng như thế nào. Bài viết này cho thấy một agentic system tốt không chỉ cần cho ra câu trả lời đúng, mà còn nên có khả năng trở thành một nền tảng cho các bài toán kế tiếp.

## 5. Vì sao cách tiếp cận này đáng chú ý

Điểm mạnh của bài viết không nằm ở việc giới thiệu một công nghệ mới duy nhất, mà nằm ở cách kết hợp AI với software architecture một cách tỉnh táo. Nó tránh được hai cực đoan thường gặp. Một là quá phụ thuộc vào model và để model gánh cả phần business logic. Hai là quá bảo thủ đến mức AI chỉ đóng vai trò minh họa. Bluesight chọn một điểm giữa hợp lý: để AI làm phần reasoning và điều phối, nhưng bao quanh nó bằng deterministic logic, observability, và security controls.

Đó cũng là lý do bài viết này có giá trị hơn một bài demo thông thường. Nó không chỉ kể câu chuyện “đã dùng AI vào sản phẩm”, mà còn chỉ ra những điều kiện để việc đó có thể xảy ra trong một môi trường regulated: dữ liệu phải truy cập được đúng cách, logic phải có thể kiểm chứng, và mọi hành vi quan trọng của agent phải để lại dấu vết đủ rõ để kiểm tra sau này.

## 6. Liên hệ với workshop của tôi

Bài viết này rất gần với workshop của tôi ở nhiều điểm. Thứ nhất là cùng dùng cloud-managed building blocks để ghép thành một hệ thống AI có cấu trúc. Thứ hai là cùng xem observability như một phần bắt buộc chứ không phải phần thêm vào sau. Thứ ba là cùng nhấn mạnh sự khác biệt giữa lớp reasoning của AI và lớp logic cần có khả năng kiểm chứng. Trong workshop của tôi, điều đó thể hiện qua Lambda logs, DynamoDB query logs, CloudWatch metric filters, fallback evidence, và reviewer-facing validation steps.

Ở mức rộng hơn, bài viết cũng giúp tôi nhìn rõ hơn giới hạn của một RAG demo đơn giản. Nếu sau này mở rộng workshop theo hướng agentic hơn, phần quan trọng sẽ không chỉ là thêm tool-calling, mà còn là thiết kế security boundary, kiểm soát quyền truy cập, và giữ được auditability của toàn bộ luồng xử lý.

## 📖 Glossary - Thuật ngữ

| English | Tiếng Việt | Định nghĩa |
| :-- | :-- | :-- |
| **Agentic AI** | AI tác tử / AI dạng agent | Hệ thống AI có khả năng lập kế hoạch, gọi công cụ, và thực hiện nhiều bước để hoàn thành một mục tiêu. |
| **Compliance** | Tuân thủ | Việc đảm bảo quy trình hoặc giao dịch đáp ứng các quy định nội bộ và bên ngoài. |
| **Deterministic Scoring** | Chấm điểm có tính quyết định | Cơ chế đánh giá dựa trên các quy tắc hoặc tín hiệu rõ ràng, cho cùng kết quả khi đầu vào không đổi. |
| **Orchestration** | Điều phối | Quá trình phối hợp nhiều bước xử lý, công cụ, hoặc dịch vụ để hoàn thành một tác vụ. |
| **AgentCore Runtime** | AgentCore Runtime | Thành phần runtime hỗ trợ chạy agent trong môi trường serverless có kiểm soát. |
| **AgentCore Gateway** | AgentCore Gateway | Thành phần giúp đưa API hiện có thành công cụ mà agent có thể sử dụng. |
| **MCP-compatible tools** | Công cụ tương thích MCP | Các công cụ hoặc API có thể tích hợp theo hướng chuẩn hóa tương tự Model Context Protocol. |
| **Session Isolation** | Cô lập phiên làm việc | Cơ chế tách biệt mỗi phiên thực thi để tăng độ an toàn và khả năng kiểm soát. |
| **Observability** | Khả năng quan sát hệ thống | Khả năng theo dõi, phân tích, và hiểu hành vi của hệ thống qua logs, metrics, traces, và các tín hiệu khác. |
| **Audit Trail** | Dấu vết kiểm toán | Tập hợp bằng chứng ghi lại các hành động hoặc sự kiện để phục vụ kiểm tra và truy vết sau này. |
| **Regulated Environment** | Môi trường có ràng buộc quy định | Môi trường mà hệ thống phải tuân thủ các yêu cầu pháp lý, bảo mật, hoặc vận hành nghiêm ngặt. |
