from sqlalchemy.orm import Session
from sqlalchemy import func, select
from typing import Any
from app.schemas.pagination import PaginationParams

def paginate(db: Session, query: Any, params: PaginationParams):
    total = db.scalar(select(func.count()).select_from(query.subquery()))
    if total is None:
        total = 0

    offset = (params.page - 1) * params.limit
    items = db.scalars(query.offset(offset).limit(params.limit)).all()
    
    return items, total