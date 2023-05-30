from datetime import datetime
from odmantic import Model

from typing import List

class Spot(Model):
    title: str
    category: str
    address: str
    coordinate: List[float]
    keeped: bool
    liked: int
    rate: float
    distance: float
    reviews: List[str]
    registed_at: datetime
    updated_at: datetime
