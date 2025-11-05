


class Board:
    def __init__(self,tiles_data:list[dict]):
        self.tiles_data=tiles_data

    def movement(self,plyer,dick:int):
        if plyer.location+dick <=len(self.tiles_data):
            plyer.location+=dick
        else:
            l=len(self.tiles_data)-plyer.location
            plyer.location=dick-l
            plyer.many+=200


