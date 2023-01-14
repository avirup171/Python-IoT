from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

#Base model
class Data(BaseModel):
    data: dict

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/{user_name}")
async def username(user_name):
    return({"user_name":user_name})

@app.get("/contact-details")
async def contactDetails(id:int = 0, email:str = "abc@abc.com"):
    return({
        "id":id,
        "email":email
    })

@app.post("/post-details")
async def postDetails(requestData: Data):
    requestDataJson=json.loads(requestData.json())
    requestDataJson["processed"]=True
    return (requestDataJson)
