# 🛡️ FraudShield AI — Real-Time Explainable AI Fraud Detection System

FraudShield AI is an enterprise-grade, full-stack fraud detection and risk monitoring system powered by Explainable AI (XAI). It combines supervised machine learning (XGBoost) and unsupervised anomaly detection (Isolation Forest) with SHAP tree attributions, real-time behavioral feature engineering, and an interactive analyst dashboard built with Next.js.

---

## 🚀 Key Features

- **Hybrid AI Detection Architecture**: Combines supervised $P(\text{Fraud})$ (XGBoost) with unsupervised anomaly scoring (Isolation Forest) and behavioral velocity rules into a composite 0–100 risk score.
- **Explainable AI (XAI) & SHAP Attributions**: Computes feature attributions using SHAP and presents human-readable reason strings (e.g., *"Transaction amount is 4.2x above customer baseline"*).
- **Real-Time Behavioral Feature Engineering**: Computes rolling velocity counters (10m, 1h, 24h), z-scores against customer baseline profiles, location anomalies, time-of-day risks, and device switches.
- **Interactive Analyst Dashboard**: Built with Next.js and Tailwind CSS for real-time monitoring, transaction inspection, alert triaging, and metric visualization.
- **Analyst Feedback Loop**: Enables fraud analysts to confirm alerts or mark false positives to refine decision rules without corrupting historical data.
- **Streaming Transaction Simulator**: Built-in simulator to generate streaming transaction traffic for continuous testing.

---

## 🏗️ Architecture Overview

```
                          ┌──────────────────────────┐
                          │    Next.js Frontend      │
                          │   Analyst Dashboard      │
                          └─────────────┬────────────┘
                                        │ REST API
                                        ▼
                          ┌──────────────────────────┐
                          │     FastAPI Backend      │
                          └─────────────┬────────────┘
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             ▼                          ▼                          ▼
 ┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────────────┐
 │   Behavioral Engine   │  │    XGBoost Model      │  │   Isolation Forest    │
 │ (Velocity, Z-Scores)  │  │  (Supervised Prob)    │  │ (Unsupervised Anomaly)│
 └───────────┬───────────┘  └───────────┬───────────┘  └───────────┬───────────┘
             │                          │                          │
             └──────────────────────────┼──────────────────────────┘
                                        ▼
                          ┌──────────────────────────┐
                          │    Hybrid Risk Engine    │
                          │     (0–100 Risk Score)   │
                          └─────────────┬────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │     SHAP Explainer       │
                          │ (Human Reason Strings)   │
                          └──────────────────────────┘
```

---

## 🛠️ Tech Stack

### **Backend**
- **Framework**: FastAPI (Python 3.11+)
- **ML / AI**: XGBoost, Scikit-Learn (Isolation Forest), SHAP, Pandas, NumPy
- **Database**: SQLite / SQLAlchemy ORM
- **Testing & Validation**: Pytest, HTTPX

### **Frontend**
- **Framework**: Next.js 16 (App Router), React 19, TypeScript
- **Styling**: Tailwind CSS, Base UI, Lucide Icons
- **Package Manager**: pnpm / npm

---

## 📁 Repository Structure

```
FraudShield-RiskEngine/
├── backend/
│   ├── app/
│   │   ├── api/                   # FastAPI Endpoints (Predict, Alerts, Feedback, etc.)
│   │   ├── database/              # DB Configuration & Seeder
│   │   ├── models/                # SQLAlchemy Models & Pydantic Schemas
│   │   ├── services/              # ML Models, Risk Engine & Feature Engineering
│   │   └── main.py                # FastAPI Application Entrypoint
│   ├── trained_models/            # Serialized XGBoost, Isolation Forest & Scaler
│   ├── train_models.py            # Model Training & Artifact Generation Script
│   ├── simulate_transactions.py   # Real-Time Transaction Generator
│   ├── verify_end_to_end.py       # End-to-End Pipeline Verification Script
│   └── requirements.txt           # Python Dependencies
├── frontend/
│   ├── app/                       # Next.js Pages & App Router
│   ├── components/                # UI Components & Dashboard Modules
│   └── package.json               # Frontend Dependencies & Scripts
└── README.md                      # Project Documentation
```

---

## ⚙️ Quick Start & Installation

### 1. Prerequisites
- **Python**: 3.11+
- **Node.js**: 18+ (Node 20+ recommended)

---

### 2. Backend Setup

1. **Navigate to the backend folder**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train / Prepare ML Models**:
   ```bash
   python train_models.py
   ```

4. **Run Backend Server**:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   - **Swagger Docs**: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)
   - **ReDoc Spec**: [http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)

---

### 3. Frontend Setup

1. **Navigate to the frontend folder**:
   ```bash
   cd frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   # or
   pnpm install
   ```

3. **Run Development Server**:
   ```bash
   npm run dev
   # or
   pnpm dev
   ```
   - **Dashboard**: [http://localhost:3000](http://localhost:3000)

---

## 📡 Key REST API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/predict` | Evaluate risk score & XAI explanation for incoming transaction |
| `GET` | `/api/transactions` | Fetch paginated list of processed transactions |
| `GET` | `/api/alerts` | Retrieve flagged transactions requiring analyst triage |
| `POST` | `/api/feedback` | Submit analyst feedback (confirm fraud / false positive) |
| `GET` | `/api/customers/{id}` | Fetch customer baseline profile & transaction history |
| `GET` | `/api/metrics` | Get system aggregated fraud statistics & model performance |
| `GET` | `/api/health` | Service health check |

---

## 🧪 Testing & Verification

- **Run Automated Test Suite**:
  ```bash
  cd backend
  pytest
  ```

- **Run End-to-End Verification**:
  ```bash
  cd backend
  python verify_end_to_end.py
  ```

- **Stream Simulated Transactions**:
  ```bash
  cd backend
  python simulate_transactions.py
  ```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
