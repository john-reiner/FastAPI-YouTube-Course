from fastapi import FastAPI
from datetime import date

app = FastAPI()


@app.get('/')
def index():
    payload =  {
        "data" : {
            "name" : "John Reiner"
        }
    }
    
    # return f"Hello "+ payload['data']['name'] +"!"
    return payload

@app.get('/about')
def about():
    today = date.today()
    payload = {
        "data" : {
            "name" : "John Reiner",
            "created" : "2022-01-05",
            "today's date" : "Today's date: " + str(today)
        }
    }
    return payload

