# -*- coding: utf-8 -*-
"""User entity"""

from typing import List
from datetime import datetime

class User:
    """User represents your collection of users as an entity."""
    def __init__(
        self,
        id: str,
        name: str,
        token: str,
        registed_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ):
        self.id: str = id
        self.name: str = name
        self.token: str = token
        self.registed_at: datetime = registed_at
        self.updated_at: datetime = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, User):
            return self.id == obj.id
        return False