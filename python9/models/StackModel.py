from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Posts:
    """Параметры класса"""
    id: int
    title: str
    content: str
    user_id: int


@dataclass
class Users(BaseModel):
    """Параметры класса"""
    id: int
    username: str
    email: str
    password: int


