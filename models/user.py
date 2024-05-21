# models/user.py
""" Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User
    Attributes:
        email (string): the email of the use.
        password (string): The password of the user.
        first_name (string): The first name of the user.
        last_name (string): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
