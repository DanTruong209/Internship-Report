---
title: "Week 11 Worklog"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

## Week 11 Objectives:

Finalize the AI Assistant module and complete the security integration phase for the Incident Response Management System (IRMS).

Improve AI security by protecting sensitive credentials, reviewing IAM permissions, and monitoring system activities through AWS services.

Perform testing, deployment, and documentation for the completed AI Assistant functionality.

Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Integrate AWS Secrets Manager to securely store AI API credentials.<br><br>- Update backend service to retrieve secrets securely instead of storing API keys directly in source code. | 06/29/2026 | 06/29/2026 | AWS Secrets Manager Documentation |
| 3 | - Review and improve IAM policies for AI-related services.<br><br>- Apply the principle of least privilege for Lambda functions and AWS resources.<br><br>- Review CloudWatch logs and monitoring configuration. | 06/30/2026 | 06/30/2026 | AWS Security Best Practices |
| 4 | - Perform EventBridge and SNS testing for security event notification flow.<br><br>- Verify automated alert mechanisms and incident notification process. | 07/01/2026 | 07/01/2026 | AWS EventBridge & SNS Documentation |
| 5 | - Conduct AI Assistant security and performance testing.<br><br>- Evaluate response quality, processing time, error handling, and input validation. | 07/02/2026 | 07/02/2026 | AI Testing Practices |
| 6 | - Finalize AI Assistant deployment and complete technical documentation.<br><br>- Review the entire integration flow and prepare project presentation materials. | 07/03/2026 | 07/03/2026 | Project Documentation |

---

## Week 11 Achievements:

This week marked the final stage of developing the AI Assistant module for the Incident Response Management System (IRMS).

The first important task was improving the security of the AI integration. Instead of storing API credentials directly inside the application source code, I integrated AWS Secrets Manager to securely manage sensitive information and allow the backend service to retrieve credentials when needed.

I also reviewed IAM permissions and adjusted access policies following the principle of least privilege. This helped ensure that each AWS service only had the permissions required for its specific function.

For system monitoring and automation, I tested the integration between EventBridge and SNS to verify the security notification workflow. When a security event occurs, the system can trigger the appropriate processing flow and send notifications to responsible users.

In addition, I performed AI Assistant testing focusing on:

- Response accuracy.
- Processing performance.
- Error handling.
- Input validation.
- Security considerations such as prompt injection risks.

After completing testing and improvements, I finalized the deployment process and prepared technical documentation describing the AI Assistant architecture, integration flow, and security configuration.

Overall, Week 11 completed the main development cycle of the AI Assistant feature, transforming IRMS into a more intelligent and secure incident response platform with AI-supported investigation capabilities.