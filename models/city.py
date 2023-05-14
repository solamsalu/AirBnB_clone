#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
