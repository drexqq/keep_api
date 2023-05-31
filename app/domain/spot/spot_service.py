from typing import Union

from app.domain.spot.spot_model import Spot
from app.domain.spot.spot_repository import SpotRepository


class SpotService():
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository = spot_repository
    
    async def get_spots(self) -> Union[list[Spot], None]:
        return await self.spot_repository.get_all()

    async def get_spot(self, id: str) -> Union[Spot, None]:
        return await self.spot_repository.get_one(id)
