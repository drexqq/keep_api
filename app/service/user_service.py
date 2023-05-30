from app.repository.user_repository import UserRepository

class UserService():
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository