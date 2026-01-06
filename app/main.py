from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(
        content={
            "status": "success",
            "message": "Welcome to the FastAPI E-commerce Application!"
        }
    )
