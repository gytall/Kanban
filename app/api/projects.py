from fastapi import APIRouter, Depends
from app.db import AsyncSession, get_db
from app.schemas import ProjectCreate
from app.crud import (
    get_project_by_id, 
    get_projects, 
    update_project, 
    create_project, 
    delete_project
)
router = APIRouter(
	prefix="/projects",
    tags=['projects']
)


@router.delete("/{project_id}")
async def delete_project_view(project_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_project(db, project_id)

@router.get("/")
async def get_all_projects(db: AsyncSession = Depends(get_db)):
    return await get_projects(db)

@router.get("/{project_id}")
async def get_project_view(project_id: int, db: AsyncSession = Depends(get_db)):
    return await get_project_by_id(db, project_id)

@router.put("/{project_id}")
async def update_project_view(project_id: int, project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await update_project(db, project_id, project)


# Project
@router.post("/")
async def create_project_view(project: ProjectCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    return await create_project(db, project, user_id)
