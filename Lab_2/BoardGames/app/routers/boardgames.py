from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID
from app.core.database import get_db
from app.core.exceptions import NotFoundException, BadRequestException
from app.services.boardgame_service import BoardGameService
from app.schemas.boardgame import BoardGameCreate, BoardGameUpdate, BoardGameResponse
from app.schemas.pagination import PaginationParams, PaginatedResponse

router = APIRouter(prefix="/boardgames", tags=["Board Games"])
service = BoardGameService()

@router.get("/", response_model=PaginatedResponse[BoardGameResponse])
def get_all(params: PaginationParams = Depends(), db: Session = Depends(get_db)):
    items, total = service.get_all(db, params)
    return PaginatedResponse.create(
        data=items, 
        total=total, 
        page=params.page, 
        limit=params.limit
    )

@router.get("/{game_id}", response_model=BoardGameResponse)
def get_by_id(game_id: UUID, db: Session = Depends(get_db)):
    try:
        return service.get_by_id(db, game_id)
    except ValueError:
        raise NotFoundException("Board game not found")

@router.post("/", response_model=BoardGameResponse, status_code=status.HTTP_201_CREATED)
def create(game_data: BoardGameCreate, db: Session = Depends(get_db)):
    return service.create(db, game_data)

@router.put("/{game_id}", response_model=BoardGameResponse)
def update(game_id: UUID, game_data: BoardGameUpdate, db: Session = Depends(get_db)):
    try:
        return service.update(db, game_id, game_data)
    except ValueError:
        raise NotFoundException("Board game not found")

@router.patch("/{game_id}", response_model=BoardGameResponse)
def partial_update(game_id: UUID, game_data: BoardGameUpdate, db: Session = Depends(get_db)):
    try:
        return service.update(db, game_id, game_data)
    except ValueError:
        raise NotFoundException("Board game not found")

@router.delete("/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(game_id: UUID, db: Session = Depends(get_db)):
    try:
        service.soft_delete(db, game_id)
        return None
    except ValueError:
        raise NotFoundException("Board game not found")
