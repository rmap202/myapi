import domain.services.auth as auth
from .base import BaseRouter

from domain.models.user import UserModel

class AuthRouter(BaseRouter):
    def __init__(self, name):
        super().__init__(name)
        self.router.add_api_route(f"/{self.name}/Login", self.login, methods=["POST"])
        self.router.add_api_route(f"/{self.name}/Register", self.register, methods=["POST"])

    def login(self):
        pass
    
    def register(self, user : UserModel):
        res = auth.register(user)
        return res
