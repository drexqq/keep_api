from contextlib import AbstractContextManager
from typing import Callable
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

class SpotRepository():
    def __init__(
        self,
        client: Callable[..., AbstractContextManager[AsyncIOMotorClient]],
        engine: Callable[..., AbstractContextManager[AIOEngine]],
        ) -> None:
        self.client = client
        self.engine = engine

    def get_all(self):
        return "HI"
        
