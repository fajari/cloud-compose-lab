import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Compose LAB OK"}