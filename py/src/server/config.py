from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Settings(BaseSettings):
    app_name: str = "AlgViso"
    admin_email: str
    items_per_user: int = 50
    cors_allowed_origins = ['*']

    class Config:
        env_file = ".env"


settings = Settings()