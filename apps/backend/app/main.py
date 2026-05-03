from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(router)

temp_items = [
    {
        "id": "1",
        "name": "Apple",
        "description": "Fresh red apple",
        "price": 1.50,
        "created_at": "2026-05-01T10:00:00",
        "expire_at": "2026-05-10T10:00:00"
    },
    {
        "id": "2",
        "name": "Banana",
        "description": "Ripe yellow banana",
        "price": 0.75,
        "created_at": "2026-05-01T10:00:00",
        "expire_at": "2026-05-08T10:00:00"
    },
    {
        "id": "3",
        "name": "Laptop",
        "description": "Gaming laptop 16GB RAM",
        "price": 999.99,
        "created_at": "2026-05-02T09:00:00",
        "expire_at": "2026-12-31T00:00:00"
    },
]


@app.get("/")
def read_root():
    return {"message": "python item webapi is running"}

@app.get("/items")
def read_items():
    return temp_items