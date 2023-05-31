from datetime import datetime

from app.config import configs
from pydantic import BaseModel, Field


class CreateSpot(BaseModel):
    title: str = Field(example="보쌈정식 줜맛")
    category: str = Field(example="식당")
    address: str = Field(example="서울특별시 용산구 한강대로 7길 22-17 1층")
    images: list[str] = Field(example=[])
    comment: str = Field(example="추천글입니다.")
    recommend_spot: str = Field(example="추천 스팟.")
    visit_route: str = Field(example="도보")
    visit_date: datetime = Field(example=datetime.now().strftime(configs.DATETIME_FORMAT))
    coordinate: list[float] = Field(example=[123.4656, 34.12356])
