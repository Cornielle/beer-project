from datetime import datetime
from typing import List
from app.models.models import Stock, Order, Item, Round
from app.exceptions.exceptions import InvalidItemNameException

class OrderRepository:
    def __init__(self):
        self.stock = Stock(
            last_updated=datetime.now(),
            beers=[
                {"name": "Corona", "price": 115, "quantity": 2},
                {"name": "Quilmes", "price": 120, "quantity": 0},
                {"name": "Club Colombia", "price": 110, "quantity": 3}
            ]
        )
        self.order = Order(
            created=datetime.now(),
            paid=False,
            subtotal=0,
            taxes=0,
            discounts=0,
            items=[],
            rounds=[]
        )

    def get_order(self) -> Order:
        return self.order

    def add_round(self, round_items: List[Item]):

        valid_beers = [beer.name for beer in self.stock.beers]
        for item in round_items:
            if item.name not in valid_beers:
                raise InvalidItemNameException(item.name)
            else:
                round = Round(
                    created=datetime.now(),
                    items=round_items
                )
                self.order.rounds.append(round)
                self.order.items.append(item.name)
                self.update_order_totals()

    def update_order_totals(self):
        subtotal = 0
        quantity = 0
        for round in self.order.rounds:
            for item in round.items:
                beer = next((beer for beer in self.stock.beers if beer.name == item.name), None)
                if beer:
                    subtotal += beer.price * item.quantity
        self.order.subtotal = subtotal
        self.order.taxes = subtotal * 0.10  
        self.order.discounts = 0 

order_repository = OrderRepository()
