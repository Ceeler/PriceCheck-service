import sqlalchemy
from .base import metadata

shops = sqlalchemy.Table(
    "shops", 
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("link", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String)
)