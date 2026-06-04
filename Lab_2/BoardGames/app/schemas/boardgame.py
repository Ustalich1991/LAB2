from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from typing import Optional

class BoardGameBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    publisher: Optional[str] = Field(None, max_length=150)
    year: Optional[int] = Field(None, ge=1900, le=2030)
    min_players: Optional[int] = Field(None, ge=1)
    max_players: Optional[int] = None
    play_time_minutes: Optional[int] = Field(None, ge=1)
    difficulty: Optional[str] = Field(None, pattern="^(easy|medium|hard)$")

class BoardGameCreate(BoardGameBase):
    pass

class BoardGameUpdate(BoardGameBase):
    pass

class BoardGameResponse(BoardGameBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
