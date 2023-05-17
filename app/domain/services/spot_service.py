from app.infrastructure.repository import SpotRepository

class SpotService():
    def __init__(self, spot_repository: SpotRepository):
        self.spot_repository = spot_repository
    
    def get_spots(self):
        return self.spot_repository.get_all()