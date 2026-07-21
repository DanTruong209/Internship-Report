---
title: "Week 11 Worklog"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

## Mục tiêu tuần 11:

Hoàn thiện module AI Assistant và kết thúc giai đoạn tích hợp bảo mật cho hệ thống **Incident Response Management System (IRMS)**.

Cải thiện tính bảo mật của hệ thống AI thông qua việc bảo vệ thông tin nhạy cảm, kiểm tra IAM Permission và giám sát hoạt động hệ thống bằng các dịch vụ AWS.

Thực hiện kiểm thử, triển khai và hoàn thiện tài liệu cho chức năng AI Assistant.

---

## Các công việc thực hiện trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Tích hợp AWS Secrets Manager để lưu trữ an toàn thông tin xác thực của AI API.<br><br>- Cập nhật Backend để lấy secret từ AWS thay vì lưu trực tiếp API Key trong source code. | 29/06/2026 | 29/06/2026 | AWS Secrets Manager Documentation |
| 3 | - Kiểm tra và cải thiện IAM Policy cho các dịch vụ liên quan đến AI.<br><br>- Áp dụng nguyên tắc Least Privilege cho Lambda Function và các AWS Resource.<br><br>- Kiểm tra CloudWatch Logs và cấu hình monitoring. | 30/06/2026 | 30/06/2026 | AWS Security Best Practices |
| 4 | - Kiểm thử luồng thông báo bảo mật thông qua EventBridge và SNS.<br><br>- Kiểm tra cơ chế tự động tạo cảnh báo và gửi notification khi xảy ra sự kiện. | 01/07/2026 | 01/07/2026 | AWS EventBridge & SNS Documentation |
| 5 | - Thực hiện kiểm thử bảo mật và hiệu năng cho AI Assistant.<br><br>- Đánh giá chất lượng phản hồi, thời gian xử lý, xử lý lỗi và kiểm tra dữ liệu đầu vào. | 02/07/2026 | 02/07/2026 | AI Testing Practices |
| 6 | - Hoàn thiện triển khai AI Assistant và tài liệu kỹ thuật.<br><br>- Kiểm tra lại toàn bộ luồng tích hợp và chuẩn bị nội dung trình bày dự án. | 03/07/2026 | 03/07/2026 | Project Documentation |

---

## Kết quả đạt được trong tuần 11:

Tuần thứ mười một đánh dấu giai đoạn hoàn thiện quá trình phát triển module **AI Assistant** trong hệ thống **Incident Response Management System (IRMS)**.

Công việc quan trọng đầu tiên là tăng cường bảo mật cho quá trình tích hợp AI. Thay vì lưu trực tiếp API Key trong source code, tôi đã tích hợp **AWS Secrets Manager** để quản lý thông tin nhạy cảm một cách an toàn. Backend có thể lấy thông tin xác thực khi cần thiết mà không làm lộ dữ liệu bảo mật.

Bên cạnh đó, tôi tiến hành kiểm tra và điều chỉnh IAM Policy cho các thành phần trong hệ thống. Việc áp dụng nguyên tắc **Least Privilege** giúp giới hạn quyền truy cập của từng service, giảm nguy cơ xảy ra lỗi bảo mật.

Đối với phần monitoring và automation, tôi thực hiện kiểm thử luồng tích hợp giữa **EventBridge và SNS** để đảm bảo hệ thống có thể xử lý các sự kiện bảo mật và gửi thông báo đến người phụ trách.

Ngoài ra, tôi tiến hành kiểm thử AI Assistant với các tiêu chí:

- Độ chính xác của phản hồi.
- Hiệu năng xử lý.
- Khả năng xử lý lỗi.
- Kiểm tra dữ liệu đầu vào.
- Các vấn đề bảo mật như Prompt Injection.

Sau quá trình kiểm thử và tối ưu, tôi hoàn thiện việc triển khai AI Assistant và xây dựng tài liệu kỹ thuật mô tả:

- Kiến trúc AI Assistant.
- Luồng tích hợp giữa các thành phần.
- Cấu hình bảo mật.
- Quy trình hoạt động của hệ thống.

