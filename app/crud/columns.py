from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from passlib.context import CryptContext

from app.models import BoardColumn
from app.schemas import BoardColumnCreate

async def create_board_column(db: AsyncSession, column: BoardColumnCreate, project_id: int):
    new_column = BoardColumn(
        name=column.name,
        project_id=project_id
    )
    db.add(new_column)
    await db.commit()
    await db.refresh(new_column)
    return new_column

async def get_columns_by_project(db: AsyncSession, project_id: int):
    result = await db.execute(select(BoardColumn).where(BoardColumn.project_id == project_id))
    return result.scalars().all()

async def get_column_by_id(db: AsyncSession, column_id: int):
    result = await db.execute(select(BoardColumn).where(BoardColumn.id == column_id))
    return result.scalars().first()

async def update_column(db: AsyncSession, column_id: int, column: BoardColumnCreate):
    existing_column = await get_column_by_id(db, column_id)
    if existing_column:
        existing_column.name = column.name
        db.add(existing_column)
        await db.commit()
        await db.refresh(existing_column)
        return existing_column
    return None

async def delete_column(db: AsyncSession, column_id: int):
    column = await get_column_by_id(db, column_id)
    if column:
        await db.delete(column)
        await db.commit()
        return column
    return None
