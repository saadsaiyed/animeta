# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    prompt: str

@app.post("/predict")
def predict(item: Item):
    try:
        # Your model inference logic goes here
        result = {"prediction": "Your prediction logic here", "prompt": item.prompt}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
