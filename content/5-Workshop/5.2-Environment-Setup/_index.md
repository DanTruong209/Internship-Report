---
title: "Environment Setup"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

## 2. Environment Setup

#### Contents

- 5.2.2 Prerequisites

### 5.2.2 Prerequisites

#### 5.2.2.1 AWS Account and Permissions
- AWS Account da kich hoat (account chung of nhom)
- IAM User with quyen du de create the service lien quan
- Region su dung: ap-southeast-1 (Singapore) — thong nhat toan nhom, not doi

#### 5.2.2.2 Install Tools
AWS CLI:

```bash
`# Verify installation`
aws --version
```

`# if chua has, install theo huong dan:`
`# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html`

`# Cau hinh after khi install`
aws configure --profile irms-shared
`# AWS Access Key ID: <enter key>`
`# AWS Secret Access Key: <enter secret>`
`# Default region name: ap-southeast-1`
`# Default output format: json`
AWS SAM CLI:

```bash
`# Verify installation`
sam --version
```

`# Install dat: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html`

`# Verify`
sam --version
`# SAM CLI, version 1.x.x`
Node.js & npm (for Frontend):

```bash
node --version   # >= 18.x
npm --version
Python 3.12 (for Lambda):
```

bash
python3 --version   # >= 3.12

#### 5.2.2.3 Set Up Budget Alert (BAT BUOC lam before)
Step nay phai lam before khi deploy bat ky resource nao.
- Vao AWS Console → Billing → Budgets → Create budget
- Select Cost budget
- Budget name: irms-demo-budget
- Budgeted amount: $5
- Alert threshold: 80% (tuc is alert khi vuot $4)
- Email nhan alert: dien email of truong nhom  or ca nhom
- Select Create budget



#### 5.2.2.4 Project Folder Structure
```text
irms/
|-- infrastructure/
|   |-- template-auth.yaml
|   |-- template-api.yaml
|   |-- template-database.yaml
|   |-- template-storage.yaml
|   |-- template-security.yaml
|   `-- template-ai.yaml
|
|-- functions/
|   |-- incident-crud/
|   |   `-- handler.py
|   |
|   |-- upload-evidence/
|   |   `-- handler.py
|   |
|   |-- generate-report/
|   |   `-- handler.py
|   |
|   |-- alert-handler/
|   |   `-- handler.py
|   |
|   `-- ai-assistant/
|       `-- handler.py
|
|-- frontend/
|   `-- React SPA
|
|-- docs/
|   |-- architecture/
|   `-- api-spec.md
|
`-- README.md
```
