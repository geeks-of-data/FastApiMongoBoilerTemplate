from fastapi import FastAPI
from worker.process import _get_users, _get_user, _create_user, _update_user, _delete_user
from worker.models.user import User

app = FastAPI()


@app.get("/", status_code=200)
async def health_check():
    return {"message": "HealthCheck Success"}


@app.get("/users/", status_code=200)
async def get_users(skip: int = 0, limit: int = 10):
    return {"users": _get_users(skip, limit)}


@app.get("/user/{username}", status_code=200)
async def get_user(username: str):
    return {"users": _get_user(username)}


@app.post("/user/}", status_code=201)
async def create_user(user: User):
    _create_user(user.dict())
    return user.dict()


@app.put("/user/{username}", status_code=204)
async def update_user(username: str, user: User):
    _update_user(user.dict(), username)
    return {"username": username}


@app.delete("/user/{username}", status_code=200)
async def delete_user(username: str, user: User):
    _delete_user(user.dict())
    return {"username": username}
