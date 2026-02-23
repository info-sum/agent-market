from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Agent Market Backend"
    env: str = "dev"
    database_url: str = "sqlite:///./agent_market.db"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    cors_origins: str = "*"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
