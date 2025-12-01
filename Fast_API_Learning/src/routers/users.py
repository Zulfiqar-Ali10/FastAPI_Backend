from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return [{"name": "Ali"}, {"name": "Asad"}]

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"name": f"User {user_id}"}
