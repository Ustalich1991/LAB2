from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from uuid import UUID
from app.models.boardgame import BoardGame
from app.schemas.pagination import PaginationParams
from app.utils.pagination import paginate

class BoardGameRepository:
    
    def get_all(self, db: Session, params: PaginationParams):
        query = select(BoardGame).where(BoardGame.deleted_at.is_(None))
        return paginate(db, query, params)
        
    def get_by_id(self, db: Session, game_id: UUID):
        stmt = select(BoardGame).where(
            and_(BoardGame.id == game_id, BoardGame.deleted_at.is_(None))
        )
        return db.scalar(stmt)

    def create(self, db: Session, game: BoardGame):
        db.add(game)
        db.commit()
        db.refresh(game)
        return game

    def update(self, db: Session, game: BoardGame):
        db.commit()
        db.refresh(game)
        return game

    def soft_delete(self, db: Session, game: BoardGame):
        game.soft_delete()
        db.commit()
        return game