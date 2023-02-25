from fastapi import FastAPI
from worker.process import _get_users, _get_user

app = FastAPI()


@app.get("/", status_code=200)
async def health_check():
    return {"message": "HealthCheck Success"}


@app.get("/users", status_code=200)
async def get_users():
    return {"users": _get_users()}


@app.get("/user/{username}", status_code=200)
async def get_user(username):
    return {"users": _get_user(username)}
