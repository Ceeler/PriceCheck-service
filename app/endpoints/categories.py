from fastapi import APIRouter, FastAPI, Depends
from typing import List
from repositories.categories import CategoryRepository
from endpoints.depends import get_category_repository
from models.categories import Category, CategoryIn

router = APIRouter()

@router.get("/", response_model=List[Category])
async def read_items(
    categories: CategoryRepository = Depends(get_category_repository),
    limit: int = 10,
    skip: int = 0):
    return await categories.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Category)
async def create(
    category: CategoryIn,
    categories: CategoryRepository = Depends(get_category_repository)):
    return await categories.create(c=category)