---
title : "Evaluation Query Set"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.5.3. </b> "
---

## Mục tiêu

Trang này đăng bộ query cố định dùng cho lượt evaluation đầu tiên của workshop.

Giữ benchmark ổn định sẽ giúp các lần so sánh sau công bằng hơn.

## Fixed query set

| query_id | query_text | query_type | short intent note |
| --- | --- | --- | --- |
| A01 | `Gỏi` | broad dish style | kiểm tra câu trả lời có xử lý tốt một nhóm món rộng không |
| A02 | `gỏi mít thịt ba chỉ` | exact dish | kiểm tra câu trả lời có mạnh với một món cụ thể quen thuộc không |
| A03 | `món gà thanh đạm` | ingredient + style | kiểm tra câu trả lời có khớp cả nguyên liệu lẫn phong cách thanh đạm không |
| A04 | `canh chua` | dish family | kiểm tra câu trả lời có xử lý rõ một nhóm món Việt phổ biến không |
| A05 | `món thịt kho` | ingredient + cooking style | kiểm tra câu trả lời có nhận diện tốt nhóm món thịt kho không |
| A06 | `món cuốn` | category | kiểm tra câu trả lời có tóm tắt hữu ích nhóm món cuốn không |
| A07 | `món ăn ngày Tết` | use-case | kiểm tra câu trả lời có xử lý yêu cầu theo dịp sử dụng không |
| A08 | `món ăn cho bữa sáng` | use-case | kiểm tra câu trả lời có xử lý tốt yêu cầu theo bữa ăn không |
| A09 | `món cá nhẹ bụng` | ingredient + feel | kiểm tra câu trả lời có hiểu được sở thích nhẹ bụng không |
| A10 | `món chay đơn giản` | dietary style | kiểm tra câu trả lời có xử lý rõ yêu cầu món chay đơn giản không |
| A11 | `món nướng` | cooking style | kiểm tra câu trả lời có xử lý yêu cầu món nướng theo cách đủ hữu ích không |
| A12 | `bún` | staple/category | kiểm tra câu trả lời có xử lý truy vấn rộng về bún mà không quá mơ hồ không |

## Cách sử dụng

- Cùng một bộ query có thể hỗ trợ cả RAG evaluation và AI evaluation.
- RAG evaluation dùng bộ này để kiểm tra chất lượng top-k retrieval.
- AI evaluation dùng bộ này để đánh giá chất lượng câu trả lời cuối.
- Không nên âm thầm thay bộ query này, nếu không việc so sánh sẽ trở nên thiếu rõ ràng.
