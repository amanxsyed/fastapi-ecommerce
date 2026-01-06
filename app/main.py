from fastapi import FastAPI, HTTPException, Query
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



@app.get("/products")
def list_products(name:str =  Query(default=None, min_length=1, max_length=50, description="Filter products by name")):
    products = get_products()
    if name: 
        name_lower = name.strip().lower()
        products = [p for p in  products if name_lower in p.get("name","").lower()]
        
        if not products:
            raise HTTPException(status_code=404, detail=f"No products found matching the given name = {name}")
        
        total = len(products)
        
        return JSONResponse(status_code=200, content={
            "total" : total,
            "items": products
        })
                            
        
        

