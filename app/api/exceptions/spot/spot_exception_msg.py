# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field

from app.api.exceptions.spot.spot_exception import SpotNotFoundError, SpotsNotFoundError

class ErrorMessageSpotNotFound(BaseModel):
    detail: str = Field(example=SpotNotFoundError.message)

class ErrorMessageSpotsNotFound(BaseModel):
    detail: str = Field(example=SpotsNotFoundError.message)