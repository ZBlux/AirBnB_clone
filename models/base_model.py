#!/usr/bin/python3
""" BaseModel for AirBnB project. """

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid())
        self.created_at = self.updated_at = datetime.now()
