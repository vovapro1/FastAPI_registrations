from fastapi import APIRouter, Depends
from sqlalchemy import select, insert

from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from operations.models import operation
from operations.shemas import AddOperation

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get("/")
async def get_specific_operations(opertion_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == opertion_type)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_operations(table: AddOperation, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**table.dict()
    )
    await session.execute(stmt)
    await session.commit()
    return "данные внесены"