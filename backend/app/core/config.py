from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Agent Market Backend"
    env: str = "dev"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/agent_market"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
