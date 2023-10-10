from fastapi import FastAPI
import sqlalchemy
from db import database
import databases



import clients
# import orders
import goods


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
@app.get("/")
async def home():
    return {"Home": "Home"}
    
    
app.include_router(goods.router, tags=["goods"])

app.include_router(orders.router, tags=["orders"])

app.include_router(clients.router, tags=["clients"])

