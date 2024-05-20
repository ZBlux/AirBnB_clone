#!/usr/bin/python3
""" Defines the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city

    Attributes:
        state_id (string): The state id
        name (string): name of the city
    """

    state_id = ""
    name = ""
