# 🏦 Bank Customer Churn Prediction — MLOps

An end-to-end Machine Learning system predicting bank customer churn using a Neural Network (MLP). Built with **FastAPI + Streamlit** and deployed to production.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-MLP-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7)

## 🌐 Live Demo

| Component | URL |
|-----------|-----|
| 🖥️ Web App | [bank-churn.streamlit.app](https://bank-churn-prediction-mlops-7c2dhjpsofl2n2n5kamqp4.streamlit.app/) |
| ⚙️ REST API | [bank-churn-predictions-mlops.onrender.com](https://bank-churn-predictions-mlops.onrender.com) |
| 📖 API Docs | [/docs](https://bank-churn-predictions-mlops.onrender.com/docs) |

## 🏗️ System Architecture

```Raw Bank Customer Data (10,000 rows)
↓
Data Cleaning & EDA
(One-hot encoding, feature analysis)
↓
Neural Network (MLP)
(85% accuracy, optimized for churn recall)
↓
FastAPI REST API  ←→  Streamlit Web App
(Render)               (Streamlit Cloud)```

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Overall Accuracy | 85% |
| Churn Recall | 43% |
| Architecture | MLP (64→32→16→1) |
| Optimizer | Adam |
| Key finding | German customers churn 2x more |

## 🔍 Key Business Insights

- 🇩🇪 **German customers** churn at 32% vs 16% for France/Spain
- 👩 **Female customers** churn more (25% vs 16%)
- 👴 **Age 40-60** is highest risk group
- 💤 **Inactive members** are most likely to churn
- 💰 **Higher balance** paradoxically leads to more churn

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| ML | Scikit-learn (MLP), Pandas, NumPy |
| API | FastAPI, Uvicorn, Pydantic |
| Frontend | Streamlit |
| API Hosting | Render |
| Frontend Hosting | Streamlit Cloud |
| Version Control | Git + GitHub |

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/SahilDogra23/Bank-Churn-Prediction-MLOps.git
cd Bank-Churn-Prediction-MLOps
pip install -r requirements.txt
```

### 2. Start the API
```bash
uvicorn app:app --reload
```

### 3. Start the frontend (new terminal)
```bash
streamlit run streamlit_app.py
```
## 🐳 Docker Deployment

### Run complete app with Docker Compose
```bash
docker-compose up
```
- API runs at `http://127.0.0.1:8002/docs`
- Frontend runs at `http://127.0.0.1:8503`

### Pull from Docker Hub
```bash
docker pull sahil2323dogra/bank-churn-api:v1
docker run -p 8000:8000 sahil2323dogra/bank-churn-api:v1
```

## 📁 Project Structure

```Bank_Churn_Prediction/
├── data/
│   └── Churn_Modelling.csv
├── notebooks/
│   └── bank_churn.ipynb
├── models/
│   ├── bank_churn_mlp.pkl
│   ├── bank_churn_scaler.pkl
│   └── bank_churn_features.pkl
├── app.py
├── streamlit_app.py
├── requirements.txt
└── README.md```

## 📚 Reference
- Dataset: [Bank Customer Churn — Kaggle](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)

## 👤 Author
**Sahil Dogra**
[![GitHub](https://img.shields.io/badge/GitHub-SahilDogra23-black)](https://github.com/SahilDogra23)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-sahildogra23-blue)](https://www.linkedin.com/in/sahildogra23)