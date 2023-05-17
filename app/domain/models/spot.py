# -*- coding: utf-8 -*-
"""Spot entity"""

from typing import List
from datetime import datetime

class Spot:
    """Spot represents your collection of spots as an entity."""
    def __init__(
        self,
        id: str,
        title: str,
        category: str,
        address: str,
        coordinate: List[float],
        keeped: bool,
        liked: int = 0,
        rate: float = 0,
        distance: float = 0,
        reviews: List[str] = [],
        registed_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ):
        self.id: str = id
        self.title: str = title
        self.category: str = category
        self.address: str = address
        self.coordinate: [float, float] = coordinate
        self.keeped: bool = keeped
        self.liked: int = liked
        self.rate: float = rate
        self.distance: float = distance
        self.reviews: [str] = reviews
        self.registed_at: datetime = registed_at
        self.updated_at: datetime = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Spot):
            return self.id == obj.id
        return False