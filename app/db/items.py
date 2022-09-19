import sqlalchemy
from .base import metadata
import datetime

items = sqlalchemy.Table(
    "items", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("category_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('categories.id'), nullable=False),
    sqlalchemy.Column("shop_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('shops.id'), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Integer),
    sqlalchemy.Column("model_name", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)
