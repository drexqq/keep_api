from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.config import configs

class GetSpotListModel(BaseModel):
    """GetSpotListModel represents data structure as a get model."""
    id: str = Field(example="vytxeTZskVKR7C7WgdSP3d")
    title: str = Field(example="보쌈정식 줜맛")
    category: str = Field(example="식당")
    address: str = Field(example="서울특별시 용산구 한강대로 7길 22-17 1층")
    coordinate: List[float] = Field(example=[123.4656, 34.12356])
    keeped: bool = Field(example=True)
    liked: int = Field(example=0)
    rate: float = Field(example=0)
    distance: float = Field(example=340.5)
    reviews: List[str] = Field(example=["vytxeTZskVKR7C7WgdSP3d","vytxeTZskVKR7C7WgdSP3d"])
    registed_at: str = Field(example=datetime.now().strftime(configs.DATETIME_FORMAT))
    updated_at: str = Field(example=datetime.now().strftime(configs.DATETIME_FORMAT))
