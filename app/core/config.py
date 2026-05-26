from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    POKEAPI_URL: str
    REDIS_URL: str = "redis://redis:6379"
    API_KEY: str

    model_config = SettingsConfigDict(
        env_file = '.env'
    )

settings = Settings()
