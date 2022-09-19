
from typing import Optional
from pydantic import BaseModel


class Shop(BaseModel):
    id: Optional[int] = None
    name: str
    link: str
    description: str

class ShopIn(BaseModel):
    name: str
    link: str
    description: str