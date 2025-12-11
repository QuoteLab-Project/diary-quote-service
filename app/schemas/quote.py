from pydantic import BaseModel

class QuoteOut(BaseModel):
    id: int
    content: str
    author: str

    model_config = {"from_attributes": True}