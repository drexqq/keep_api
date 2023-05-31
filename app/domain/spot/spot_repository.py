from contextlib import AbstractContextManager
from typing import Callable, Union

from app.domain.spot.spot_model import Spot
from bson.objectid import ObjectId
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

    async def get_all(self) -> Union[list[Spot], list]:
        return await self.engine.find(Spot, sort=Spot.created_at, limit=10)

    async def get_one(self, id) -> Union[Spot, None]:
        return await self.engine.find_one(Spot, Spot.id == ObjectId(id))
        
