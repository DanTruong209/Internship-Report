---
title: "Week 8 Worklog"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

## Week 8 Objectives:

Understand Event-Driven Architecture and asynchronous processing patterns on AWS.

Learn how AWS messaging services such as Amazon SQS, Amazon SNS, and Amazon EventBridge support distributed systems.

Practice designing event-based workflows and understand how asynchronous processing can improve system scalability and reliability.

---

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Research Event-Driven Architecture concepts on AWS.<br><br>- Understand the role of events, producers, consumers, and asynchronous processing in modern cloud systems. | 06/08/2026 | 06/08/2026 | AWS Event-Driven Architecture Documentation |
| 3 | - Study Amazon SQS and SNS services.<br><br>- Understand SQS Standard/FIFO Queue, SNS Topic, Subscription, and message delivery mechanisms. | 06/09/2026 | 06/09/2026 | AWS Documentation |
| 4 | - Design an asynchronous processing workflow using SQS and SNS.<br><br>- Analyze how message queues can handle large workloads and prevent system overload. | 06/10/2026 | 06/10/2026 | AWS Messaging Services |
| 5 | - Research error handling mechanisms in distributed systems.<br><br>- Learn about Dead Letter Queue (DLQ), message retry, and failure handling strategies. | 06/11/2026 | 06/11/2026 | AWS SQS Documentation |
| 6 | - Review SQS + SNS integration patterns.<br><br>- Design sample event flows and verify how services communicate asynchronously. | 06/12/2026 | 06/12/2026 | AWS Architecture Center |
| 7 | - Practice configuring Amazon SNS Topic and Amazon SQS Queue on AWS Console.<br><br>- Test sending messages and receiving notifications through the configured services. | 06/13/2026 | 06/13/2026 | AWS Console |

---

## Week 8 Achievements:

This week focused on understanding Event-Driven Architecture, which is one of the important design patterns for building scalable cloud applications.

I studied how traditional synchronous processing can become a limitation when systems receive a large number of requests simultaneously. Through Amazon SQS and SNS, I learned how AWS enables asynchronous communication between services, allowing different components to process tasks independently.

I practiced designing message processing flows using SQS as a queue system and SNS as a notification mechanism. Concepts such as FIFO Queue, Subscription, Message Retry, and Dead Letter Queue (DLQ) helped me understand how AWS maintains reliability and prevents data loss when processing failures occur.

I also practiced configuring SQS Queue and SNS Topic directly on AWS Console to understand the actual workflow of sending and receiving messages.

