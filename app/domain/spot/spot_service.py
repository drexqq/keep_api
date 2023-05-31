from datetime import datetime
from typing import Union

from app.config import configs
from app.domain.spot.spot_model import Spot
from app.domain.spot.spot_repository import SpotRepository
from app.domain.spot.spot_schema import CreateSpot
from fastapi import HTTPException

from app.util.object_validator import ObjectValidator


class SpotService():
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository = spot_repository
    
    async def get_spots(self) -> Union[list[Spot], list]:
        return await self.spot_repository.get_all() or []

    async def get_spot(self, id: str) -> Spot:
        spot = await self.spot_repository.get_one(id)
        if spot == None:
            raise HTTPException(status_code=404, detail="Spot Not found")
        return spot

    async def add_spot(self, data: CreateSpot) -> Spot:
        spot = Spot(
            title=data.title,
            category=data.category,
            address=data.address,
            images=data.images,
            comment=data.comment,
            recommend_spot=data.recommend_spot,
            reviews=[],
            visit_route=data.visit_route,
            visit_date=data.visit_date,
            coordinate=data.coordinate,
            liked=0,
            rate=0,
            created_at=datetime.now().strftime(configs.DATETIME_FORMAT),
            updated_at=datetime.now().strftime(configs.DATETIME_FORMAT),
        )
        ret = ObjectValidator.validate(data)
        if ret != True:
            raise HTTPException(status_code=422, detail=f"`{ret[0]}` must not be empty")

        return await self.spot_repository.create(spot)
