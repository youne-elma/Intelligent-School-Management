from fastapi import FastAPI
from pydantic import BaseModel
from app.model.request_response import gen_answer


app = FastAPI()


class TextIn(BaseModel):
    text: str

class ListIn(BaseModel):
    list: dict    

class PredictionOut(BaseModel):
    response: dict


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict")
def predict(user_input: TextIn,chat_history:ListIn=None):
    response = gen_answer(user_input.text,chat_history.list)
    
    answer  = response[0]
    chat_history = response[1]
   
    return {"answer": answer,
            "chat history": chat_history}  