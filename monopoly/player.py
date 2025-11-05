

class Player:
    def __init__(self,name):
        self.name=name
        self.location=0
        self.many=1500
        self.property=[]

    def add_property(self,asset:dict):
        self.property.append(asset)

    def inpoting(self):

        inpoting=input("y/n")
        if inpoting in ("y","n"):
            return inpoting
        else:
            print("futal")
            return None
