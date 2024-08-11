from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def health():
    return {"message": "api working"}
