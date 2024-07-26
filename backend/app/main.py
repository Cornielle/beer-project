from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import order

app = FastAPI()

# Set all CORS enabled origins
origins = [
    "http://localhost:3000",  # React frontend
    "http://localhost:8000",
    "http://your-frontend-domain.com",  # Add your frontend domain here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order.router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the beer order API"}
