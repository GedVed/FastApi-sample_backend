from pydantic import BaseModel
import datetime
from enum import Enum

class Blog_Post(BaseModel):
    author: str
    title: str
    text: str
    timestamp = datetime.now()

class Category(Enum):
    WELLNESS = "wellness"
    LIFESTYLE = "lifestyle"
    DIY = "diy"