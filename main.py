from fastapi import FastAPI
from routes import router

app = FastAPI(title="AI Banking Fraud Detection API")

app.include_router(router)

@app.get("/")
def home():
    return {"message":"AI Banking API Running"}
