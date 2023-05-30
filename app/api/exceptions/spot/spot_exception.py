# -*- coding: utf-8 -*-
"""Spot exception"""

class SpotNotFoundError(Exception):
    """SpotNotFoundError is an error that occurs when a spot is not found."""
    message = "The spot you spcecified does not exist."

    def __str__(self):
        return SpotNotFoundError.message


class SpotsNotFoundError(Exception):
    """SpotsNotFoundError is an error that occurs when spots are not found."""
    message = "No spots were found."

    def __str__(self):
        return SpotsNotFoundError.message
