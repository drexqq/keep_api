from app.config.container import Container
from app.domain.spot.spot_model import SpotListResponse, SpotResponse
from app.domain.spot.spot_schema import CreateSpot
from app.domain.spot.spot_service import SpotService
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/spot", tags=["spot"])

@router.get(
    "/list",
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
    response_description="success",
    responses={
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_404_NOT_FOUND: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
@inject
async def get_spot(
    spot_id: str = "647758918e0c4feb59468229",
    service: SpotService = Depends(Provide[Container.spot_service]),
) -> SpotResponse:
    """Get spot by spot_id"""
    spot = await service.get_spot(id=spot_id)
    return {"data": spot}

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_description="ok",
    responses={
        status.HTTP_400_BAD_REQUEST: {},
        status.HTTP_401_UNAUTHORIZED: {},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
@inject
async def add_spot(
    spot: CreateSpot,
    service: SpotService = Depends(Provide[Container.spot_service]),
) -> SpotResponse:
    """Add Spot"""
    spot = await service.add_spot(spot)
    return {"data": spot}
