from fastapi import FastAPI
from typing import List
from uuid import uuid4, UUID
from models import User, Gender, Role, Userupdaterequest



app = FastAPI()


db: list[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender= Gender.female,
        roles= [Role.student]
),
    User(
        id=uuid4(),
        first_name="Jason",
        last_name="staton",
        gender= Gender.male,
        roles= [Role.admin, Role.user]
)


]


@app.get("/")
async def root():
    return {"hiii": "Hello World"}


@app.get("/api/v1/users")
async def get_users():
    return db;

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id:": user.id}


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: Userupdaterequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            return {"message": "user updated"}
