from app.config.container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from app.domain.spot.spot_model import SpotListResponse, SpotResponse

from app.domain.spot.spot_service import SpotService

router = APIRouter(prefix="/spot", tags=["spot"])

@router.get(
    "s",
    status_code=status.HTTP_200_OK,
    response_description="success",
    responses={
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
@inject
async def get_spots(
    service: SpotService = Depends(Provide[Container.spot_service]),
) -> SpotListResponse:
    """Get list of spots"""
    spots = await service.get_spots()
    return {"data": spots}
    
@router.get(
    "",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
        },
    },
)
@inject
async def get_spot(
    spot_id: str = "64774455d9f3bf3b0002c3d0",
    service: SpotService = Depends(Provide[Container.spot_service]),
) -> SpotResponse:
    """Get spot by spot_id"""
    spot = await service.get_spot(id=spot_id)
    return {"data": spot}
