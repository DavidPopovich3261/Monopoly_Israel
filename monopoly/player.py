

class Player:
    def __init__(self,name,location,many):
        self.name=name
        self.location=location
        self.many=many
        self.property=[]

    def add_property(self,asset:dict):
        self.property.append(asset)

    def