# 🛡️ FraudShield AI — Real-Time Explainable AI Fraud Detection System

FraudShield AI is an enterprise-grade, full-stack fraud detection and risk monitoring system powered by Explainable AI (XAI). It combines supervised machine learning (XGBoost) and unsupervised anomaly detection (Isolation Forest) with SHAP tree attributions, real-time behavioral feature engineering, and an interactive analyst dashboard built with Next.js.

The entire application is architected to deploy as a **single Vercel project** under one public URL (e.g. `https://fraudshield.vercel.app`), serving both the Next.js frontend and the Python FastAPI API seamlessly without separate backend hosting.

---

## 🚀 Key Features

- **Single Vercel Project Architecture**: Frontend and Python Serverless API deployed together under a single domain.
- **Hybrid AI Detection Architecture**: Combines supervised $P(\text{Fraud})$ (XGBoost) with unsupervised anomaly scoring (Isolation Forest) and behavioral velocity rules into a composite 0–100 risk score.
- **Explainable AI (XAI) & SHAP Attributions**: Computes feature attributions using SHAP and presents human-readable reason strings (e.g., *"Transaction amount is 4.2x above customer baseline"*).
- **Real-Time Behavioral Feature Engineering**: Computes rolling velocity counters (10m, 1h, 24h), z-scores against customer baseline profiles, location anomalies, time-of-day risks, and device switches.
- **Interactive Analyst Dashboard**: Built with Next.js App Router for real-time monitoring, transaction inspection, alert triaging, and metric visualization.
- **Analyst Feedback Loop**: Enables fraud analysts to confirm alerts or mark false positives to refine decision rules without corrupting historical data.

---

## 🏗️ Deployment Architecture

```text
                            Vercel (Single Deployment)
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             │                                                     │
      Frontend UI                                          Python Serverless API
     (Next.js App)                                         (Vercel Function)
             │                                                     │
  app/, components/, lib/                                    api/index.py
             │                                                     │
             └──────────────────────────┬──────────────────────────┘
                                        │
                             backend/app/ (FastAPI)
                                        │
                               ┌────────┴────────┐
                               │                 │
                           ML Models          Database
                        (joblib / sklearn)  (PostgreSQL / SQLite)
```

---

## 🛠️ Tech Stack

### **Backend & API**
- **Framework**: FastAPI (Python 3.11+) exposed via Vercel Python Serverless Functions (`api/index.py`).
- **ML / AI**: XGBoost, Scikit-Learn (Isolation Forest), SHAP, Pandas, NumPy, Joblib.
- **Database**: PostgreSQL (Production) / SQLite (`/tmp/` for serverless demo).
- **Testing**: Pytest, HTTPX.

### **Frontend**
- **Framework**: Next.js 16 (App Router), React 19, TypeScript.
- **Styling**: Tailwind CSS, Base UI, Lucide Icons.
- **Package Manager**: npm / pnpm.

---

## 📁 Repository Structure

```text
FraudShield-RiskEngine/
├── app/                       # Next.js App Router Pages & Layouts
├── components/                # React UI Components
├── lib/                       # API Utility & Type Definitions
├── public/                    # Static Assets
├── api/                       # Vercel Serverless Function Entrypoint
│   └── index.py               # Python Serverless Handler exporting FastAPI app
├── backend/                   # Python Core Engine
│   ├── app/                   # FastAPI Endpoints, Database & Services
│   ├── data/                  # Sample Training Data
│   └── trained_models/        # XGBoost & Isolation Forest Joblib Models
├── package.json               # Next.js & Frontend Dependencies
├── next.config.mjs            # Next.js Config with Local Dev Rewrite Proxy
├── vercel.json                # Vercel Routing Configuration
├── requirements.txt           # Consolidated Python Dependencies
├── .env.example               # Environment Variables Template
├── .gitignore                 # Git Ignore Configuration
└── README.md                  # Documentation
```

---

## ⚙️ Local Development Setup

### 1. Prerequisites
- **Node.js**: 18+ (Node 20+ recommended)
- **Python**: 3.11+

### 2. Install Dependencies

```bash
# 1. Install Node.js frontend dependencies
npm install

# 2. Install Python dependencies
pip install -r requirements.txt
```

### 3. Run Application Locally

Option A: **Full-Stack Development (Recommended)**

Run backend FastAPI server:
```bash
python -m backend.app.main
```

In a second terminal, run Next.js dev server:
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). Next.js automatically proxies `/api/*` calls to `http://127.0.0.1:8000/api/*`.

---

## 🌐 Deploying to Vercel (Single Deployment)

To deploy the entire application (Frontend + FastAPI Backend) under **ONE public Vercel URL**:

1. Push your repository to **GitHub**.
2. Go to [Vercel Dashboard](https://vercel.com/new) and click **Import Repository**.
3. Select your repository.
4. **Vercel Project Settings**:
   - **Framework Preset**: Next.js (detected automatically)
   - **Root Directory**: `./` (leave default as repository root)
5. **Environment Variables**:
   - `DATABASE_URL`: Hosted PostgreSQL connection string (e.g. Neon, Supabase, or Vercel Postgres).
   - *(If `DATABASE_URL` is omitted, Vercel will automatically run a transient SQLite database in `/tmp/fraudshield.db`)*.
6. Click **Deploy**.

After deployment, your application is live at:
```text
https://fraudshield.vercel.app
```
and API endpoints are accessible on the same domain at:
```text
https://fraudshield.vercel.app/api/health
https://fraudshield.vercel.app/api/predict
https://fraudshield.vercel.app/api/transactions
https://fraudshield.vercel.app/api/alerts
https://fraudshield.vercel.app/api/metrics
```

---

## 📡 REST API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | System health check (DB connection & ML model status) |
| `POST` | `/api/predict` | Evaluate risk score & XAI explanation for transaction |
| `GET` | `/api/transactions` | Fetch processed transactions |
| `GET` | `/api/alerts` | Retrieve flagged transactions needing analyst review |
| `POST` | `/api/feedback` | Submit analyst feedback (confirm fraud / mark legitimate) |
| `GET` | `/api/customers/{id}` | Customer baseline profile & transaction history |
| `GET` | `/api/metrics` | System aggregated fraud statistics & model performance |

---

## 🧪 Testing & Verification

```bash
# Run pytest backend test suite
pytest backend/tests/

# Verify end-to-end prediction pipeline
python backend/verify_end_to_end.py
```
