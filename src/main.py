from fastapi import FastAPI
from src.external_api import router as external_router

app = FastAPI(
    title="FastAPI External API Integration",
    description="Example project to fetch cat facts and images from external APIs",
    version="1.0.0",
)

app.include_router(external_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI External API Integration!"}

@app.get("/health")
def health():
    return {"status": "ok"}
