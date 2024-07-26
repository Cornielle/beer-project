from typing import List
from app.models.models import Item, Order
from app.repositories.order_repository import order_repository

class OrderService:
    def get_order_status(self) -> Order:
        return order_repository.get_order()

    def add_round(self, items: List[Item]):
        order_repository.add_round(items)

order_service = OrderService()
