from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.util.singleton import singleton
from app.config import configs
from app.config.container import Container
from app.presentation.endpoints import routers as routers
from app.config.database import MongoDB


app = FastAPI()
@singleton
class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            version="0.0.1",
        )

        self.container = Container()
        self.db = MongoDB()

        # set cors
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # set routes
        # @self.app.get("/")
        # def ping():
        #     return "pong"

        self.app.include_router(routers)

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container

app.add_event_handler("startup", db.connect)
app.add_event_handler("shutdown", db.close)

