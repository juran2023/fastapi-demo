from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "dev"
    database_url: str
    jwt_secret: str

    class Config:
        env_file = ".env"


settings = Settings(_env_file=".env")  # type: ignore[call-arg]
