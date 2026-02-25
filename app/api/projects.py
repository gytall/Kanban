"""API endpoints for project management."""

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


@router.post("/")
async def create_project_view(
    project: ProjectCreate,
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new project.
    
    Args:
        project: Project creation data
        user_id: ID of the user creating the project
        db: Database session
        
    Returns:
        Created project instance
    """
    return await create_project(db, project, user_id)


@router.get("/")
async def get_all_projects(db: AsyncSession = Depends(get_db)):
    """
    Get all projects.
    
    Args:
        db: Database session
        
    Returns:
        List of all projects
    """
    return await get_projects(db)


@router.get("/{project_id}")
async def get_project_view(
    project_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get a project by ID.
    
    Args:
        project_id: ID of the project to retrieve
        db: Database session
        
    Returns:
        Project instance if found, None otherwise
    """
    return await get_project_by_id(db, project_id)


@router.put("/{project_id}")
async def update_project_view(
    project_id: int,
    project: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Update an existing project.
    
    Args:
        project_id: ID of the project to update
        project: Updated project data
        db: Database session
        
    Returns:
        Updated project instance if found, None otherwise
    """
    return await update_project(db, project_id, project)


@router.delete("/{project_id}")
async def delete_project_view(
    project_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a project by ID.
    
    Args:
        project_id: ID of the project to delete
        db: Database session
        
    Returns:
        Deleted project instance if found, None otherwise
    """
    return await delete_project(db, project_id)
