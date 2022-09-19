from typing import List
from db.categories import categories
from models.categories import Category, CategoryIn
from .base import BaseRepository

class CategoryRepository(BaseRepository):

    async def get_all(self, limit: int = 10, skip: int = 0) -> List[Category]:
        query = categories.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    
    async def create(self, c: CategoryIn) -> Category:
        category = Category(
            id = 0,
            name = c.name
        )
        values = {**category.dict()}
        values.pop("id", None)
        query = categories.insert().values(**values)
        category.id = await self.database.execute(query=query)
        return category

