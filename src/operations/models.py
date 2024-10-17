
from sqlalchemy import TIMESTAMP, Column, Integer, MetaData, String, Table


metadata = MetaData()


operation = Table(
    "operations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quanti", String, nullable=False),
    Column("figi", String, nullable=False),
    Column("instrumental_type", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String, ),
)


