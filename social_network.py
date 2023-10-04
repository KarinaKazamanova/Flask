from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

app = FastAPI()




class UserIn(BaseModel):
    name: str
    email: str
    password: str
    
class User(UserIn):
    id: int
  
users=[User(id=1, name='user1', email='usr1@mail.ru', password=''), 
       User(id=2, name='user2',  email='usr2@mail.ru', password=''),  
       User(id=3, name='user3',  email='usr3@mail.ru', password='')] 

@app.get('/users/', response_class=list[User])
async def root():
   return users

@app.get('/users/{id}')
async def get_user(id: int):
    for user in users:
       if user.id == id:
            return user
       
    raise HTTPException(status_code=404, detail=f'User {id} not found')


@app.post('/users/', response_class=(int, str, str))
async def create_user(user: UserIn):
    new_user_id =  max(list(map(lambda x: x.id, users))) + 1
    new_user = User(id=new_user_id, 
                      name=user.name,
                      email=user.email,
                      password=generate_password_hash(user.password))
    users.append(new_user)
    return new_user.id, new_user.name, new_user.email
    
@app.put('/users/{id}', response_class=User)
async def update_user(id: int, new_user: UserIn):
    for user in users:
        if user.id == id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = generate_password_hash(new_user.password)
            return user
    raise HTTPException(status_code=404, detail=f'User {id} not found')


@app.delete('/users/{id}', response_class=str)
async def delete_task(id: int):
    for user in users:
       if user.id == id:
            # Можно изначально в классе User прописать поле status 
            # и при выполнении запроса на удаление пользователя не удалять данные о человеке, 
            # а ставить флаг True в поле status, таким образом можно оставить возможность пользователю восстановиться 
            # (можно установить период времени, в который такое возможно сделать, 
            # по истечение данного периода уже можно будет непосредственно удалить пользователя)
            users.remove(user)
            return f"User {id} deleted successfully"
    raise HTTPException(status_code=404, detail=f'Task {id} not found')

if __name__ == '__main__':
    uvicorn.run(app='social_network:app', host='127.0.0.1', port=8000, reload=True)