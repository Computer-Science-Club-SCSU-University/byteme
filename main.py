from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
from bytemeUtil.utils import pipeline
import json


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the specific origins allowed to access the API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/utils")
async def main():    
    file_path = "bytemeUtil/Degree audit.txt"

    with open(file_path, 'r') as file:
        text = file.readlines()

    data = json.loads(pipeline(text))
    return data



if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", port=80, log_level="debug", reload="True")