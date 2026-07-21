---
title: "Week 9 Worklog"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

## Week 9 Objectives:

Start implementing the main internship project: Incident Response Management System (IRMS).

Research and design the AI Assistant module to support Security Analysts during incident investigation.

Analyze how Generative AI can be integrated into the incident response workflow through AI context building, prompt engineering, and security-aware recommendations.

Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ---- | ---------- | --------------- | ------------------ |
| 2 | - Analyze the IRMS project requirements and define the role of AI Assistant in incident response.<br><br>- Research how AI can support security analysts in incident analysis, incident summary, and recommended actions. | 06/15/2026 | 06/15/2026 | AWS AI/ML Documentation |
| 3 | - Design the AI Assistant architecture and data flow.<br><br>- Identify required input context including Incident information, Timeline investigation data, and Evidence metadata. | 06/16/2026 | 06/16/2026 | System Architecture Design |
| 4 | - Research AI integration approaches for IRMS.<br><br>- Compare different LLM API solutions and study the communication flow between Backend Service and AI Provider. | 06/17/2026 | 06/17/2026 | Generative AI Documentation |
| 5 | - Design the AI Context Builder mechanism.<br><br>- Define how incident data, investigation timeline, and evidence information are collected and transformed into AI input context. | 06/18/2026 | 06/18/2026 | AI Prompt Engineering Resources |
| 6 | - Analyze security requirements for AI integration.<br><br>- Identify security considerations including API Key protection, IAM permissions, and secure communication between services. | 06/19/2026 | 06/19/2026 | AWS Security Best Practices |

---

## Week 9 Achievements:

This week marked the beginning of the implementation phase for my main internship project: **Incident Response Management System (IRMS)**.

The main focus was researching and designing the **AI Assistant module**, which aims to support Security Analysts during cybersecurity incident investigation. Instead of manually analyzing every incident, the AI Assistant can help summarize incidents, evaluate severity levels, and suggest possible response actions.

During this week, I analyzed the role of AI in the incident response workflow and designed the overall integration approach between the IRMS system and the AI service.

The most important part was designing the **AI Context Builder**, which defines how information from different sources can be collected and provided to the AI model. The context includes:

- Incident information.
- Investigation timeline.
- Evidence metadata.
- Previous investigation activities.

The designed workflow:

**Incident Data → AI Context Builder → AI Model → Security Analysis & Recommendations**

I also researched security requirements before integrating AI into the system. Important considerations include protecting API credentials, applying proper IAM permissions, validating user input, and ensuring secure communication between backend services and the AI provider.

Overall, Week 9 helped establish the foundation for developing the AI Assistant feature in IRMS. The architecture design and security analysis from this week will be used as the basis for the next stages: Groq API integration, prompt engineering, AI Analyst development, and AI Chat implementation.