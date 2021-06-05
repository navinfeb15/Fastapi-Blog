from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit = 5, published: bool= True, sort: Optional[str] = None):
    if published: 
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}

@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def show(id: int):
    return {'data':[id,id+1,id+2]}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def creating_blog(material: Blog):
    return {'data': f'Blog is created of title{material.title} '}


