# API FastAPI pour le moteur Trail Video Geolocation
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .geolocator import geolocate_video

app = FastAPI(
    title="Trail Video Geolocation API",
    description="Moteur de Géolocalisation & Suivi de Trajectoire Vidéo",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec carte de trajectoire
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Trail API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Trail", "version": "1.0.0"}

@app.get("/api/v1/geolocate", response_model=ResultContract)
def get_geolocate(video_path: str = Query("parcours_drone.mp4")):
    return geolocate_video(video_path)
