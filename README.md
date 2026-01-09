# 🇸🇳 SND AI Digital "Stratégie nationale de Développement (SND) et de la Vision Sénégal 2050"

Assistant conversationnel intelligent représentant le Sénégal, basé sur des données factuelles institutionnelles et propulsé par l’IA générative via AWS Bedrock.

---

## 🎯 Objectif du projet

Ce projet a pour objectif de concevoir un jumeau numérique conversationnel du Sénégal, non officiel, destiné à faciliter la compréhension de la Stratégie Nationale de Développement (SND).
Il permet de:
- diffuser des informations factuelles, fiables et structurées (démographie, institutions, économie),
- répondre avec un ton professionnel, neutre et pédagogique,,
- illustrer l’intégration d’une IA générative au sein d’une architecture cloud serverless moderne.
  
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

