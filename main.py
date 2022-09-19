import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List

app = FastAPI()


class Users(BaseModel):
    user_name: str
    user_id: int
    user_email: str
    age: int
    recommendations: List[str]
    ZIP: Union[int, None] = None


users_dict = {}


@app.put('/users')
def create_user(user: Users):
    user = user.dict()
    user_id = user['user_id']
    if user_id in users_dict.keys():
        return {'description': f"Error: El usuario con ID '{user_id}' ya existe."}
    else:
        users_dict[user['user_id']] = user
        return {'description': f'El usuario con ID {user["user_id"]} fue creado exitosamente.'}


@app.post('/users/{user_id}')
def update_user(user_id: int, user: Users):
    if user_id not in users_dict.keys():
        return {'description': f"Error: El usuario con ID '{user_id}' no existe."}
    else:
        user = user.dict()
        users_dict[user['user_id']] = user
        return {'description': f'La información del usuario con ID {user["user_id"]} fue actualizada exitosamente.'}


@app.get('/users/{user_id}')
def get_user(user_id: int):
    if user_id not in users_dict.keys():
        return {'description': f"Error: El usuario con ID '{user_id}' no existe."}
    else:
        return {'user_id': users_dict[user_id]["user_id"],
                'information': users_dict[user_id]}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    if user_id not in users_dict.keys():
        return {'description': f"Error: El usuario con ID '{user_id}' no existe."}
    else:
        users_dict.pop(user_id)
        return {'description': 'Usuario eliminado exitosamente.'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
