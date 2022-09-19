from fastapi import APIRouter, FastAPI, Depends
from typing import List
from repositories.items import ItemRepository
from endpoints.depends import get_item_repository
from models.items import Item, ItemIn

router = APIRouter()

@router.get("/", response_model=List[Item])
async def read_items(
    items: ItemRepository = Depends(get_item_repository),
    limit: int = 100,
    skip: int = 0):
    return await items.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Item)
async def create(
    item: ItemIn,
    items: ItemRepository = Depends(get_item_repository)):
    return await items.create(i=item)