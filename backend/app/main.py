from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import Base
from .api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sentinel AI",
    version="1.0.0"
)

# 👇 ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Sentinel AI Backend Running 🚀"
    }