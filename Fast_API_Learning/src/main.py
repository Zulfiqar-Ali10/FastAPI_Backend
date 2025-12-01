from fastapi import FastAPI, HTTPException 
from typing import Optional
from pydantic  import BaseModel
import asyncio
from routers import users
from routers import products


app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Hello World^^"}

# ////////////////////////////////////////////////////////////////

# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id}

# @app.get("/items/")
# def read_item(name: str, age: int = 0):
#     return {"name": name, "age": age}

# @app.get("/search")
# def search_item(q: Optional[str]= None):
#     if q:
#         return {"query": q}
#     return{"query": "no query provided"}



# ////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////

# /// Model Create 

# class User(BaseModel):
#     name: str
#     age: int
#     is_active: bool = True

# @app.post("/users1/")
# def create_user(user: User):
#     return {"message": "User created", "user": user}


# /////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////

# class UserIn(BaseModel):
#     name: str
#     age: int
#     password: str  # sensitive

# class UserOut(BaseModel):
#     name: str
#     age: int

# @app.post("/users/", response_model=UserOut)
# def create_user(user: UserIn):
#     return user

# /////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////

# fake_users_db = {
#     1: {"name": "Ali", "age": 25},
#     2: {"name": "Sara", "age": 30}
# }

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id not in fake_users_db:
#         raise HTTPException(status_code=404, detail="User not found")
#     return fake_users_db[user_id]


# /////////////////////////////////////////////////////////////

# @app.get("/sync")
# def sync_route():
#     import time
#     time.sleep(3)  # blocking
#     return {"message": "Hello from sync"}

# @app.get("/async")
# async def async_route():
#     await asyncio.sleep(3)  # non-blocking
#     return {"message": "Hello from async"}

# @app.get("/concurrent")
# async def concurrent_example():
#     task1 = asyncio.create_task(asyncio.sleep(2))
#     task2 = asyncio.create_task(asyncio.sleep(2))
#     await task1
#     await task2
#     return {"message": "Both tasks done concurrently"}

# /////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////

# app.include_router(users.router, prefix="/users", tags=["Users"])

# /////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////

app.include_router(products.router)

# ////////////////////////////////////////////////////////////////////

