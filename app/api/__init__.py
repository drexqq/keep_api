from fastapi import APIRouter

from app.api.routes.spot import router as spot_router
from app.api.routes.user import router as user_router

routers = APIRouter()
router_list = [spot_router, user_router]

for router in router_list:
    routers.include_router(router)
