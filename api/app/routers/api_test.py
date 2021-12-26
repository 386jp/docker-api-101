from fastapi import APIRouter

router = APIRouter()

@router.get('/', tags=["test"])
def get_hello_world() -> dict:
    return {"message": "Hello World!"}