from fastapi import APIRouter, FastAPI, Depends
from typing import List
from repositories.shops import ShopRepository
from endpoints.depends import get_shop_repository
from models.shops import Shop, ShopIn

router = APIRouter()

@router.get("/", response_model=List[Shop])
async def read_items(
    shops: ShopRepository = Depends(get_shop_repository),
    limit: int = 10,
    skip: int = 0):
    return await shops.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Shop)
async def create(
    shop: ShopIn,
    shops: ShopRepository = Depends(get_shop_repository)):
    return await shops.create(s=shop)