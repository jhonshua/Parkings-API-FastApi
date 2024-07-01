from fastapi import FastAPI

app = FastAPI()

app.title = "Exchange-Rates"
app.version = "2.0.0"




@app.get('/', tags=['home'])
def home():
    data = {
        "nombre": "Juan",
        "edad": 30
    }
    return data






