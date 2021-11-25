import System.Random
# Importing datetime.
from datetime import datetime

def get_random_number():
    seed = int(datetime.now().strftime('%Y%m%d%H%M%S'))%10000
    rand = System.Random(seed).Next(0,100)
    return rand
    
def wait_for_target(spell, timeout):
    Journal.Clear()
    time = 0
    mana = Player.Mana
    while time <= timeout:
        Misc.Pause(5)
        time += 5
        if Target.HasTarget() or Player.Mana < mana:
            return True
        if Journal.Search("disturbed"):
            Player.HeadMessage(13,"disturbed -> " + spell)
            return False
        if Journal.Search("fizzles"):
            Player.HeadMessage(13,"fizzles -> " + spell)
            return False
        if Journal.Search("recovered"):
            Player.HeadMessage(13,"recovered -> " + spell)
            return False
        if Journal.Search("mana"):
            return False
        if Journal.Search("away"):
            return False

OffSet = {
    'North' : (0,-1),
    'South' : (0,1),
    'West' : (-1,0),
    'East' : (1,0),
    'Up' : (-1,-1),
    'Down' : (1,1),
    'Left' : (-1,1),
    'Right' : (1,-1),
    }
        
def Impassable(x, y, map = Player.Map):
    staticTiles = Statics.GetStaticsTileInfo(x, y, map)
    #Misc.SendMessage(str(x) + " " + str(y))
    #Misc.SendMessage(str(staticTiles),14)
    #Misc.SendMessage(str(len(staticTiles)),14)
    
    if staticTiles == None or len(staticTiles) == 0:
        Misc.SendMessage("TESTING by LAND",14)
        staticTile = Statics.GetLandFlag(Statics.GetLandID(x,y,map),"Impassable")
        
        return staticTile
    
    for static in staticTiles:
        Misc.SendMessage("TESTING by STATICSs",14)
        #Misc.SendMessage(str(static))
        Player.HeadMessage("Distance: {}".format(Player.DistanceTo(static.Serial)))
        if Statics.GetTileFlag(static.StaticID,"Impassable"):
        #Misc.SendMessage("Impassable by STATIC",14)
            return True

    return False

    
def teleport(x,y,z,distance = 11):
    if Player.Direction == "North" or Player.Direction == "West" or Player.Direction == "Up" or Player.Direction == "Right" or Player.Direction == "Left": 
        distance = 11
    if Player.Direction == "Down" : 
        distance = 9
    Misc.SendMessage(Player.Direction,14)
    real_offset = OffSet[Player.Direction]
    destinationX = x+real_offset[0]*distance
    destinationY = y+real_offset[1]*distance

    #Misc.SendMessage("----------------------",14)
    #Misc.SendMessage("------DISTANCE--------" + str(distance),55)
    if distance <= 5:
        #Misc.SendMessage("FINISHED",14)
        #Misc.SendMessage("----------------------",55)
        return
    if Impassable(destinationX,destinationY):
        #Misc.SendMessage("Impassable",14)
        teleport(x,y,z,distance-1)
        return
    Player.HeadMessage(55,"------DISTANCE--------" + str(distance) )
    Player.HeadMessage(55,"------DIRECTION --------" + Player.Direction )
    
    if wait_for_target("Teleport",1000):
        Target.TargetExecuteRelative(Player.Serial,distance)
        Misc.Pause(10)
    return
    
if Items.BackpackCount(0x1F42, 0) > 0: # TP Scrolls
    Items.UseItemByID(0x1F42, 0)
else:
    Spells.CastMagery("Teleport")
    teleport(Player.Position.X,Player.Position.Y,Player.Position.Z)  
Misc.Pause(10)    
    #Target.WaitForTarget(900, True)
    #Target.TargetExecute(Rel.X, Rel.Y, Rel.Z)