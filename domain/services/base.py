
class BaseService:

    def __init__(self, name, entity, model):
        self.name = name
        self.entity = entity
        self.model = model

    def getById(self, id):
        e = self.entity.get(self.entity.id == id)
        return e.__data__
        
    def add(self):
        pass

    def bulkAdd(self):
        pass

    def update(self):
        pass
    
    def delete(self):
        pass

    def bulkDelete(self):
        pass

    def count(self):
        pass
