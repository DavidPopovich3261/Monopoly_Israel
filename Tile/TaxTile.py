

class TaxTile:
    def __init__(self,plyer,Tile ):
        plyer.many-=Tile["amount"]
        print(f"Tax{Tile}")