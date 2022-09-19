from repositories.items import ItemRepository
from repositories.shops import ShopRepository
from repositories.categories import CategoryRepository
from db.base import database

def get_item_repository() -> ItemRepository:
    return ItemRepository(database)

def get_category_repository() -> CategoryRepository:
    return CategoryRepository(database)

def get_shop_repository() -> ShopRepository:
    return ShopRepository(database)
