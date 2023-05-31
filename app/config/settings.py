import os

import pydantic
from bson.objectid import ObjectId
from dotenv import load_dotenv
from pydantic import BaseSettings

# pydantic ObjectId setting
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

load_dotenv()

ENV: str
class Configs(BaseSettings):
    # base
    ENV: str = os.getenv("ENV", "dev")
    PROJECT_NAME: str = "Keep-api"

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # database
    DB_ENGINE: str = os.getenv("DB_ENGINE", "mongodb+srv")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_SETTING: str = os.getenv("DB_SETTING")

    DATABASE_URI = "{db_engine}://{user}:{password}@{host}/{setting}".format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        setting=DB_SETTING,
    )

configs = Configs()
