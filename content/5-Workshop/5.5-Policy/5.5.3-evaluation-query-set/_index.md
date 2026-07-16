---
title : "Evaluation Query Set"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.5.3. </b> "
---

## Purpose

This page posts the fixed query set used for the first workshop evaluation pass.

Keeping the benchmark stable makes later comparisons fair.

## Fixed query set

| query_id | query_text | query_type | short intent note |
| --- | --- | --- | --- |
| A01 | `Gỏi` | broad dish style | check whether the answer handles a broad food category well |
| A02 | `gỏi mít thịt ba chỉ` | exact dish | check whether the answer is strong on a specific known dish |
| A03 | `món gà thanh đạm` | ingredient + style | check whether the answer matches both ingredient and light flavor or style intent |
| A04 | `canh chua` | dish family | check whether the answer handles a common Vietnamese dish family clearly |
| A05 | `món thịt kho` | ingredient + cooking style | check whether the answer identifies braised pork-style dishes well |
| A06 | `món cuốn` | category | check whether the answer summarizes wrapped-roll style dishes helpfully |
| A07 | `món ăn ngày Tết` | use-case | check whether the answer handles occasion-based food requests |
| A08 | `món ăn cho bữa sáng` | use-case | check whether the answer handles meal-time recommendations well |
| A09 | `món cá nhẹ bụng` | ingredient + feel | check whether the answer interprets a gentle or light preference well |
| A10 | `món chay đơn giản` | dietary style | check whether the answer handles simple vegetarian intent clearly |
| A11 | `món nướng` | cooking style | check whether the answer handles grilled-food requests broadly but usefully |
| A12 | `bún` | staple/category | check whether the answer handles a broad staple or noodle query without becoming too vague |

## How it is used

- The same set can support both RAG evaluation and AI evaluation.
- RAG evaluation uses it to inspect top-k retrieval quality.
- AI evaluation uses it to judge final response quality.
- The set should not be silently replaced, or later comparisons become unclear.
