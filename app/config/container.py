from dependency_injector import containers, providers

from app.config import configs
from app.config.database import MongoDB
from app.repository import *
from app.service import *

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.routes.spot",
            "app.api.routes.user",
        ]
    )
    db = providers.Singleton(MongoDB, db_url=configs.DATABASE_URI)
    
    spot_repository = providers.Factory(SpotRepository, client=db.provided.client, engine=db.provided.engine)
    user_repository = providers.Factory(UserRepository, client=db.provided.client, engine=db.provided.engine)

    spot_service = providers.Factory(SpotService, spot_repository=spot_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
