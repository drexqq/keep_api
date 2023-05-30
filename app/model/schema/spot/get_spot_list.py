from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field
from app.config import configs
from bson.objectid import ObjectId
class GetSpotListModel(BaseModel):
    id: str = Field(alias="_id", example="vytxeTZskVKR7C7WgdSP3d")
    title: str = Field(example="보쌈정식 줜맛")
    category: str = Field(example="식당")
    address: str = Field(example="서울특별시 용산구 한강대로 7길 22-17 1층")
    coordinate: list[float] = Field(example=[123.4656, 34.12356])
    images: list[str] = Field(example=[""])
    keeped: bool = Field(example=True)
    liked: int = Field(example=0)
    rate: float = Field(example=0)
    distance: float = Field(example=340.5)
    reviews: list[str] = Field(example=["review1","review2"])
    registed_at: datetime = Field(example=datetime.now().strftime(configs.DATETIME_FORMAT))
    updated_at: datetime = Field(example=datetime.now().strftime(configs.DATETIME_FORMAT))
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
