from pydantic import BaseModel

class CardRequest(BaseModel):
    title: str
    type: str
    position: int
    url: str