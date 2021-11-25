RaggioScansione = 11
TreeStaticID = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3274, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]



# Variabili Sistema
from System.Collections.Generic import List
tileinfo = List[Statics.TileInfo]
treeposx = []
treeposy = []
treeposz = []
treegfx = []
treenumber = 0
blockcount = 0
lastrune = 5
onloop = False

def ScanStatic( ): 
    global treenumber
    Misc.SendMessage("--> Iniciou o scaner", 77)
   
    direction = Player.Direction
    playerX = Player.Position.X
    playerY = Player.Position.Y
    playerZ = Player.Position.Z
    if direction == 'Up':
        tileX = playerX - 11
        tileY = playerY - 11
        tileZ = playerZ
        x = -1
        z = -1
    elif direction == 'North':
        tileX = playerX
        tileY = playerY - 11
        tileZ = playerZ
        x = 0
        z = -1
    elif direction == 'Right':
        tileX = playerX + 11
        tileY = playerY - 11
        tileZ = playerZ
        x = + 1
        z = - 1
    elif direction == 'East':
        tileX = playerX + 11
        tileY = playerY
        tileZ = playerZ
        x = + 1
        z = 0
    elif direction == 'Down':
        tileX = playerX + 11
        tileY = playerY + 11
        tileZ = playerZ
        x = + 1
        z = + 1
    elif direction == 'South':
        tileX = playerX
        tileY = playerY + 11
        tileZ = playerZ
        x = 0
        z = + 1
    elif direction == 'Left':
        tileX = playerX - 11
        tileY = playerY + 11
        tileZ = playerZ
        x = - 1
        z = + 1
    elif direction == 'West':
        tileX = playerX - 11
        tileY = playerY
        tileZ = playerZ
        x = + 1
        z = 0
    minx = tileX
    maxx = tileX
    miny = tileY
    maxy = tileY

    while miny <= maxy:
        while minx <= maxx:
            tileinfo = Statics.GetStaticsTileInfo(minx, miny, Player.Map)
            if tileinfo.Count > 0:
                for tile in tileinfo:
                    for staticid in TreeStaticID:
                        if staticid != tile.StaticID:
                            if direction == direction:
                                Misc.SendMessage('--> Titles', 66)
                                Misc.SendMessage('--> Titleff X: %i - Y: %i - Z: %i' % (tileX, tileY, Player.Position.Z +60), 66)
                            Misc.SendMessage('--> Title X: %i - Y: %i - Z: %i' % (maxx, maxy, tile.StaticZ), 66)
                            treeposx.Add(minx)
                            treeposy.Add(miny)
                            treeposz.Add(tile.StaticZ)
                            treegfx.Add(tile.StaticID)
                            Spells.CastMagery("Teleport")
                            Target.WaitForTarget(1000)
                            Target.TargetExecute(maxx, maxy, Player.Position.Z +60)
                        else :
                            Misc.SendMessage('--> nao tem arvore' % (treenumber), 77)
                      
            else:
                Misc.SendMessage('--> Totale Alberis: %i' % (treenumber), 77)
                Spells.CastMagery("Teleport")
                Target.WaitForTarget(1000)
                Target.TargetExecute(tileX, tileY, Player.Position.Z +60)

    
ScanStatic()
Misc.ScriptStop("ScanStatic")