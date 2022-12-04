from fastapi import APIRouter

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
    def __init__(self, name, entity, model):    
        super().__init__(name)

        self.entity = entity
        self.model = model

        # register routes
        self.router.add_api_route(f"/{self.name}/Get", self.get, methods=["GET"])        
        self.router.add_api_route(f"/{self.name}/Add", self.add, methods=["POST"], response_model=self.model)
        self.router.add_api_route(f"/{self.name}/Update", self.update, methods=["PUT"])
        self.router.add_api_route(f"/{self.name}/Delete", self.delete, methods=["DELETE"])

    def get(self, id):
        e = self.entity.get(self.entity.id == id)
        return e.__data__
        
    def add(self):
        pass

    def update(self):
        pass
    
    def delete(self):
        pass
