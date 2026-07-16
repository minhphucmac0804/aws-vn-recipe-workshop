---
title: "Chia sẻ và phản hồi"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Phần này tóm tắt cách tôi trải nghiệm chương trình, kiểu hướng dẫn nào hữu ích nhất với tôi, và những điểm mà tôi nghĩ có thể cải thiện cho các thực tập sinh sau.

## Đánh giá chung

**1. Môi trường làm việc**

Môi trường học tập khá linh hoạt và hỗ trợ tốt, điều này quan trọng vì hướng dự án của tôi không rõ ngay từ đầu. Tôi dành một phần lớn thời gian thực tập để cân bằng giữa học kỹ thuật rộng, công việc đồ án tốt nghiệp, và sau đó là quá trình hoàn thiện workshop submission, nên việc có không gian để học và điều chỉnh hướng đi là rất cần thiết. Tuy vậy, sự linh hoạt đó cũng đồng nghĩa với việc tôi phải tự rèn nhiều hơn về quản lý bản thân và thu hẹp dự án theo thời gian.

**2. Sự hỗ trợ từ mentor / admin chương trình**

Kiểu hỗ trợ hữu ích nhất với tôi không chỉ là giải thích kỹ thuật, mà còn là việc buộc dự án trở nên cụ thể hơn và dễ review hơn. Hướng dẫn đặc biệt có giá trị khi tôi cần tách luồng workshop cuối cùng khỏi các nhánh khám phá trước đó, làm rõ reviewer cần nhìn thấy bằng chứng gì, và nghĩ kỹ hơn về validation, cleanup, và cost awareness. Với tôi, kiểu hỗ trợ đó quan trọng hơn việc chỉ nhận các câu trả lời kỹ thuật rời rạc.

**3. Mức độ liên quan của công việc với chuyên ngành học**

Kỳ thực tập có liên hệ với nền tảng học tập của tôi, nhưng không theo cách trực tiếp hoàn toàn. Điểm mạnh ban đầu của tôi nằm nhiều hơn ở toán, thống kê, và các ý tưởng machine learning hơn là cloud engineering hay deployment. Chính vì vậy, dự án này hữu ích ở chỗ nó buộc tôi phải nối các khái niệm ML quen thuộc như embeddings, retrieval, và evaluation với những mảng tôi yếu hơn nhiều, như AWS services, deployment flow, và system design theo hướng reviewer-facing.

**4. Cơ hội học hỏi và phát triển kỹ năng**

Kỳ thực tập này giúp tôi phát triển ở nhiều lớp cùng lúc. Ở phía AWS, tôi tiến bộ trong việc sử dụng Lambda, ECR, DynamoDB, CloudWatch, EventBridge Scheduler, SNS, và các phần thiết lập liên quan đến IAM. Ở phía ML, tôi hiểu thực tế hơn về retrieval systems, vector search, embeddings, dataset quality, và sự khác biệt giữa một hệ thống chạy được với một hệ thống truy xuất và trả lời tốt. Tôi cũng tiến bộ trong documentation và technical reporting khi phải chuyển implementation thành một workshop có cấu trúc rõ ràng.

**5. Cấu trúc chương trình và cách giao tiếp**

Chương trình cho tôi khá nhiều tự do để khám phá, nhưng điều đó cũng có nghĩa là chất lượng hướng đi của tôi phụ thuộc rất nhiều vào việc tôi thu hẹp dự án sớm đến mức nào. Nhìn lại, tôi nghĩ sẽ tốt hơn nếu có các ví dụ sớm hơn về scope workshop phù hợp, các nhắc nhở mạnh hơn để giảm exploration drift, và nhiều checkpoint hơn tập trung vào reviewer-facing output. Cấu trúc giao tiếp hiện tại vẫn hữu ích, nhưng tôi hưởng lợi nhiều nhất khi kỳ vọng được làm rõ thành các đầu ra cụ thể.

**6. Quy trình thực tập / kỳ vọng**

Quy trình trở nên rõ ràng hơn nhiều ở giai đoạn cuối, khi dự án được nhìn không chỉ như một implementation task mà còn như một workshop submission cần có validation evidence, evaluation notes, và cleanup guidance. Ở giai đoạn đầu, tôi dành nhiều thời gian hơn cho học và thử nghiệm so với việc xây trực tiếp sản phẩm nộp cuối. Điều đó làm hành trình dài hơn, nhưng đồng thời cũng tạo cho workshop cuối nền tảng kỹ thuật mạnh hơn so với một hướng triển khai quá hẹp ngay từ đầu.

## Một số câu hỏi thêm

**Điều gì làm bạn hài lòng nhất trong kỳ thực tập?**

Điều làm tôi hài lòng nhất là việc nhiều hướng công việc rời rạc cuối cùng đã hội tụ thành một đầu ra hoàn chỉnh. Các phần như recipe data, retrieval, Qdrant, embeddings, AWS labs, observability, và evaluation ban đầu không phải lúc nào cũng nhìn giống một dự án thống nhất, nhưng đến cuối cùng chúng đã ghép lại thành một AWS workshop thực tế. Sự hội tụ đó khiến chặng đường dài của dự án trở nên có ý nghĩa.

**Bạn nghĩ điều gì nên được cải thiện cho các thực tập sinh sau?**

Tôi nghĩ các thực tập sinh sau sẽ được lợi nhiều nếu nhận được hỗ trợ sớm hơn về cách định scope dự án và được xem sớm hơn các ví dụ về một workshop repo tốt thực sự trông như thế nào. Cũng nên làm rõ sớm hơn rằng khám phá kỹ thuật là hữu ích, nhưng sản phẩm nộp cuối vẫn cần một kiến trúc hẹp, reviewer-facing, có evidence rõ, và có cleanup discipline. Nhiều checkpoint có cấu trúc hơn quanh các điểm này sẽ giúp giảm drift đáng kể.

**Nếu giới thiệu chương trình này cho bạn bè, bạn có khuyên họ tham gia không? Vì sao?**

Có, tôi vẫn sẽ giới thiệu chương trình này, đặc biệt với những người muốn đi xa hơn kiến thức kiểu trên lớp và học cách biến công việc kỹ thuật thành một sản phẩm thực tế. Chương trình cho tôi đủ không gian để học nghiêm túc và kết nối cloud services với tư duy ML. Tuy nhiên, tôi cũng nghĩ trải nghiệm sẽ tốt hơn nhiều nếu người tham gia sẵn sàng chấp nhận sự mơ hồ ban đầu và chủ động thu hẹp scope dần dần.

## Đề xuất và mong muốn

- Có hướng dẫn sớm hơn về cách chọn một project scope vừa với format workshop.
- Cung cấp sớm hơn các ví dụ repo cuối tốt, đặc biệt là ví dụ phân biệt rõ exploration notes với reviewer-facing deliverables.
- Bổ sung nhiều checkpoint hơn tập trung vào worklog quality, evidence collection, evaluation, và cleanup expectations.
- Nếu có thể, nhắc sớm hơn rằng cost control, secret redaction, và cleanup cũng là một phần của deliverable, không chỉ là chi tiết triển khai.
