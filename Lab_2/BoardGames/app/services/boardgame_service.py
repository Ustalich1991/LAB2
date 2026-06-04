from sqlalchemy.orm import Session
from uuid import UUID
from app.models.boardgame import BoardGame
from app.repository.boardgame_repo import BoardGameRepository
from app.schemas.boardgame import BoardGameCreate, BoardGameUpdate
from app.schemas.pagination import PaginationParams

class BoardGameService:
    def __init__(self):
        self.repo = BoardGameRepository()

    def get_all(self, db: Session, params: PaginationParams):
        items, total = self.repo.get_all(db, params)
        return items, total

    def get_by_id(self, db: Session, game_id: UUID):
        game = self.repo.get_by_id(db, game_id)
        if not game:
            raise ValueError("Board game not found")
        return game

    def create(self, db: Session, game_data: BoardGameCreate):
        game = BoardGame(**game_data.model_dump())
        return self.repo.create(db, game)

    def update(self, db: Session, game_id: UUID, game_data: BoardGameUpdate):
        game = self.repo.get_by_id(db, game_id)
        if not game:
            raise ValueError("Board game not found")
        
        update_data = game_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(game, key, value)
        
        return self.repo.update(db, game)

    def soft_delete(self, db: Session, game_id: UUID):
        game = self.repo.get_by_id(db, game_id)
        if not game:
            raise ValueError("Board game not found")
        return self.repo.soft_delete(db, game)
