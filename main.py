from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id: str

app = FastAPI()

@app.get('/')
def root():
    return {'massage': 'Hi'}

@app.get('/id/{id}')
def id(id: int):
    return id

@app.get('/e/{id}')
def rr(id: int):
    return id

@app.post('/add')
def add(usr: User):
    if usr.id[0] in ['1','2','3','4','5','6','7','8','9']:
        raise HTTPException(status_code=401,detail='number')
    else:
        return 'ok'