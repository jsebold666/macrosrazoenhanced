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
        Player.HeadMessage(13,"Range ZERO - UM")
        c = Items.Select(EXPLOS,'Nearest')
        Items.UseItem(c)
        Target.WaitForTarget(500,True)
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
            Player.HeadMessage(13,"Range 4 - UM")
            lasttarget = Target.GetLast()
            Target.TargetExecute(Rel.X, Rel.Y, Rel.Z)
            Misc.Pause(200)
            Target.SetLast(lasttarget)
            return
        Target.TargetExecute(enemy)
        Misc.Pause(250)


    elif len(EXPLOS2) > 0:
        c = Items.Select(EXPLOS2,'Nearest')
        Player.HeadMessage(13,"Range DOISs")
        Items.Move(c,Player.Backpack.Serial,1,90,100)
        Misc.Pause(600)
        Items.UseItem(c)
        Target.WaitForTarget(500,True)
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
            Misc.Pause(250)
            Target.SetLast(lasttarget)
            return
        Target.TargetExecute(enemy)
        Misc.Pause(250)
    else:    
        potID = 0x0F0D
        Player.HeadMessage(13,"Range 3 - UM")
        pots = Items.FindByID(potID,-1,Player.Backpack.Serial)
        if Items.BackpackCount(potID, -1) == 0:
            Player.HeadMessage(30, 'Out of Exp pots')
        else:
            stack = pots.Serial
            Items.UseItem(stack)
            Target.WaitForTarget(200,True)
            if enemy != None:
                if Player.DistanceTo( enemy ) <= 11:
                    Player.HeadMessage(13,"Range 32 - UM")
                    Target.TargetExecute(enemy)
                    #Target.ClearLastAttack( )
                    #Target.ClearLastandQueue( )
                    Misc.Pause(10)
                    return
            elif Target.GetLast() != None:
                Player.HeadMessage(13,"Range 31 - UM")
                Target.LastQueued()
                ##Target.ClearLastAttack( )
                ##Target.ClearLastandQueue( )
                Misc.Pause(10)
                return
    return    

ThrowExploPotAway()
Misc.Pause(10)