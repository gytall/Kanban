from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from app.models import Project
from app.schemas import ProjectCreate

async def create_project(db: AsyncSession, project: ProjectCreate, user_id: int):
    new_project = Project(
        name=project.name,
        description=project.description,
        user_id=user_id
    )
    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)
    return new_project

async def get_projects(db: AsyncSession):
    result = await db.execute(select(Project))
    return result.scalars().all()

async def get_project_by_id(db: AsyncSession, project_id: int):
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalars().first()

async def update_project(db: AsyncSession, project_id: int, project: ProjectCreate):
    existing_project = await get_project_by_id(db, project_id)
    if existing_project:
        existing_project.name = project.name
        existing_project.description = project.description
        db.add(existing_project)
        await db.commit()
        await db.refresh(existing_project)
        return existing_project
    return None

async def delete_project(db: AsyncSession, project_id: int):
    project = await get_project_by_id(db, project_id)
    if project:
        await db.execute(delete(Project).where(Project.id == project_id))
        await db.commit()
    return None