from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_level: str | int = "INFO"
