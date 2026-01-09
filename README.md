# 🇸🇳 SND AI Digital Twin

Assistant conversationnel intelligent représentant le Sénégal, basé sur des données factuelles institutionnelles et propulsé par l’IA générative via AWS Bedrock.

---

## 🎯 Objectif du projet

Ce projet vise à créer un **jumeau numérique conversationnel du Sénégal**, capable de :
- fournir des informations fiables et structurées (démographie, institutions, économie),
- répondre de manière professionnelle, neutre et pédagogique,
- démontrer l’intégration d’une IA générative dans une architecture cloud serverless.

---

## 🧠 Fonctionnalités principales

- 💬 Chat conversationnel temps réel
- 🏛️ Réponses institutionnelles et factuelles
- 🧩 Mémoire de conversation (locale ou S3)
- ☁️ Backend serverless (AWS Lambda)
- 🤖 IA générative via **AWS Bedrock (Amazon Nova)**
- 🌍 Frontend moderne avec **Next.js**

---

## 🏗️ Architecture
Frontend (Next.js)  
⬇️  
Backend API (FastAPI – AWS Lambda)  
⬇️  
AWS Bedrock (Amazon Nova)

---

## 🛠️ Technologies utilisées

### Backend
- Python 3
- FastAPI
- AWS Lambda
- AWS Bedrock (Amazon Nova)
- boto3
- Mangum
- pypdf

### Frontend
- Next.js (React)
- TypeScript

### Cloud & DevOps
- AWS IAM
- Serverless Architecture
- Git & GitHub

---

## ⚙️ Configuration (Backend)

### Variables d’environnement

```env
DEFAULT_AWS_REGION=eu-west-3
BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
USE_S3=false

