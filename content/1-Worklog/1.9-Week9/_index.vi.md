---
title: "Week 9 Worklog"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

## Mục tiêu tuần 9:

Bắt đầu triển khai dự án thực tập chính: **Incident Response Management System (IRMS)**.

Nghiên cứu và thiết kế module **AI Assistant** nhằm hỗ trợ Security Analyst trong quá trình điều tra và xử lý sự cố an ninh mạng.

Tìm hiểu cách tích hợp Generative AI vào quy trình Incident Response thông qua việc xây dựng AI Context, Prompt Engineering và đưa ra các đề xuất xử lý sự cố.

---

## Các công việc thực hiện trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Phân tích yêu cầu của dự án IRMS và xác định vai trò của AI Assistant trong hệ thống.<br><br>- Nghiên cứu cách AI có thể hỗ trợ Security Analyst trong việc phân tích incident, tạo bản tóm tắt và đề xuất hướng xử lý. | 15/06/2026 | 15/06/2026 | AWS AI/ML Documentation |
| 3 | - Thiết kế kiến trúc tổng thể của AI Assistant.<br><br>- Xác định các dữ liệu cần cung cấp cho AI bao gồm Incident Information, Timeline điều tra và Evidence Metadata. | 16/06/2026 | 16/06/2026 | System Architecture Design |
| 4 | - Nghiên cứu phương án tích hợp AI vào hệ thống IRMS.<br><br>- Tìm hiểu cách Backend giao tiếp với AI Provider thông qua API. | 17/06/2026 | 17/06/2026 | Generative AI Documentation |
| 5 | - Thiết kế cơ chế AI Context Builder.<br><br>- Xây dựng phương án tổng hợp dữ liệu Incident, Timeline và Evidence để tạo context đầu vào cho AI. | 18/06/2026 | 18/06/2026 | Prompt Engineering Resources |
| 6 | - Phân tích các yêu cầu bảo mật khi tích hợp AI.<br><br>- Nghiên cứu bảo vệ API Key, IAM Permission và phương thức giao tiếp an toàn giữa các service. | 19/06/2026 | 19/06/2026 | AWS Security Best Practices |

---

## Kết quả đạt được trong tuần 9:

Tuần thứ chín đánh dấu giai đoạn bắt đầu triển khai dự án thực tập chính: **Incident Response Management System (IRMS)**.

Trong tuần này, tôi tập trung nghiên cứu và thiết kế module **AI Assistant**, một thành phần giúp hỗ trợ Security Analyst trong quá trình điều tra và xử lý các sự cố an ninh mạng.

Thay vì Security Analyst phải phân tích thủ công toàn bộ thông tin của từng incident, AI Assistant có thể hỗ trợ tạo bản tóm tắt sự cố, đánh giá mức độ nghiêm trọng và đề xuất các bước xử lý phù hợp.

Tôi đã phân tích vai trò của AI trong quy trình Incident Response và thiết kế hướng tích hợp giữa hệ thống IRMS với AI Service.

Phần quan trọng nhất trong tuần là thiết kế cơ chế **AI Context Builder**. Cơ chế này giúp thu thập và tổng hợp dữ liệu từ nhiều nguồn khác nhau để cung cấp đầy đủ thông tin cho AI phân tích.

Các dữ liệu được đưa vào context bao gồm:

- Thông tin Incident.
- Timeline điều tra.
- Metadata của Evidence.
- Các hoạt động xử lý trước đó.

Luồng xử lý được thiết kế:

**Incident Data → AI Context Builder → AI Model → Security Analysis & Recommendations**

Ngoài việc thiết kế chức năng AI, tôi cũng nghiên cứu các yêu cầu bảo mật khi tích hợp AI vào hệ thống.

Các vấn đề được xem xét bao gồm:

- Bảo vệ API Key.
- Kiểm soát quyền truy cập bằng IAM.
- Kiểm tra dữ liệu đầu vào.
- Đảm bảo giao tiếp an toàn giữa Backend và AI Provider.

Nhìn chung, Week 9 giúp tôi xây dựng nền tảng ban đầu cho việc phát triển AI Assistant trong hệ thống IRMS. Các thiết kế về kiến trúc và bảo mật trong tuần này sẽ là cơ sở để triển khai các phần tiếp theo như Groq API Integration, Prompt Engineering, AI Analyst Development và AI Chat.