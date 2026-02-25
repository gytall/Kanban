"""CRUD operations for projects."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from app.models import Project
from app.schemas import ProjectCreate


async def create_project(
    db: AsyncSession,
    project: ProjectCreate,
    user_id: int
):
    """
    Create a new project.
    
    Args:
        db: Database session
        project: Project creation data
        user_id: ID of the user creating the project
        
    Returns:
        Created project instance
    """
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
    """
    Get all projects from the database.
    
    Args:
        db: Database session
        
    Returns:
        List of all projects
    """
    result = await db.execute(select(Project))
    return result.scalars().all()


async def get_project_by_id(db: AsyncSession, project_id: int):
    """
    Get a project by ID.
    
    Args:
        db: Database session
        project_id: ID of the project to retrieve
        
    Returns:
        Project instance if found, None otherwise
    """
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalars().first()


async def update_project(
    db: AsyncSession,
    project_id: int,
    project: ProjectCreate
):
    """
    Update an existing project.
    
    Args:
        db: Database session
        project_id: ID of the project to update
        project: Updated project data
        
    Returns:
        Updated project instance if found, None otherwise
    """
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
    """
    Delete a project by ID.
    
    Args:
        db: Database session
        project_id: ID of the project to delete
        
    Returns:
        None
    """
    project = await get_project_by_id(db, project_id)
    if project:
        await db.execute(delete(Project).where(Project.id == project_id))
        await db.commit()
    return None