from typing import Union
from fastapi import FastAPI

app = FastAPI(title="My first API app")


@app.get("/")
def root():
    return {"Hello": "World"}


# item_id is a reference variable
@app.get("/items/{item_id}")  # localhost:8000/items/248?color=black
# define/variates the datatype
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}
