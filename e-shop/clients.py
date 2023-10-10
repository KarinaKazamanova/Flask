from fastapi import APIRouter, HTTPException
from db import clients, database
from typing import List
from models import Client, ClientIn
from werkzeug.security import generate_password_hash, check_password_hash


router = APIRouter()



@router.get("/clients/", response_model=List[Client])
async def all_clients():
    query = clients.select()
    return await database.fetch_all(query)

@router.post("/clients/",response_model=Client)
async def create_client(client: ClientIn):
    query = clients.insert().values(name=client.name,
                                    surname=client.surname,
                                    email=client.email,
                                    password=generate_password_hash(client.password))
    last_record_id = await database.execute(query)
    return {**client.dict(), "id": last_record_id}

@router.get("/clients/{client_id}", response_model=Client)
async def read_client(client_id: int):
    query = clients.select().where(clients.c.id == client_id)
    try:
        return await database.fetch_one(query)
    except:
        raise HTTPException(status_code=404, detail=f'Client {client_id} not found')

@router.put("/clients/{client_id}", response_model=Client)
async def update_client(client_id: int, new_client: ClientIn):
    query = \
        clients.\
        update().\
        where(clients.c.id == client_id).\
        values(name=new_client.name,
               surname=new_client.surname,
               email=new_client.email,
               password=generate_password_hash(new_client.password))
    try:
        await database.fetch_one(query)
        return {**new_client.dict(), "id": client_id}
    except:
        raise HTTPException(status_code=404, detail=f'Client {client_id} not found')
    

@router.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    query = clients.delete().where(clients.c.id == client_id)
    try:
        await database.fetch_one(query)
        return {"message": "Client deleted"}
    except:
        raise HTTPException(status_code=404, detail=f'Client {client_id} not found')
    
