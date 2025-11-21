from fastapi import FastAPI
from src.cat_facts.router import router as external_router

app = FastAPI(title="External API Integration")

app.include_router(external_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to External API Integration!"}
