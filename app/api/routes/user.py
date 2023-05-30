from fastapi import APIRouter

# router = APIRouter(prefix="/user", tags=["user"], dependencies=[Depends(JWTBearer())])
router = APIRouter(prefix="/user", tags=["user"])