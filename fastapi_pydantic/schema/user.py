from pydantic import BaseModel


class UserSchema(BaseModel):
    usename: str
    password: str
