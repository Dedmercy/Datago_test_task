from fastapi import FastAPI

from app.api.endpoints import router_list


class AppCreator:
    """
        Class of initialization of an app.
    """
    __app: FastAPI

    def __init__(self):
        self.__app = FastAPI(
            title="Money tracker",
            description="My money tracker"
        )
        self.register_events()
        self.register_routes()

    def get_app(self) -> FastAPI:
        """
            Getting the application instance.
        """
        return self.__app

    def register_events(self):
        @self.__app.on_event("startup")
        async def startup():
            pass

        @self.__app.on_event("shutdown")
        async def shutdown():
            pass

    def register_routes(self):
        for router in router_list:
            self.__app.include_router(router)
