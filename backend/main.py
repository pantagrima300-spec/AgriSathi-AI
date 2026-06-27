from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.crops import router as crop_router

app = FastAPI(
    title="Agri AI Backend",
    description="REST API using FastAPI + Supabase",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "🌾 Agri AI Backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(crop_router)