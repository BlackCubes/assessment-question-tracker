from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Field

from app.database.base import Base


# Shared properties
class UserBase(Base):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    full_name: str | None = Field(default=None, max_length=255)
    is_active: bool = True
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    hashed_password: str


# Properties to return via API
class UserPublic(UserBase):
    id: int
    uuid: UUID
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
