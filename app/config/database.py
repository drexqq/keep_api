import logging
from logging import config
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from app.config import configs
from app.util.singleton import singleton

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@singleton
class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(configs.DATABASE_URI)
        self.engine = AIOEngine(client=self.client, database="keep")
        logger.info("DB Connect success")
    
    def close(self):
        logger.info("DB Close success")
        self.client.close()
