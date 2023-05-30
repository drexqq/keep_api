from app.repository.spot_repository import SpotRepository

class SpotService():
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository = spot_repository
    
    async def get_spots(self):
        return await self.spot_repository.get_all()