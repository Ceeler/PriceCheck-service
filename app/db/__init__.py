from .items import items
from .categories import categories
from .shops import shops
from .base import metadata, engine

metadata.create_all(bind=engine)

