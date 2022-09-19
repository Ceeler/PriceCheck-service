from typing import List
from db.shops import shops
from models.shops import Shop, ShopIn
from .base import BaseRepository

class ShopRepository(BaseRepository):

    async def get_all(self, limit: int = 10, skip: int = 0) -> List[Shop]:
        query = shops.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    
    async def create(self, s: ShopIn) -> Shop:
        shop = Shop(
            id = 0,
            name = s.name,
            link = s.link,
            description = s.description
        )
        values = {**shop.dict()}
        values.pop("id", None)
        query = shops.insert().values(**values)
        shop.id = await self.database.execute(query=query)
        return shop

