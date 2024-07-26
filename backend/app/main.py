from fastapi import FastAPI
from app.api.v1 import order

app = FastAPI()

app.include_router(order.router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the beer order API"}
