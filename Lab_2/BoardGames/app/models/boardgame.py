from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.core.database import Base

class BoardGame(Base):
    __tablename__ = "boardgames"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(String(1000))
    publisher = Column(String(150))
    year = Column(Integer)
    min_players = Column(Integer)
    max_players = Column(Integer)
    play_time_minutes = Column(Integer)
    difficulty = Column(String(20))

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)   

    def soft_delete(self):
        self.deleted_at = func.now()
