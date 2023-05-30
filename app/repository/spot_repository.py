from contextlib import AbstractContextManager
from typing import Callable
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.model.domain.spot import Spot
from bson.objectid import ObjectId

class SpotRepository():
    def __init__(
        self,
        client: Callable[..., AbstractContextManager[AsyncIOMotorClient]],
        engine: Callable[..., AbstractContextManager[AIOEngine]],
        ) -> None:
        self.client = client
        self.engine = engine

    async def get_all(self):
        return await self.engine.find(Spot, sort=Spot.registed_at, limit=10)

    async def get_one(self, id):
        return await self.engine.find_one(Spot, Spot.id == ObjectId(id))
        
