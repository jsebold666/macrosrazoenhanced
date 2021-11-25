Misc.Pause(50)
from System.Collections.Generic import List
#
class Coord:
    X = Y = Z = 0
    def __init__(self, x, y):
        self.X = x + Player.Position.X
        self.Y = y + Player.Position.Y
        self.Z = Player.Position.Z
#    
EXPF = Items.Filter()
EXPF.RangeMax = 1
EXPF.OnGround = True
EXPF.Movable = True
EXPIds = List[int]([0x0F0D,0x099B])
EXPF.Graphics = EXPIds

EXPF2 = Items.Filter()
EXPF2.RangeMin = 2
EXPF2.RangeMax = 2
EXPF2.OnGround = True
EXPF2.Movable = True
EXP2Ids = List[int]([0x0F0D,0x099B])
EXPF2.Graphics = EXP2Ids

#
Misc.Pause(10)

def ThrowExploPotAway():
    enemy = Mobiles.FindBySerial(Target.GetLast())
    EXPLOS = Items.ApplyFilter(EXPF)
    EXPLOS2 = Items.ApplyFilter(EXPF2)    
    if len(EXPLOS) > 0:
        c = Items.Select(EXPLOS,'Nearest')
        Items.UseItem(c)
        Target.WaitForTarget(2000,False)
        if enemy == None or Player.DistanceTo( enemy ) > 10:
            Tiles = 6
            Dir = {
                'North' : Coord(0, -Tiles),
                'South' : Coord(0, Tiles),
                'West' : Coord(-Tiles, 0),
                'East' : Coord(Tiles, 0),
                'Up' : Coord(-Tiles, -Tiles),
                'Down' : Coord(Tiles, Tiles),
                'Left' : Coord(-Tiles, Tiles),
                'Right' : Coord(Tiles, -Tiles)
            }
            Rel = Dir[Player.Direction]
            lasttarget = Target.GetLast()
            Target.TargetExecute(Rel.X, Rel.Y, Rel.Z)
            Target.SetLast(lasttarget)
            #Player.HeadMessage(13,"PRIMEIRO IF")
            return
        Target.TargetExecute(enemy)
        #Player.HeadMessage(13,"PRIMEIRO ENEMY")
        #Items.Message(c, 64, 'jhhjh')      
###############################################################################
    elif len(EXPLOS2) > 0:
        c = Items.Select(EXPLOS2,'Nearest')
        Items.Move(c,Player.Backpack.Serial,1,90,100)
        Misc.Pause(600)
        Items.UseItem(c)
        Target.WaitForTarget(2000,False)
        if enemy == None or Player.DistanceTo( enemy ) > 12:
            Tiles = 6
            Dir = {
                'North' : Coord(0, -Tiles),
                'South' : Coord(0, Tiles),
                'West' : Coord(-Tiles, 0),
                'East' : Coord(Tiles, 0),
                'Up' : Coord(-Tiles, -Tiles),
                'Down' : Coord(Tiles, Tiles),
                'Left' : Coord(-Tiles, Tiles),
                'Right' : Coord(Tiles, -Tiles)
            }
            Rel = Dir[Player.Direction]
            lasttarget = Target.GetLast()
            Target.TargetExecute(Rel.X, Rel.Y, Rel.Z)
            Target.SetLast(lasttarget)
            #Player.HeadMessage(13,"SEGUNDO IF")
            return
        Target.TargetExecute(enemy)
        #Player.HeadMessage(13,"SEGUNDO ENEMY")
        #Items.Message(c, 64, 'jhhjh')      
        
    return    


ThrowExploPotAway()
Misc.Pause(600)