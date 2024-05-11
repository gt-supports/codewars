from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

class create_user(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }
@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return { 'message': f'Hello {name}'}

@app.post("/users/")
def create_user(user: create_user):
    return {
        "message": "succes",
        "email": user.email,
    }

@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a":a,
        "b": b,
        "result": a+b,
    }



@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]

@app.get('/items/latest/')
def return_latest_item():
    return {'item': {'id':'0', 'name': 'latest'}}

@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id": item_id + 3,
        },
    }




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)





