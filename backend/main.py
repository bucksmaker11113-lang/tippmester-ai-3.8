# ===========================================
#  MZ/X 4.5.1 Fusion³D Core - main.py
#  Fő indítófájl (API + AI + AutoReport)
# ===========================================

import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.logger import logger
from utils.config_loader import config
from ai.fusion_core import FusionCore
from reports.auto_reporter import AutoReporter
from api.server import router as api_router


# === FastAPI inicializálás ===
app = FastAPI(
    title="MZ/X 4.5.1 Fusion³D Core API",
    description="AI Fusion Engine, MetaMind, és AutoReport háttérmotor.",
    version="4.5.1"
)

# === CORS beállítások ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === AI motor inicializálása ===
fusion_core = FusionCore()


@app.on_event("startup")
async def startup_event():
    """Alkalmazás indításkor fut le."""
    logger.success("MZ/X 4.5.1 Fusion³D Core elindult ✅")

    # Háttértanulási ciklus (FusionCore)
    asyncio.create_task(fusion_core.background_learning())

    # Automatikus riport ütemezés (AutoReporter)
    if config.get("AUTO_REPORT_ENABLED", True):
        AutoReporter()
    else:
        logger.warn("Automatikus riportküldés letiltva konfiguráció alapján.")


@app.get("/")
async def root():
    """Egyszerű root endpoint a státusz ellenőrzéshez."""
    return {
        "status": "running",
        "version": config.get("VERSION", "4.5.1"),
        "auto_report": config.get("AUTO_REPORT_ENABLED", True),
        "report_hour": config.get("REPORT_HOUR", 22),
        "message": "MZ/X Fusion³D Core működik 🚀"
    }


# === API router betöltése ===
app.include_router(api_router)


# === Lokális futtatás (fejlesztéshez) ===
if __name__ == "__main__":
    import uvicorn
    logger.info("Lokális indítás: http://127.0.0.1:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
