from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get('/blog')
def index(limit: int, authenticated: bool = False):
    
    if authenticated:    
        if limit > 1:
            payload =  {
                "data" : f"Here is {limit} blogs"
            }
        else:
            payload =  {
                "data" : f"Here is the {limit} blog requested."
            }
        return payload
    else:
        return "Please get authenticated first!"

@app.get('/blog/unpublished')
def unpublished():
    payload = {
        "data" : {
            "unpublished_blogs" : [{"title" : "upb 1"}]
        }
    }
    return payload

@app.get('/blog/{id}')
def show(id: int):
    payload = {
        "data" : id
    }
    return payload


@app.get('/blog/{id}/comments')
def comments(id):
    payload = {
        "data": {
            "1"
        }
    }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    
    payload = {
        "data" : {
            "message" : f"{request.title} created!",
            "status" : 201
        }
    }
    
    return payload
    