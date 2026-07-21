---
title: "Week 8 Worklog"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

## Mục tiêu tuần 8:

Tìm hiểu kiến trúc hướng sự kiện (Event-Driven Architecture) và mô hình xử lý bất đồng bộ trên AWS.

Nghiên cứu cách các dịch vụ Messaging như Amazon SQS, Amazon SNS và Amazon EventBridge hỗ trợ xây dựng hệ thống phân tán.

Thực hành thiết kế các luồng xử lý dựa trên sự kiện và hiểu cách xử lý bất đồng bộ giúp hệ thống tăng khả năng mở rộng và độ tin cậy.

---

## Các công việc thực hiện trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Nghiên cứu khái niệm Event-Driven Architecture trên AWS.<br><br>- Tìm hiểu vai trò của Event Producer, Event Consumer và cơ chế xử lý bất đồng bộ trong hệ thống Cloud hiện đại. | 08/06/2026 | 08/06/2026 | AWS Event-Driven Architecture Documentation |
| 3 | - Tìm hiểu Amazon SQS và Amazon SNS.<br><br>- Nghiên cứu SQS Standard/FIFO Queue, SNS Topic, Subscription và cơ chế truyền tải Message. | 09/06/2026 | 09/06/2026 | AWS Documentation |
| 4 | - Thiết kế luồng xử lý bất đồng bộ sử dụng SQS và SNS.<br><br>- Phân tích cách Message Queue giúp xử lý lượng lớn yêu cầu và tránh quá tải hệ thống. | 10/06/2026 | 10/06/2026 | AWS Messaging Services |
| 5 | - Nghiên cứu cơ chế xử lý lỗi trong hệ thống phân tán.<br><br>- Tìm hiểu Dead Letter Queue (DLQ), Message Retry và các chiến lược xử lý khi xảy ra lỗi. | 11/06/2026 | 11/06/2026 | AWS SQS Documentation |
| 6 | - Ôn tập mô hình tích hợp SQS + SNS.<br><br>- Thiết kế các luồng Event mẫu và kiểm tra cách các dịch vụ giao tiếp bất đồng bộ. | 12/06/2026 | 12/06/2026 | AWS Architecture Center |
| 7 | - Thực hành cấu hình Amazon SNS Topic và Amazon SQS Queue trên AWS Console.<br><br>- Kiểm tra việc gửi Message và nhận Notification thông qua các dịch vụ đã cấu hình. | 13/06/2026 | 13/06/2026 | AWS Console |

---

## Kết quả đạt được trong tuần 8:

Tuần này tập trung vào việc tìm hiểu Event-Driven Architecture, một trong những mô hình quan trọng để xây dựng các hệ thống Cloud có khả năng mở rộng.

Tôi đã tìm hiểu hạn chế của mô hình xử lý đồng bộ truyền thống khi hệ thống phải tiếp nhận nhiều yêu cầu cùng lúc. Thông qua Amazon SQS và SNS, tôi hiểu được cách AWS hỗ trợ giao tiếp bất đồng bộ giữa các thành phần, giúp từng dịch vụ có thể xử lý độc lập và giảm tải cho hệ thống chính.

Tôi đã thực hành thiết kế các luồng xử lý Message sử dụng SQS làm Queue và SNS làm cơ chế gửi thông báo. Các khái niệm như FIFO Queue, Subscription, Message Retry và Dead Letter Queue (DLQ) giúp tôi hiểu rõ hơn cách AWS đảm bảo tính ổn định và hạn chế mất dữ liệu khi xảy ra lỗi trong quá trình xử lý.

Ngoài ra, tôi thực hành cấu hình trực tiếp SQS Queue và SNS Topic trên AWS Console để hiểu rõ quy trình gửi và nhận Message trong môi trường thực tế.

