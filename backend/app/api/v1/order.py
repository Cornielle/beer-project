from fastapi import APIRouter, HTTPException
from typing import List
from app.models.models import Item
from app.services.order_service import order_service
from app.exceptions.exceptions import InvalidItemNameException

router = APIRouter()

@router.get("/order/status")
async def get_order_status():
    return order_service.get_order_status()

@router.post("/order/add-round")
async def add_round(items: List[Item]):
    try:
        order_service.add_round(items)
        return {"message": "Round added successfully"}
    except InvalidItemNameException as e:
        detail = f'The element "{e}" is not part of the stock'
        print(detail, "detail")
        raise HTTPException(status_code=400, detail=detail)
