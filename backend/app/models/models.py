from datetime import datetime
from typing import List
from pydantic import BaseModel
import uuid

class Beer(BaseModel):
    name: str
    price: int
    quantity: int

class Stock(BaseModel):
    last_updated: datetime
    beers: List[Beer]

class Item(BaseModel):
    name: str
    quantity: int

class Round(BaseModel):
    id: str = str(uuid.uuid4())
    created: datetime
    items: List[Item]

class Order(BaseModel):
    created: datetime
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[Item]
    rounds: List[Round]

