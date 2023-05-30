from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import Provide, inject

from app.config.container import Container

from app.api.exceptions.spot import (
    ErrorMessageSpotNotFound,
    ErrorMessageSpotsNotFound
)

from app.model.schema.spot import (
    GetSpotListModel
)

from app.service.spot_service import (
    SpotService
)

router = APIRouter(prefix="/spot", tags=["spot"])

@router.get(
    "",
    # response_model=List[GetSpotListModel],
    # status_code=status.HTTP_200_OK,
    # responses={
    #     status.HTTP_404_NOT_FOUND: {
    #         "model": ErrorMessageSpotsNotFound,
    #     },
    # },
)
@inject
async def get_spots(
    service: SpotService = Depends(Provide[Container.spot_service]),
):
    """Get a list of spots."""
    spots = await service.get_spots()
    return {"data": spots}
