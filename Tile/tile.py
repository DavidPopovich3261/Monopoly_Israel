from Tile import TaxTile, BonusTile
from monopoly import player,board




class Tile:
    def __init__(self,player,board):
        self.player=player
        self.tile=board[player.location]

    def tile_location(self):
        if self.tile['type']=='property':
            PropertyTile(self.tile,self.player)
        elif self.tile['type']=='tax':
            TaxTile.TaxTile(self.player,self.tile)
        elif self.tile['type'] == 'bonus':
            BonusTile.BonusTile(self.player,self.tile)
        elif self.tile['type'] == 'jail':
            JailTile()
        elif self.tile['type'] == 'go_to_jail':
            GoToJailTile(self.player)



















