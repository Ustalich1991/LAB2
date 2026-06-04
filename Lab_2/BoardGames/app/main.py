from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.routers.boardgames import router as boardgames_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BoardGames API - Лабораторная №2",
    description="REST API для настольных игр с Soft Delete и пагинацией",
    version="1.0.0"
)

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# роутеры
app.include_router(boardgames_router)

@app.get("/")
def root():
    return {
        "message": "BoardGames API работает!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)
