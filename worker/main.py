from fastapi import FastAPI, status, HTTPException
from worker.process import _get_users, _get_user, _create_user, _update_user, _delete_user
from worker.models.user import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    return {"message": "HealthChecks Success"}


@app.get("/users/", status_code=status.HTTP_200_OK)
async def get_users(skip: int = 0, limit: int = 10):
    return {"users": _get_users(skip, limit)}


@app.get("/user/{username}", status_code=status.HTTP_200_OK)
async def get_user(username: str):
    return {"users": _get_user(username)}


@app.post("/user/}", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    result = _create_user(user.dict())
    if result:
        return {"message": "Created"}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exist!")


@app.put("/user/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(username: str, user: User):
    _update_user(user.dict(), username)
    return {"username": username}


@app.delete("/user/{username}", status_code=status.HTTP_200_OK)
async def delete_user(username: str):
    _delete_user(username)
    return {"username": username}
