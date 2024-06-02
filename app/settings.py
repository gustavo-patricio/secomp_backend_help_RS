from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".enviroments", env_file_encoding="utf-8")

    PROJECT_NAME: str 
    USER_PROFILE: str
    DATABASE_URL: str = Field(description="Url do Banco de Dados")
    ACESS_TOKEN_EXPIRE: int = Field(description="tempo de validade do token")
    SECRET_KEY: str = Field(description="chave secreta da api")
    

