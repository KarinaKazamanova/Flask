from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    
    DATABASE_URL="sqlite:///shopdatabase.db"

    class Config:
        env_file = '.env'


settings = Settings()