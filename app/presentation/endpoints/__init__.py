from fastapi import APIRouter

from app.presentation.endpoints.spot import router as spot_router
from app.presentation.endpoints.user import router as user_router

routers = APIRouter()
router_list = [spot_router, user_router]

for router in router_list:
    routers.include_router(router)
