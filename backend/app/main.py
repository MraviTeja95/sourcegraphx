from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.projects import router as projects_router

app = FastAPI(
    title="SourceGraphX API",
    description="Open-source dependency and impact explorer",
    version="0.1.0",
)

import os

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
    