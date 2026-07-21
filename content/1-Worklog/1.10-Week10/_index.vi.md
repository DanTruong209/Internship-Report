---
title: "Week 10 Worklog"
date: 2026-06-22
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

## Mục tiêu tuần 10:

Phát triển các chức năng AI cốt lõi cho hệ thống **Incident Response Management System (IRMS)**.

Tích hợp Groq API làm nền tảng xử lý AI và xây dựng các chức năng hỗ trợ Security Analyst trong quá trình điều tra sự cố.

Triển khai các tính năng AI Analyst bao gồm tóm tắt incident, đánh giá mức độ nghiêm trọng, đề xuất hướng xử lý và xây dựng chức năng AI Chat.

---

## Các công việc thực hiện trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Nghiên cứu và tích hợp Groq API vào Backend của hệ thống IRMS.<br><br>- Xây dựng luồng giao tiếp giữa Backend Service và AI Provider để xử lý các yêu cầu phân tích incident. | 22/06/2026 | 22/06/2026 | Groq API Documentation |
| 3 | - Nghiên cứu Prompt Engineering cho bài toán phân tích sự cố an ninh mạng.<br><br>- Thiết kế prompt có cấu trúc để AI tạo summary, đánh giá severity và đề xuất hướng xử lý. | 23/06/2026 | 23/06/2026 | Prompt Engineering Resources |
| 4 | - Phát triển chức năng AI Analyst.<br><br>- Xây dựng khả năng tạo Incident Summary và Recommended Actions dựa trên dữ liệu sự cố. | 24/06/2026 | 24/06/2026 | Generative AI Development |
| 5 | - Phát triển chức năng AI Chat dành cho Security Analyst.<br><br>- Cho phép người dùng trao đổi với AI để hỗ trợ quá trình điều tra incident. | 25/06/2026 | 25/06/2026 | AI Application Design |
| 6 | - Xây dựng và cải thiện AI Context Builder.<br><br>- Tổng hợp dữ liệu Incident, Timeline và Evidence Metadata để cung cấp đầy đủ context cho AI phân tích.<br><br>- Kiểm thử chất lượng phản hồi và tối ưu prompt. | 26/06/2026 | 26/06/2026 | AI Context Engineering |

---

## Kết quả đạt được trong tuần 10:

Trong tuần thứ mười, tôi bắt đầu giai đoạn phát triển AI cho hệ thống **Incident Response Management System (IRMS)**.

Kết quả quan trọng nhất trong tuần là tích hợp thành công Groq API vào Backend và xây dựng được luồng giao tiếp giữa hệ thống IRMS với tầng xử lý AI.

Thay vì chỉ gửi một đoạn mô tả incident đơn giản, tôi xây dựng cơ chế **AI Context Builder** để thu thập và tổ chức các dữ liệu liên quan như:

- Thông tin Incident.
- Timeline điều tra.
- Metadata của Evidence.

Việc cung cấp đầy đủ context giúp AI hiểu rõ hơn tình huống bảo mật trước khi đưa ra phân tích và đề xuất xử lý.

Bên cạnh việc tích hợp API, tôi tập trung vào **Prompt Engineering** để cải thiện chất lượng phản hồi của AI.

Các prompt được thiết kế nhằm hướng dẫn AI thực hiện các nhiệm vụ:

- Tạo bản tóm tắt Incident.
- Đánh giá mức độ nghiêm trọng.
- Đề xuất các bước điều tra tiếp theo.
- Đưa ra hướng xử lý sự cố.

Ngoài ra, tôi đã phát triển phiên bản ban đầu của hai chức năng:

- **AI Analyst:** hỗ trợ phân tích và đưa ra recommendation.
- **AI Chat:** cho phép Security Analyst trao đổi trực tiếp với AI trong quá trình điều tra.

Thông qua quá trình kiểm thử, tôi tiếp tục điều chỉnh prompt và cách xây dựng context để cải thiện độ chính xác và tính phù hợp của câu trả lời.

Nhìn chung, Week 10 là một bước tiến quan trọng trong việc chuyển IRMS từ một hệ thống quản lý incident truyền thống thành một nền tảng bảo mật thông minh có khả năng hỗ trợ điều tra bằng AI.