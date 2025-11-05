


class PropertyTile:
    def __init__(self,tile:dict,player):
        if 'status' in tile.keys():
            player.many-=tile["rent"]
        else:
            select=player.inpoting()
            if select=="y":
                player.many-=tile["price"]
                player.property.append(tile)
                tile['status']=player.name
            else:

















