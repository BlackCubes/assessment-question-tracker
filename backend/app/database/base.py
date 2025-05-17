from datetime import datetime
from typing import Optional
from uuid import UUID
from uuid import uuid4

from sqlalchemy.sql.schema import Column
from sqlmodel import FetchedValue
from sqlmodel import Field
from sqlmodel import Integer
from sqlmodel import SQLModel
from sqlmodel import text
from sqlmodel import TIMESTAMP


class Base(SQLModel):
    id: int = Field(
        sa_column=Column(
            Integer,
            autoincrement="auto",
            primary_key=True,
            default=1,
            unique=True,
        )
    )
    uuid: UUID = Field(default_factory=uuid4, primary_key=False)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            server_onupdate=FetchedValue(),
        ),
    )
