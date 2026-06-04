from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str = "postgres"
    DB_PORT: int = 5432
    APP_PORT: int = 4200

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
