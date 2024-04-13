from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from uuid import uuid4

app = FastAPI()

# Хранилище данных
products_db: Dict[str, Dict[str, str]] = {}


class Product(BaseModel):
    name: str
    description: str = None
    price: float


@app.post("/products", status_code=201)
async def create_product(product: Product):
    product_id = str(uuid4())
    products_db[product_id] = product.dict()
    return JSONResponse(status_code=201, content={"id": product_id})


@app.get("/products/{product_id}")
async def read_product(product_id: str):
    if product_id in products_db:
        return products_db[product_id]
    else:
        return JSONResponse(status_code=404, content={"error": "Product not found"})


@app.get("/products_download")
async def download_products():
    return JSONResponse(content=products_db)
