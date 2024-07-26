import pytest
from datetime import datetime
from app.repositories.order_repository import OrderRepository
from app.models.models import Item

@pytest.fixture
def repository():
    return OrderRepository()


def test_add_round(repository):
    items = [Item(name="Corona", quantity=2)]
    
    repository.add_round(round_items=items)
    updated_order = repository.get_order()
    
    assert len(updated_order.rounds) == 1
    assert updated_order.rounds[0].items[0].name == "Corona"
    assert updated_order.rounds[0].items[0].quantity == 2
