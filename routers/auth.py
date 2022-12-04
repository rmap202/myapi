from .base import BaseRouter

class AuthRouter(BaseRouter):
    def __init__(self, name):
        super().__init__(name)

        self.router.add_api_route(f"/{self.name}/Login", self.login, methods=["POST"])

    def login(self):
        pass
