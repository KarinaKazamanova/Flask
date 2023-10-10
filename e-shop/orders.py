from fastapi import APIRouter, HTTPException
from db import orders, database, clients, goods
from typing import List
from models import Order, OrderIn, Client


router = APIRouter()



@router.get("/orders/", response_model=List[Order])
async def all_orders():
    query = orders.select()
    list_of_orders = await database.fetch_all(query)
    orders_dict = dict()
    for order in list_of_orders:
        orders_dict[order.id] = {
            "client": clients.select(clients.c.name).where(clients.c.id == order.client_id),
            "item": goods.select(goods.c.name).where(goods.c.id == order.item_id),
            "created_at": order.created_at,
            "status": order.status,            
        }
    return orders_dict
        

@router.post("/orderss/",response_model=Order)
async def create_order(order: OrderIn):
    query = clients.insert().values(client_id=order.client_id,
                                    item_id=order.item_id,
                                    created_at=order.created_at,
                                    status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}

@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    try:
        return await database.fetch_one(query)
    except:
        raise HTTPException(status_code=404, detail=f'Order {order_id} not found')

@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = \
        orders.\
        update().\
        where(orders.c.id == order_id).\
        values(client_id=new_order.client_id,
               item_id=new_order.item_id,
               status=new_order.status,
        )
    try:
        await database.fetch_one(query)
        return {**new_order.dict(), "id": order_id}
    except:
        raise HTTPException(status_code=404, detail=f'Order {order_id} not found')
    

@router.delete("/orders/{order_id}")
async def delete_client(order_id: int):
    query =orders.delete().where(orders.c.id == order_id)
    try:
        await database.fetch_one(query)
        return {"message": "Client deleted"}
    except:
        raise HTTPException(status_code=404, detail=f'Order {order_id} not found')
    
        