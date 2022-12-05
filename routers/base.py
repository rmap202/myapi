from fastapi import APIRouter
from domain.models.user import UserModel

from domain.services.base import BaseService

"""
    Base Router is very basic and just create a name and a router.
"""
class BaseRouter():
    def __init__(self, name):
        self.name = name
        self.router = APIRouter(tags=[self.name])

"""
    Basic Router inherit's BaseRouter, it's added functionality is that it handles getting, updating, and deleting
    with any type of entity.
"""
class BasicRouter(BaseRouter):

    model = None

    def __init__(self, name, entity, model):    
        super().__init__(name)

        self.service = BaseService(name, entity, model)
        self.entity = entity
        self.model = model

        # register routes
        self.router.add_api_route(f"/{self.name}/Get", self.get, methods=["GET"])        
        self.router.add_api_route(f"/{self.name}/Add", self.add, methods=["POST"])
        self.router.add_api_route(f"/{self.name}/Update", self.update, methods=["PUT"])
        self.router.add_api_route(f"/{self.name}/Delete", self.delete, methods=["DELETE"])

    async def get(self):
        return self.service.getById(id)

    ## TODO: Override with Model
    async def add(self, item : model):
        return item.__dict__

    async def update(self):
        pass
    
    async def delete(self):
        pass
