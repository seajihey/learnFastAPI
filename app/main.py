from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str,None]=None
    price: float
    
    
@app.get("/")
async def read_root():
    return "이건 메인페이지입니다 여기에 메인.html경로 넣으면 되는거쥬?"
@app.get("/이건경로/")
async def root():
    return "경로연습"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,  None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}