# MZ/X 4.5 Fusion³D Core - API Server
# Teljes verzió, bővített endpointokkal

from fastapi import APIRouter
from datetime import datetime
from meta.meta_mind import MetaMind
from reports.report_generator import generate_daily_report

router = APIRouter()

# === ALAP TESZT ENDPOINT ===
@router.get("/")
def index():
    return {
        "system": "MZ/X 4.5 Fusion³D Core API",
        "status": "online",
        "timestamp": datetime.now().isoformat()
    }

# === RENDSZER EGÉSZSÉG ELLENŐRZÉS ===
@router.get("/health")
def health_check():
    return {
        "status": "OK",
        "version": "4.5",
        "uptime": datetime.now().isoformat(),
        "modules": ["MonteCarlo", "HybridBias", "Sentiment", "FusionCore"]
    }

# === AI ÚJRATANÍTÁS (MANUÁLIS TRIGGER) ===
@router.post("/retrain")
def retrain_model():
    mind = MetaMind()
    mind.trigger_retrain()
    return {
        "message": "Újratanítás elindítva",
        "time": datetime.now().strftime("%H:%M:%S"),
        "status": "processing"
    }

# === NAPI RIPORT GENERÁLÁSA ===
@router.get("/report")
def get_report():
    report = generate_daily_report()
    return {
        "timestamp": report["timestamp"],
        "ai_status": report["ai_status"],
        "confidence_avg": report["confidence_avg"],
        "roi_avg": report["roi_avg"],
        "note": report["note"]
    }

# === AI ÁLLAPOT KÉRÉS ===
@router.get("/status")
def ai_status():
    return {
        "ai": "Fusion³D Core",
        "learning": True,
        "mode": "adaptive",
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
