from pydantic import BaseModel, Field
from datetime import datetime

class ClientIn(BaseModel):
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    email: str = Field(..., max_length=128) #Нужно ли устанавливать максимальную длину, если она установлена в таблице?
    password: str = Field(..., max_length=512)
    
class Client(BaseModel):
    id: int
    name: str = Field(..., max_length=64)
    surname: str = Field(..., max_length=64)
    email: str = Field(..., max_length=128)
    
    

class ItemIn(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=2)
    price: float
    
class Item(BaseModel):
    id: int
    name: str = Field(..., max_length=64)
    description: str = Field(..., max_length=64)
    price: float
    
    

class OrderIn(BaseModel):
    client_id: int
    item_id: int
    created_at: datetime = Field(..., format="%Y-%m-%d", default=datetime.now)
    status: str = Field(..., min_length=2, default='in_order')
    
class Order(BaseModel):
    id: int
    status: str = Field(..., max_length=16)