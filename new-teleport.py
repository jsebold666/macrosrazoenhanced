from ClassicAssist.UO.Data import Statics, TileFlags, MapInfo
from Assistant import Engine

def Impassable(x, y, map = int(Engine.Player.Map)):
    staticTiles = Statics.GetStatics( map, x, y )
    
    if staticTiles == None or staticTiles.Length == 0:
        return MapInfo.GetLandTile(map, x, y).Flags.HasFlag(TileFlags.Impassable  and  TileFlags.Surface or TileFlags.PrefixA  and  TileFlags.Surface)
    
    for x in staticTiles:
        if x.Flags.HasFlag(TileFlags.Impassable and  TileFlags.Surface):
            return True

    return False

def get_direction_dist():
    if Direction('self') == 'North' or  Direction('self') == 'East' or Direction('self') == 'South' or Direction('self') == 'West':
        return 13
    elif Direction('self') == 'Northeast' or Direction('self') == 'Southeast' or Direction('self') == 'Southwest' or Direction('self') == 'Northwest':
        return 12
    else:
        return 11
    
def Tele_Tile(distance):
    offsetX = 0
    offsetY = 0
    if Direction('self') == 'North':
        offsetY = -1;
    elif Direction('self') == 'Northeast':
        offsetY = -1;
        offsetX = 1;
    elif  Direction('self') == 'East':
        offsetX = 1;
    elif Direction('self') == 'Southeast':
        offsetX = 1;
        offsetY = 1;
    elif Direction('self') == 'South':
        offsetY = 1;
    elif Direction('self') == 'Southwest':
        offsetY = 1;
        offsetX = -1;
    elif Direction('self') == 'West':
        offsetX = -1;
    elif Direction('self') == 'Northwest':
        offsetX = -1;
        offsetY = -1;
        
    totalOffsetX = offsetX * distance;
    totalOffsetY = offsetY * distance;
    
    destinationX = Engine.Player.X + totalOffsetX;
    destinationY = Engine.Player.Y + totalOffsetY;
    
    if Impassable(destinationX,destinationY):
        return True
    return False
    
dist = get_direction_dist()
if dist is None:
    dist = 11
for x in range(dist,1,-1):
    if Tele_Tile(x) == False:
        HeadMsg(str(x), "self")
        Cast("teleport")
        if WaitForTargetOrFizzle(1500):
            if InRange('self', dist):
                TargetTileRelative("self", x, False)
                Pause(80)
                Stop()