from pydantic import BaseModel

# schema must match API data structure


class FoxSchema(BaseModel):
    image: str
    link: str
