---
title: "Week 7 Worklog"
date: 2026-06-01
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

## Mục tiêu tuần 7:

Tìm hiểu các phương pháp triển khai ứng dụng trên AWS và cách các hệ thống Cloud được đưa vào môi trường thực tế.

Nghiên cứu AWS Elastic Beanstalk như một giải pháp Platform-as-a-Service (PaaS), đồng thời so sánh với phương pháp triển khai truyền thống trên EC2.

Tìm hiểu các khái niệm CI/CD và các công cụ tự động hóa triển khai trên AWS để chuẩn bị cho quá trình xây dựng hệ thống thực tế.

---

## Các công việc thực hiện trong tuần:

| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Nghiên cứu kiến thức cơ bản về AWS Elastic Beanstalk.<br><br>- Tìm hiểu Application, Environment, quy trình Deploy và cách Beanstalk tự động quản lý tài nguyên AWS. | 01/06/2026 | 01/06/2026 | AWS Elastic Beanstalk Documentation |
| 3 | - So sánh triển khai truyền thống trên EC2 sử dụng PM2 với triển khai bằng AWS Elastic Beanstalk.<br><br>- Phân tích sự khác biệt về quản lý tài nguyên, khả năng mở rộng và độ phức tạp vận hành. | 02/06/2026 | 02/06/2026 | AWS Documentation |
| 4 | - Thực hành triển khai Backend Node.js đơn giản bằng Elastic Beanstalk.<br><br>- Tìm hiểu Application Version, Environment Configuration và quy trình Deployment. | 03/06/2026 | 03/06/2026 | AWS Elastic Beanstalk |
| 5 | - Tìm hiểu các dịch vụ CI/CD trên AWS.<br><br>- Nghiên cứu CodeCommit, CodeBuild, CodeDeploy và CodePipeline. | 04/06/2026 | 04/06/2026 | AWS CI/CD Documentation |
| 6 | - Nghiên cứu quy trình triển khai tự động.<br><br>- Tìm hiểu cách kết nối Source Code từ GitHub/CodeCommit với CodePipeline để tự động Build và Deploy. | 05/06/2026 | 05/06/2026 | AWS Developer Tools |

---

## Kết quả đạt được trong tuần 7:

Tuần này tập trung vào việc tìm hiểu quy trình triển khai ứng dụng hiện đại trên AWS.

Trước đây, tôi chủ yếu triển khai ứng dụng thủ công trên EC2 bằng PM2, yêu cầu phải tự cấu hình Server, cài đặt Dependency và quản lý tiến trình ứng dụng. Qua việc tìm hiểu AWS Elastic Beanstalk, tôi hiểu được cách AWS tự động quản lý các thành phần hạ tầng như EC2 Instance, Load Balancer, Auto Scaling và Application Environment.

Tôi đã thực hành triển khai một ứng dụng Backend Node.js đơn giản bằng Elastic Beanstalk và hiểu rõ hơn về mô hình triển khai PaaS. So với việc quản lý Server truyền thống, Beanstalk cung cấp cách triển khai chuẩn hóa hơn, dễ quản lý và phù hợp với môi trường Production.

Bên cạnh đó, tôi nghiên cứu hệ sinh thái CI/CD trên AWS bao gồm CodePipeline và CodeBuild. Tôi hiểu được cách thay đổi Source Code có thể tự động kích hoạt quá trình Build và Deployment, giúp giảm thao tác thủ công và nâng cao hiệu quả phát triển.

