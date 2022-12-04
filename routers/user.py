from .base import BasicRouter

class UserRouter(BasicRouter):
    def __init__(self, name, entity, model):
        super().__init__(name, entity, model)
