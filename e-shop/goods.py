from fastapi import APIRouter, HTTPException
from db import goods, database
from typing import List
from models import Item, ItemIn



router = APIRouter()



@router.get("/goods/", response_model=List[Item])
async def all_goods():
    query = goods.select()
    return await database.fetch_all(query)

@router.post("/goods/",response_model=Item)
async def create_item(item: ItemIn):
    query = goods.insert().values(name=item.name,
                                    description=item.description,
                                    price=item.price,
                                    )
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}

@router.get("/goods/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = goods.select().where(goods.c.id == item_id)
    try:
        return await database.fetch_one(query)
    except:
        raise HTTPException(status_code=404, detail=f'Item {item_id} not found')

@router.put("/goods/{item_id}", response_model=Item)
async def update_item(item_id: int, new_item: ItemIn):
    query = \
        goods.\
        update().\
        where(goods.c.id == item_id).\
        values(name=new_item.name,
               description=new_item.description,
               price=new_item.price,
               )
    try:
        await database.fetch_one(query)
        return {**new_item.dict(), "id": item_id}
    except:
        raise HTTPException(status_code=404, detail=f'Item {item_id} not found')
    

@router.delete("/goods/{item_id}")
async def delete_item(item_id: int):
    query = goods.delete().where(goods.c.id == item_id)
    try:
        await database.fetch_one(query)
        return {"message": "Item deleted"}
    except:
        raise HTTPException(status_code=404, detail=f'Item {item_id} not found')
    
        