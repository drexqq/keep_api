from typing import Annotated, List
from fastapi import APIRouter, Path, Depends, status
from dependency_injector.wiring import Provide, inject
from app.config.container import Container

from app.api.exceptions.spot import (
    ErrorMessageSpotNotFound,
    ErrorMessageSpotsNotFound
)

from app.service.spot_service import (
    SpotService
)

router = APIRouter(prefix="/spot", tags=["spot"])

@router.get(
    "s",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageSpotsNotFound,
        },
    },
)
@inject
async def get_spots(
    service: SpotService = Depends(Provide[Container.spot_service]),
):
    """Get list of spots"""
    print("Get list of spots")
    spots = await service.get_spots()
    return {"data" : spots}
    
@router.get(
    "",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageSpotNotFound,
        },
    },
)
@inject
async def get_spot(
    # spot_id: Annotated[str, Path(title="The ID of spot to get")],
    spot_id: str,
    service: SpotService = Depends(Provide[Container.spot_service]),
):
    """Get spot by id"""
    print("Get spot by id")
    spot = await service.get_spot(id=spot_id)
    return {"data": spot}
