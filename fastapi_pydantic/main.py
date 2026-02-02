import requests
from typing import Union
from fastapi import FastAPI, status
from schema.user import UserSchema, UserSchemaResponse
from schema.fox import FoxSchema

userList: list[UserSchema] = [
    UserSchema(username="Miranda", password="123"),
    UserSchema(username="Frida", password="321"),
    UserSchema(username="Tommy", password="abc")
]


app = FastAPI(title="My first API app")


@app.get("/")
def root():
    return {"Hello": "World"}


# item_id is a reference variable
@app.get("/items/{item_id}")  # localhost:8000/items/248?color=black
# define/variates the datatype
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}


# @app.get("/users", response_model=list[UserSchema])
# def getUsers() -> list[UserSchema]:
#     return userList

# filter sensitive information


@app.get("/users", response_model=list[UserSchemaResponse])
def getUsers() -> list[UserSchemaResponse]:
    return userList


@app.post("/users", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def post_user(user: UserSchema) -> UserSchema:  # body
    userList.append(user)
    return user


@app.get("/fox", response_model=FoxSchema)
def get_fox() -> FoxSchema:

    response = requests.get("https://randomfox.ca/floof/")

    result_json = response.json()

    print(f"DEBUGGING{result_json}")

    fox = FoxSchema(**result_json)  # convert json to python object

    return fox
