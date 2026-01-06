from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from service.products import get_products

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(
        content={
            "status": "success",
            "message": "Welcome to the FastAPI E-commerce Application!"
        }
    )

@app.get("/products/{id}")
def get_product(id: int):
    products = ["Mouse", "Keyboard", "Monitor", "CPU"]

    if id < 0 or id >= len(products):
        raise HTTPException(status_code=404, detail="Product not found")

    return JSONResponse(
        content={
            "status": "success",
            "data": {
                "id": id,
                "name": products[id]
            }
        }
    )
