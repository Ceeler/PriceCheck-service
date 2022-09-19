from re import I
from typing import List
from db.items import items
from models.items import Item, ItemIn
from .base import BaseRepository
import datetime

class ItemRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Item]:
        query = items.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)


    async def get_by_filter(self, shop_id: int, category_id: int,limit: int = 100, skip: int = 0) -> List[Item]:
        return

    async def get_by_model(self, model_name: str) -> Item:
        query = items.select().where(items.c.model == model_name).first()
        item = await self.database.fetch_one(query)
        if item == None:
            return None
        return item
    
    async def create(self, i: ItemIn) -> Item:
        item = Item(
            id = 0,
            title = i.title,
            description = i.description,
            price = i.price,
            model_name = i.model_name,
            category_id = i.category_id,
            shop_id = i.shop_id,
            created_at =  datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow()
        )
        values = {**item.dict()}
        values.pop("id", None)
        query = items.insert().values(**values)
        item.id = await self.database.execute(query=query)
        return item

    
    async def update(self, id: int, i: ItemIn) -> Item:

        item = Item(
            id = id,
            title = i.title,
            description = i.description,
            price = i.price,
            model_name = i.model_name,
            category_id = i.category_id,
            shop_id = i.shop_id,
            created_at =  datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow()
        )
        values = {**item.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = items.update().where(items.c.id==id).values(**values)
        await self.database.execute(query)
        return item


