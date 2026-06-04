from pydantic import BaseModel, Field
from typing import Generic, TypeVar, List

T = TypeVar("T")

class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1, description="Номер страницы")
    limit: int = Field(default=10, ge=1, le=100, description="Кол-во элементов")

class PaginatedResponse(BaseModel, Generic[T]):
    data: List[T]
    meta: dict

    @classmethod
    def create(cls, data: List[T], total: int, page: int, limit: int):
        total_pages = (total + limit - 1) // limit
        return cls(
            data=data,
            meta={"total": total, "page": page, "limit": limit, "total_pages": total_pages}
        )