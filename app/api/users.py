"""API endpoints for user management."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.crud import (
    create_user,
    get_user_by_id,
    get_all_users,
    delete_user,
)
from app.schemas import (
    UserCreate,
    UserOut
)

router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.post("/")
async def create_user_view(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new user.
    
    Args:
        user: User creation data
        db: Database session
        
    Returns:
        Created user instance
    """
    return await create_user(db, user)


@router.get("/")
async def get_all_users_view(db: AsyncSession = Depends(get_db)):
    """
    Get all users.
    
    Args:
        db: Database session
        
    Returns:
        List of all users
    """
    users = await get_all_users(db)
    return users


@router.get("/{user_id}", response_model=UserOut)
async def get_user_view(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Get a user by ID.
    
    Args:
        user_id: ID of the user to retrieve
        db: Database session
        
    Returns:
        User instance if found
        
    Raises:
        HTTPException: If user is not found
    """
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found."
        )
    return user


@router.delete("/{user_id}")
async def delete_user_view(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a user by ID.
    
    Args:
        user_id: ID of the user to delete
        db: Database session
        
    Returns:
        Deleted user instance if found, None otherwise
    """
    result = await delete_user(db, user_id)
    return result
