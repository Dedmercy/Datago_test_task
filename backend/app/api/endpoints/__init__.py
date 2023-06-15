from app.api.endpoints.account import router as account_router
from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.tracking import router as tracking_router

router_list = [account_router, auth_router, tracking_router]
