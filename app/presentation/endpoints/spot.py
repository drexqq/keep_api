from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import Provide, inject

from app.config.container import Container

from app.presentation.exceptions import (
    ErrorMessageSpotNotFound,
    ErrorMessageSpotsNotFound
)

from app.presentation.models import (
    GetSpotModel
)

from app.domain.services import (
    SpotService
)

router = APIRouter(prefix="/spot", tags=["spot"])

@router.get(
    "",
    # response_model=List[GetSpotModel],
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
    service.get_spots()
    return {"asdasd":"asldkjaslkj"}
