from fastapi import FastAPI

app = FastAPI()

@app.get("/api/home")
def hello_world():
    return {"message": "Hello World"}