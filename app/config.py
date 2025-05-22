from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

# Load .env.local (if present) to override defaults for local dev
load_dotenv(find_dotenv(".env.local", raise_error_if_not_found=False))
# Load .env (optional fallback)
load_dotenv(find_dotenv(".env", raise_error_if_not_found=False))

class Settings(BaseSettings):
    environment: str = "PRODUCTION"
    db_link: str

    class Config:
        env_file = ".env"  # fallback in case not loaded manually
        env_file_encoding = "utf-8"

# Create a singleton settings object
settings = Settings()
