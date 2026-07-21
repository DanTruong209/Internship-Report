---
title: "Infrastructure Configuration"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

## 3. Infrastructure Configuration

#### Contents

- 5.3.3 Setup Authentication
- 5.3.4 Setup API Gateway
- 5.3.5 Setup DynamoDB
- 5.3.6 Setup S3 & Storage

### 5.3.3 Setup Authentication (Amazon Cognito)

#### 5.3.3.1 Prepare Before Starting
Open these two things first:
Thu 1 — AWS Console in the browser:
- Open the browser (Chrome/Edge), vao dia chi: https://console.aws.amazon.com
- Sign in with your IAM user
- In the top-right corner, check the selected region — phai is Asia Pacific (Singapore) ap-southeast-1. If it is not correct, click vao ten region → select Asia Pacific (Singapore)
Thu 2 — Terminal on the local machine:
Windows: Nhan phim Windows → go PowerShell → Enter. or open Git Bash if da install Git.
Mac: Nhan Cmd + Space → go Terminal → Enter.
Configure AWS CLI
-Create an access key
-Create a profile, then nhap accsess key and secret key
Verify that AWS CLI is configured correctly with this command:

```bash
aws sts get-caller-identity --profile irms-shared
```

> Expected result: the AWS CLI should return your account ID and user ARN, confirming that the profile is valid and the credentials are active.

```json
{
"UserId": "AIDXXXXXXXXXXXXXXXXX",
"Account": "123456789012",
"Arn": "arn:aws:iam::123456789012:user/your-username"
}
```

#### 5.3.3.2 Create a Cognito User Pool (in the AWS Console)
**Step 1: Tren AWS Console, thanh tim kiem phia tren go Cognito → click Amazon Cognito**
**Step 2: Click nut Create user pool (goc tren ben phai)**
**Step 3: Trang Configure sign-in experience:**
- Authentication providers: select Cognito user pool
- Cognito user pool sign-in options: tich ✅ vao Email
- Click Next
**Step 4: Trang Configure security requirements:**
- Password policy mode: select Custom
- Minimum length: 8
- Tich ✅: Contains at least 1 uppercase, 1 lowercase, 1 number, 1 special character
- Multi-factor authentication: select No MFA (demo not can)
- Click Next
**Step 5: Trang Configure sign-up experience:**
- Keep the default settings tat ca
- Click Next
**Step 6: Trang Configure message delivery:**
- Email provider: select Send email with Cognito (mien phi, du dung for demo)
- Click Next
**Step 7: Trang Integrate your app:**
- User pool name: irms-user-pool
- App client name: irms-web-client
- Client secret: select Don't generate a client secret
- Click Next
**Step 8: Trang Review and create:**
- Scroll down xem lai toan bo
- Click Create user pool
**Step 9: after khi create xong, trang hien ra User Pool moi. Save 2 gia tri nay vao file notepad/txt tren may:**
User Pool ID:  ap-southeast-1_XXXXXXXXX  ← thay o tab "Overview"
Client ID:     XXXXXXXXXXXXXXXXXXXXXXXXXX ← vao tab "App clients" de xem
2 gia tri nay se dung nhieu lan o the step after, save can than.

#### 5.3.3.3 Create Four Groups (RBAC)
Van o trang Cognito User Pool vua create:
**Step 1: Click tab Groups → Click Create group**
**Step 2: Create Group 1:**
Group name:  Admin
Description: Toan quyen system
Precedence:  1
Click Create group
**Step 3: Lap lai, create them 3 group:**
Group name:  SecurityManager
Description: Xem tat ca Incident, phan cong, xem report
Precedence:  2

Group name:  SecurityAnalyst
Description: Dieu tra, upload evidence, cap nhat trang thai
Precedence:  3

Group name:  Auditor
Description: Chi xem, not chinh sua
Precedence:  4
after khi xong, tab Groups phai hien du 4 group nhu after:
Admin            (Precedence: 1)
SecurityManager  (Precedence: 2)
SecurityAnalyst  (Precedence: 3)
Auditor          (Precedence: 4)

> If the console UI differs slightly, the important part is that the four groups exist with the expected precedence order.

#### 5.3.3.4 Create a Test User
Van o trang User Pool, click tab Users → Create user:
User 1 (Admin):
Invitation message:     Don't send an invitation
Email address:          admin@irms-demo.com
Email address verified: tich ✅
Temporary password:     select "Set a password"
Password:               Admin@123456
User must create a new password: bo tich ✅
Click Create user → click vao user vua create → Add user to group → select Admin

Lap lai tuong tu for 3 user con lai, gan vao dung group:
manager@irms-demo.com  → group SecurityManager  → pass: Manager@123456
analyst@irms-demo.com  → group SecurityAnalyst   → pass: Analyst@123456
auditor@irms-demo.com  → group Auditor           → pass: Auditor@123456

> Keep the credentials in a safe note if you plan to test the API later.

#### 5.3.3.5 Verify from the Terminal
Open Terminal tren may, chay lenh after (thay YOUR_CLIENT_ID with Client ID da luu o step 3.2):

```bash
aws cognito-idp initiate-auth \
--auth-flow USER_PASSWORD_AUTH \
--auth-parameters USERNAME=analyst@irms-demo.com,PASSWORD=Analyst@123456 \
--client-id YOUR_CLIENT_ID \
--region ap-southeast-1 \
--profile irms-shared
Expected result — seeing three tokens means success:
```

json
{
"AuthenticationResult": {
"AccessToken": "eyJraWQiOi...",
"IdToken": "eyJraWQiOi...",
"RefreshToken": "eyJjdHki...",
"ExpiresIn": 3600,
"TokenType": "Bearer"
}
}
![Setup Authentication 5](/images/5-Workshop/IRMS/section-03-005.png)
![Setup Authentication 6](/images/5-Workshop/IRMS/section-03-006.png)
![Setup Authentication 7](/images/5-Workshop/IRMS/section-03-007.png)
if thay loi NotAuthorizedException → verify lai password or email.
if thay loi UserNotFoundException → verify lai email da create dung chua.
Verify JWT token:
- Copy toan bo chuoi IdToken (dai, bat dau with eyJ...)
- Open the browser, vao https://jwt.io
- Paste vao o Encoded ben trai
- Ben phai muc Payload phai thay:

```json
{
"email": "analyst@irms-demo.com",
"cognito:groups": ["SecurityAnalyst"],
```

...
}
Thay dung 2 field tren →  Cognito complete.

> This confirms that the user pool is working and that the issued token contains the expected group claims.

### 5.3.4 Setup API Gateway
Luu y ve cach tiep can: nay chi dung Console de hieu co che Cognito Authorizer and test JWT token. Toan bo API routes that (/incidents, /evidence, /reports, /ai) se do SAM tu sinh o 7 khi deploy Lambda — not create tay o day de tranh conflict.

#### 5.3.4.1 Create the REST API
**Step 1: Tren AWS Console, thanh tim kiem go API Gateway → click API Gateway**
**Step 2: Click Create API**
**Step 3: Trang select loai API:**
- Select REST API (not phai REST API Private, not phai HTTP API)
- Click Build
**Step 4: Dien thong tin:**
API details:        New API
API name:           irms-api-learning
Description:        Dung de learn Authorizer, se delete after khi sang 7
API endpoint type:  Regional
Click Create API
⚠ API nay dat ten irms-api-learning de phan biet with API that do SAM create after. after khi test xong Authorizer o nay, API nay has the delete di — not anh huong gi to system.

#### 5.3.4.2 Create a Cognito Authorizer
**Step 1: Menu ben trai → click Authorizers → click Create authorizer**
**Step 2: Dien thong tin:**
Authorizer name:    irms-cognito-authorizer
Authorizer type:    Cognito
Cognito user pool:  select "irms-user-pool"
Token source:       Authorization
Token validation:   (de trong)
Click Create authorizer

#### 5.3.4.3 Create Two Test Routes
Vao Resources o menu ben trai. Muc tieu create 2 route de test ro rang:
GET /ping       → not has Authorizer → luon tra 200
GET /ping-auth  → has Authorizer       → 401 if not has token, 200 if has token
Create /ping (not has Authorizer):
**Step 1: Click vao / (root) → click Create resource**
Resource name:  ping
Resource path:  /ping
CORS:           not tich (de SAM management after)
Click Create resource
**Step 2: Click vao /ping → click Create method**
Method type:        GET
Integration type:   Mock
Click Create method
**Step 3: Vao Integration Response → Mapping Templates → them template:**
Content-Type:   application/json
Template body:
{
"message": "pong",
"auth": false
}
Click Save
**Step 4: Xac nhan /ping not gan Authorizer:**
- Click method GET
- Tab Method request → Authorization: phai is NONE

Create /ping-auth (has Authorizer):
**Step 1: Click vao / (root) → click Create resource**
Resource name:  ping-auth
Resource path:  /ping-auth
CORS:           not tich
Click Create resource
**Step 2: Click vao /ping-auth → click Create method**
Method type:        GET
Integration type:   Mock
Click Create method
**Step 3: Vao Integration Response → Mapping Templates → them template:**
Content-Type:   application/json
Template body:
{
"message": "Authorized",
"auth": true
}
Click Save
**Step 4: Gan Authorizer vao /ping-auth:**
- Click method GET of /ping-auth
- Tab Method request → Authorization → click Edit
- Select irms-cognito-authorizer
- Click Save de luu

#### 5.3.4.4 Deploy the dev Stage
**Step 1: Click Deploy API (goc tren ben phai)**
**Step 2: Cua so Deploy API:**
Stage:       *New stage*
Stage name:  dev
Click Deploy
**Step 3: Trang Stage Editor hien ra → luu Invoke URL:**
Invoke URL: https://ymag7i4369.execute-api.ap-southeast-1.amazonaws.com/dev
⚠ URL nay chi dung de test Authorizer in 4. URL that of system se do SAM create o 7 and has gia tri khac — luc do dung URL of SAM, bo URL nay di.

#### 5.3.4.5 Test with Postman
Install Postman if chua has:
- Vao https://www.postman.com/downloads/
- Download → install dat → open len → select Skip (not can create account)
Lay JWT token from Cognito:
Open Terminal (Windows: PowerShell or Git Bash / Mac: Terminal), chay lenh after (thay YOUR_CLIENT_ID with Client ID da luu o 3):
aws cognito-idp initiate-auth \
--auth-flow USER_PASSWORD_AUTH \
--auth-parameters USERNAME=analyst@irms-demo.com,PASSWORD=Analyst@123456!\
--client-id YOUR_CLIENT_ID \
--region ap-southeast-1 \
--profile irms-shared
![Setup API Gateway 12](/images/5-Workshop/IRMS/section-04-012.png)
Copy toan bo chuoi IdToken (bat dau with eyJ...) vao notepad.

Test 1 — /ping not can token:
Open Postman:
- Method: GET
- URL: https://xxxxxxxxxx.execute-api.ap-southeast-1.amazonaws.com/dev/ping
- not them gi o Headers
- Click Send
Expected result:
{
"message": "pong",
"auth": false
}
![Setup API Gateway 13](/images/5-Workshop/IRMS/section-04-013.png)
Status: 200 OK → ✅ API Gateway hoat dong

Test 2 — /ping-auth not has token:
- Method: GET
- URL: https://xxxxxxxxxx.execute-api.ap-southeast-1.amazonaws.com/dev/ping-auth
- not them gi o Headers
- Click Send
Expected result:
{
"message": "Unauthorized"
}
![Setup API Gateway 14](/images/5-Workshop/IRMS/section-04-014.png)
Status: 401 Unauthorized → ✅ Authorizer dang chan dung

Test 3 — /ping-auth has token:
- Method: GET
- URL: https://xxxxxxxxxx.execute-api.ap-southeast-1.amazonaws.com/dev/ping-auth
- Tab Headers → them:
Key:    Authorization
Value:  Bearer <eyJraWQiOi...>   ← paste IdToken vao day
- Click Send
Expected result:
{
"message": "Authorized",
"auth": true
}
![Setup API Gateway 15](/images/5-Workshop/IRMS/section-04-015.png)
Status: 200 OK → ✅ Authorizer authentication JWT thanh cong

Test 4 — /ping-auth with token sai:
- Giu nguyen setup Test 3 nhung sua token thanh chuoi bat ky:
Authorization: Bearer thisisafaketoken
- Click Send
Expected result:
{
"message": "Unauthorized"
}
![Setup API Gateway 16](/images/5-Workshop/IRMS/section-04-016.png)
Status: 401 Unauthorized → ✅ Authorizer from choi token not hop le

#### 5.3.4.6 Checklist 4
before khi sang 5, xac nhan du the muc after:
- ✅ API Gateway (Regional) da create ten irms-api-learning
- ✅ Cognito Authorizer da create, tro dung vao irms-user-pool
- ✅ GET /ping  → Mock, not has Authorizer
- ✅ GET /ping-auth → Mock, has Cognito Authorizer
- ✅ Da deploy stage dev
- ✅ Test Postman:
/ping          → 200 (not can token)
/ping-auth     → 401 (not has token)
/ping-auth     → 200 (has token hop le)
/ping-auth     → 401 (token sai)
- ✅ Da luu Invoke URL (chi dung tam for nay)

### 5.3.5 Setup DynamoDB

#### 5.3.5.1 Design the Schema Before Creation
before khi vao Console, can hieu ro cau truc data. IRMS dung 4 bang:
Incidents          → luu thong tin incident
Timeline           → luu lich su tung step xu ly
EvidenceMetadata   → luu thong tin file evidence
Users              → luu thong tin user
Chi tiet tung bang:
Bang Incidents:
Partition key:  incidentId (String)
GSI 1:          status-index     → query theo trang thai (Open/Investigating/Closed)
GSI 2:          assignedTo-index → query theo nguoi is phan cong
Attributes:
incidentId      String   "INC-001"
title           String   "SQL Injection Attack"
severity        String   "Critical / High / Medium / Low"
status          String   "Open / Investigating / Containment / Resolved / Closed"
description     String   mo ta chi tiet
assignedTo      String   email nguoi xu ly
createdBy       String   email nguoi create
createdAt       String   ISO timestamp
updatedAt       String   ISO timestamp

Bang Timeline:
Partition key:  incidentId (String)
Sort key:       timestamp  (String)
Attributes:
incidentId   String
timestamp    String   ISO timestamp
action       String   "Created / Assigned / Status Changed / Note Added"
description  String   mo ta hanh dong
performedBy  String   email nguoi thuc hien

Bang EvidenceMetadata:
Partition key:  evidenceId  (String)
GSI 1:          incidentId-index → query evidence theo incident
Attributes:
evidenceId    String   UUID
incidentId    String   "INC-001"
fileName      String   "screenshot.png"
fileType      String   "image/png"
s3Key         String   duong dan in S3
uploadedBy    String   email nguoi upload
uploadedAt    String   ISO timestamp
fileSize      Number   bytes

Bang Users:
Partition key:  email (String)
Attributes:
email         String
fullName      String
role          String   "Admin / SecurityManager / SecurityAnalyst / Auditor"
createdAt     String

#### 5.3.5.2 Create Table Incidents
**Step 1: Tren AWS Console, thanh tim kiem go DynamoDB → click DynamoDB**
**Step 2: Click Create table**
**Step 3: Dien thong tin co ban:**
Table name:           irms-incidents
Partition key:        incidentId    Type: String
Sort key:             (de trong)
**Step 4: Table settings → select Customize settings**
**Step 5: Table class: DynamoDB Standard**
**Step 6: Read/write capacity settings:**
Capacity mode: On-demand
Select On-demand vi demo not has traffic on dinh, chi tra phi theo luot request thuc te — tranh bi tinh phi khi bang not dung.
**Step 7: Encryption: Owned by Amazon DynamoDB (mac dinh, du for demo)**
**Step 8: Click Create table, cho khoang 30 giay to khi Status chuyen sang Active**

#### 5.3.5.3 Create the GSI for the Incidents Table
after khi bang Active, create Global Secondary Index de query nhanh theo status and assignedTo:
**Step 1: Click vao bang irms-incidents → tab Indexes → click Create index**
Create GSI 1 — query theo status:
Partition key:   status      Type: String
Sort key:        createdAt   Type: String
Index name:      status-index
Projected attributes: All
Click Create index → cho Status chuyen sang Active
Create GSI 2 — query theo nguoi is phan cong:
Click Create index lan nua:
Partition key:   assignedTo   Type: String
Sort key:        createdAt    Type: String
Index name:      assignedTo-index
Projected attributes: All
Click Create index → cho Active

#### 5.3.5.4 Create Table Timeline
**Step 1: Click Create table**
**Step 2:**
Table name:      irms-timeline
Partition key:   incidentId    Type: String
Sort key:        timestamp     Type: String
Sort key is timestamp vi in 1 incident has nhieu moc thoi gian, sort key giup automatic sap xep theo thu tu thoi gian.
**Step 3: Table settings → Customize settings → Capacity mode: On-demand**
**Step 4: Click Create table → cho Active**

#### 5.3.5.5 Create Table EvidenceMetadata
**Step 1: Click Create table**
**Step 2:**
Table name:      irms-evidence-metadata
Partition key:   evidenceId    Type: String
Sort key:        (de trong)
**Step 3: Table settings → Customize settings → Capacity mode: On-demand**
**Step 4: Click Create table → cho Active**
**Step 5: Create GSI de query evidence theo incidentId:**
Tab Indexes → Create index:
Partition key:   incidentId    Type: String
Sort key:        uploadedAt    Type: String
Index name:      incidentId-index
Projected attributes: All
Click Create index → cho Active

#### 5.3.5.6 Create Table Users
**Step 1: Click Create table**
**Step 2:**
Table name:      irms-users
Partition key:   email    Type: String
Sort key:        (de trong)
**Step 3: Table settings → Customize settings → Capacity mode: On-demand**
**Step 4: Click Create table → cho Active**

#### 5.3.5.7 Add Sample Data for Testing
after khi create du 4 bang, them vai record mau vao bang Incidents de test Lambda after nay:
**Step 1: Click vao bang irms-incidents → tab Explore items → click Create item**
**Step 2: Select JSON view, paste noi dung after:**
{
"incidentId": { "S": "INC-001" },
"title": { "S": "Public S3 Bucket Detected" },
"severity": { "S": "Critical" },
"status": { "S": "Open" },
"description": { "S": "S3 bucket company-data dang bi public access, has the lo data khach hang" },
"assignedTo": { "S": "analyst@irms-demo.com" },
"createdBy": { "S": "admin@irms-demo.com" },
"createdAt": { "S": "2026-06-01T08:00:00Z" },
"updatedAt": { "S": "2026-06-01T08:00:00Z" }
}
Click Create item
**Step 3: Create them record thu 2:**
{
"incidentId": "INC-002",
"title": "SSH Brute Force Attack",
"severity": "High",
"status": "Investigating",
"description": "Phat hien 500 lan dang enter SSH that bai from IP 203.0.113.42 in 10 phut",
"assignedTo": "analyst@irms-demo.com",
"createdBy": "manager@irms-demo.com",
"createdAt": "2026-06-02T10:30:00Z",
"updatedAt": "2026-06-02T11:00:00Z"
}
Click Create item

#### 5.3.5.8 Verify from the Console
**Step 1: Click vao bang irms-incidents → tab Explore items**
**Step 2: Thay 2 record INC-001 and INC-002 → ✅**
**Step 3: Test query theo GSI:**
- Click Scan/Query → select Query
- Index: select status-index
- Partition key value: Open
- Click Run
- Results phai tra ve INC-001 → ✅ GSI hoat dong dung


#### 5.3.5.9 Hybrid Deployment with AWS SAM
in workshop nay, the bang Amazon DynamoDB is create thu cong with AWS Console o the step before nham giup nguoi learn hieu ro cach thiet ke schema, Partition Key, Sort Key and Global Secondary Index (GSI).
after khi complete phan thuc hanh with Console, du an IRMS chuyen sang mo hinh Hybrid Deployment.
O mo hinh nay:
- Amazon Cognito and Amazon DynamoDB is giu nguyen from the step cau hinh with Console.
- AWS SAM se chi trien khai the thanh phan con lai of system nhu:
- Amazon API Gateway
- AWS Lambda
- Amazon S3
- Amazon SNS
- Amazon EventBridge
- AWS Secrets Manager
Dieu nay giup:
- Tranh create trung the bang DynamoDB.
- Dam bao data mau da create o 5 van is giu nguyen.
- Giup nguoi learn vua hieu cach cau hinh thu cong, vua lam quen with Infrastructure as Code (IaC) with AWS SAM.
the bang DynamoDB is SAM su dung
Thay vi create moi, template AWS SAM se tham chieu truc tiep to the bang da ton tai:

| Table | Purpose |
| --- | --- |
| irms-incidents | Luu thong tin Incident |
| irms-timeline | Luu Timeline xu ly |
| irms-evidence-metadata | Luu metadata Evidence |
| irms-users | Luu thong tin user |

Ten the bang se is truyen vao Lambda thong qua SAM Parameters and Environment Variables, vi vay not can create lai with CloudFormation.
File template su dung
in repository IRMS Source Code, toan bo ha tang is management boi:
infrastructure/template.yaml
Template nay da is cau hinh theo mo hinh Hybrid Deployment, bao gom:
- Su dung Amazon Cognito User Pool da create san.
- Su dung the DynamoDB Tables da create o 5.
- Create moi:
- Amazon API Gateway
- AWS Lambda Functions
- Amazon S3 Buckets
- Amazon SNS
- Amazon EventBridge
- AWS Secrets Manager
Verify Configuration
has the verify template before khi trien khai with lenh:
sam validate ^
  --template-file infrastructure/template.yaml ^
  --region ap-southeast-1
Expected result:
Template provided at 'infrastructure/template.yaml' was successfully validated.

#### 5.3.5.10 Checklist 5
- ✅ Da create thanh cong 4 bang DynamoDB:
- irms-incidents
- irms-timeline
- irms-evidence-metadata
- irms-users
- ✅ Hai Global Secondary Index of bang irms-incidents hoat dong:
- status-index
- assignedTo-index
- ✅ Global Secondary Index of bang irms-evidence-metadata hoat dong:
- incidentId-index
- ✅ Da them 2 ban ghi mau (INC-001, INC-002) vao bang irms-incidents.
- ✅ Da verify truy van thong qua status-index tra ve dung ket qua.
- ✅ Da authentication (sam validate) thanh cong Hybrid SAM Template for giai doan trien khai tiep theo.

### 5.3.6 Setup S3 & Storage

#### 5.3.6.1 Storage Design
IRMS su dung 2 S3 bucket with muc dich hoan toan khac nhau:
irms-frontend-031577240048-ap-southeast-1   → luu React SPA (public qua CloudFront)
irms-evidence-031577240048-ap-southeast-1   → luu file evidence (private, chi Lambda truy cap)
Ly do them Account ID and Region vao ten bucket: S3 bucket name is unique toan cau — dung Account ID + Region dam bao ten luon doc nhat, tranh conflict with nguoi khac.
So sanh 2 bucket:

|  | irms-frontend-... | irms-evidence-... |
| --- | --- | --- |
| Public access | Block (chi CloudFront is doc) | Block hoan toan |
| Ai truy cap | CloudFront | Lambda function |
| Luu gi | HTML, CSS, JS, assets | Screenshot, log, PCAP, PDF report |
| Versioning | not can | Bat (bao ve evidence) |
| CORS | not can | Can (presigned URL upload from browser) |

#### 5.3.6.2 Evidence Upload Flow
Can hieu luong upload file evidence de hieu tai sao Evidence bucket can CORS:
Browser                Lambda                    S3
│                      │                       │
│──POST /evidence──────►│                       │
│  (filename, type)     │                       │
│                       │──GeneratePresignedURL─►│
│                       │◄──presignedUrl─────────│
│◄──presignedUrl────────│                       │
│                       │                       │
│──PUT presignedUrl──────────────────────────────►│
│  (file binary)        │                  file saved
│◄──200 OK──────────────────────────────────────│
│                       │                       │
│──POST /evidence/{id} ►│                      │
│  (evidenceId)         │──PutItem──────────────►DynamoDB
│◄──200 OK──────────────│
Uu diem of Presigned URL: File upload thang from browser len S3, not di qua Lambda — tranh gioi han 6MB payload of Lambda and tiet kiem bandwidth.

#### 5.3.6.3 Verify Configuration S3 in template.yaml
Template da has san in repo — nay chi doc hieu cau hinh, not them resource moi.
Open file infrastructure/template.yaml, tim phan S3 and doc tung thuoc tinh:
Frontend Bucket:
FrontendBucket:
Type: AWS::S3::Bucket
Properties:
BucketName: !Ref FrontendBucketName
`# Block toan bo public access`
`# CloudFront se truy cap qua OAC (setup o phan after)`
PublicAccessBlockConfiguration:
BlockPublicAcls: true
BlockPublicPolicy: true
IgnorePublicAcls: true
RestrictPublicBuckets: true
Nhung diem can luu y:
- BlockPublicAcls: true → not ai is set ACL public for object
- BlockPublicPolicy: true → not ai is create bucket policy for phep public
- not has WebsiteConfiguration vi frontend phan phoi qua CloudFront, not phai S3 static website hosting truc tiep
Evidence Bucket:
EvidenceBucket:
Type: AWS::S3::Bucket
Properties:
BucketName: !Ref EvidenceBucketName
PublicAccessBlockConfiguration:
BlockPublicAcls: true
BlockPublicPolicy: true
IgnorePublicAcls: true
RestrictPublicBuckets: true
`# Versioning ON: bao ve evidence khoi bi delete/ghi de`
VersioningConfiguration:
Status: Enabled
`# CORS: for phep browser PUT file qua Presigned URL`
CorsConfiguration:
CorsRules:
- AllowedHeaders:
- "*"
AllowedMethods:
- PUT
- GET
AllowedOrigins:
- "*"
MaxAge: 3600
Nhung diem can luu y:
- VersioningConfiguration: Enabled → moi lan upload file cung ten se create version moi, not ghi de — quan trong with evidence phap ly
- CorsRules for phep PUT from AllowedOrigins: "*" → browser has the upload thang qua Presigned URL
- MaxAge: 3600 → browser cache CORS preflight response 1 tieng, giam so lan OPTIONS request

#### 5.3.6.4 Verify Parameters in template.yaml
Tim phan Parameters, xac nhan has du 2 bucket name and the gia tri default dung:
Parameters:

`# ── S3 ──────────────────────────────────────────────────────`
FrontendBucketName:
Type: String
Default: irms-frontend-031577240048-ap-southeast-1

EvidenceBucketName:
Type: String
Default: irms-evidence-031577240048-ap-southeast-1
if thay dung 2 ten nay → ✅ tiep tuc.

#### 5.3.6.5 Verify Environment Variables Lambda in template.yaml
Lambda can biet ten Evidence bucket de create Presigned URL. Tim phan Globals xac nhan has:
Globals:
Function:
Environment:
Variables:
EVIDENCE_BUCKET: !Ref EvidenceBucketName
or tung Lambda Upload Evidence has rieng:
UploadEvidenceFunction:
Type: AWS::Serverless::Function
Properties:
Environment:
Variables:
EVIDENCE_BUCKET: !Ref EvidenceBucketName

#### 5.3.6.6 Verify samconfig.toml
Open file infrastructure/samconfig.toml, xac nhan dung cau hinh:
version = 0.1

[default.deploy.parameters]
stack_name          = "irms-dev"
region              = "ap-southeast-1"
confirm_changeset   = false
capabilities        = "CAPABILITY_IAM CAPABILITY_NAMED_IAM"
profile             = "irms-shared"

parameter_overrides = [
"Environment=dev",
"UserPoolId=ap-southeast-1_XXXXXXXXX",
"UserPoolClientId=XXXXXXXXXXXXXXXXXXXXXXXXXX",
"UserPoolArn=arn:aws:cognito-idp:ap-southeast-1:031577240048:userpool/ap-southeast-1_XXXXXXXXX",
"IncidentsTableName=irms-incidents",
"TimelineTableName=irms-timeline",
"EvidenceMetadataTableName=irms-evidence-metadata",
"UsersTableName=irms-users",
"FrontendBucketName=irms-frontend-031577240048-ap-southeast-1",
"EvidenceBucketName=irms-evidence-031577240048-ap-southeast-1"
]
Thay the gia tri XXXXXXXXX with gia tri that da luu o 3.

#### 5.3.6.7 Validate Template
after khi xac nhan du the muc tren, chay lenh validate de verify template not has loi cu phap:
Open Terminal, di chuyen vao thu muc root of repo:
cd irms
Chay validate:
sam validate ^
--template-file infrastructure/template.yaml ^
--region ap-southeast-1
Expected result:
Template provided at 'infrastructure/template.yaml' was successfully validated.

Xu ly loi thuong gap:
if thay:
Error: Template format error: YAML not well-formed
→ Loi cu phap YAML, thuong do indent sai. Open template.yaml verify lai dong is chi ra in notification loi. Moi cap indent phai is 2 spaces, not dung tab.
if thay:
Error: [InvalidResourceException] Resource 'XYZ' not found
→ a resource dang tham chieu to resource chua has in template. Binh thuong if is tham chieu CloudFront/WAF (se them o after), can hoi lai team.

#### 5.3.6.9 Checklist 6
- ✅ Hieu ro muc dich 2 bucket:
irms-frontend-031577240048-ap-southeast-1  → React SPA, qua CloudFront
irms-evidence-031577240048-ap-southeast-1  → file evidence, qua Lambda
- ✅ Hieu luong Presigned URL (Browser → Lambda lay URL → PUT thang len S3)
- ✅ Doc hieu cau hinh FrontendBucket in template.yaml:
BlockPublicAcls, BlockPublicPolicy = true
- ✅ Doc hieu cau hinh EvidenceBucket in template.yaml:
Versioning ON, CORS for PUT
- ✅ Xac nhan Parameters FrontendBucketName and EvidenceBucketName dung ten
- ✅ Xac nhan EVIDENCE_BUCKET has in Environment Variables of Lambda
- ✅ Xac nhan samconfig.toml dung stack_name = "irms-dev"
- ✅ sam validate chay thanh cong
