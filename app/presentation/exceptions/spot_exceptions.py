from pydantic import BaseModel, Field

from app.domain.exceptions import (
    SpotNotFoundError,
    SpotsNotFoundError,
)

class ErrorMessageSpotNotFound(BaseModel):
    detail: str = Field(example=SpotNotFoundError.message)

class ErrorMessageSpotsNotFound(BaseModel):
    detail: str = Field(example=SpotsNotFoundError.message)
