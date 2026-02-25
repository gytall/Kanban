"""CRUD operations for users."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext

from app.models import User
from app.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(db: AsyncSession, user: UserCreate):
    """
    Create a new user with hashed password.
    
    Args:
        db: Database session
        user: User creation data
        
    Returns:
        Created user instance
    """
    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_all_users(db: AsyncSession):
    """
    Get all users from the database.
    
    Args:
        db: Database session
        
    Returns:
        List of all users
    """
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, user_id: int):
    """
    Get a user by ID.
    
    Args:
        db: Database session
        user_id: ID of the user to retrieve
        
    Returns:
        User instance if found, None otherwise
    """
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def delete_user(db: AsyncSession, user_id: int):
    """
    Delete a user by ID.
    
    Args:
        db: Database session
        user_id: ID of the user to delete
        
    Returns:
        Deleted user instance if found, None otherwise
    """
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if user:
        await db.delete(user)
        await db.commit()
        return user
    return None