from typing import Optional
from unicodedata import category, name
from pydantic import BaseModel
import datetime

class Item(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    price: int
    model_name: str
    category_id: int
    shop_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ItemIn(BaseModel):
    title: str
    description: str
    price: int
    model_name: str
    category_id: int
    shop_id: int
    