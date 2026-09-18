import os
from pydantic_settings import BaseSettings
from typing import List

def get_db_url() -> str:
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        if db_url.startswith("postgres://"):
            return db_url.replace("postgres://", "postgresql://", 1)
        return db_url
    # If running inside Vercel serverless lambda environment with no external DB URL
    if os.getenv("VERCEL"):
        return "sqlite:////tmp/fraudshield.db"
    return "sqlite:///./fraudshield.db"

class Settings(BaseSettings):
    PROJECT_NAME: str = "FraudShield AI Backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database
    DATABASE_URL: str = get_db_url()
    
    # CORS — Never use "*" with allow_credentials=True; list explicit origins only
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "https://*.vercel.app",
    ]
    
    # Model settings — config.py is at backend/app/config.py, so go up one level to backend/
    MODELS_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "trained_models"))
    XGBOOST_MODEL_PATH: str = os.path.join(MODELS_DIR, "xgboost_model.joblib")
    ISOLATION_FOREST_PATH: str = os.path.join(MODELS_DIR, "isolation_forest.joblib")
    SCALER_PATH: str = os.path.join(MODELS_DIR, "scaler.joblib")
    METRICS_PATH: str = os.path.join(MODELS_DIR, "metrics.json")

    
    # Risk Engine Weights
    XGB_WEIGHT: float = 0.60
    IFOREST_WEIGHT: float = 0.40
    
    # Risk Thresholds
    LOW_THRESHOLD: float = 39.0
    MEDIUM_THRESHOLD: float = 69.0
    
    class Config:
        case_sensitive = True

settings = Settings()
