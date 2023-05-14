#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.

    Attributes:
        name
    """
    name = ""
