from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get('/matheus')
async def matheus() -> dict:
    """
    This function returns a greeting message for Matheus.
    """
    return {'message': 'Hello Matheus!'}