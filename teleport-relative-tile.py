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
        #Misc.SendMessage("TESTING by LAND",14)
        return Statics.GetLandFlag(Statics.GetLandID(x,y,map),"Impassable")
    
    for static in staticTiles:
        #Misc.SendMessage("TESTING by STATICS",14)
        #Misc.SendMessage(str(static))
        if Statics.GetTileFlag(static.StaticID,"Impassable"):
        #Misc.SendMessage("Impassable by STATIC",14)
            return True

    return False

    
def teleport(x,y,z,distance = 11):
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
    Player.HeadMessage(55,"------DISTANCE--------" + str(distance))
    Target.WaitForTarget(1000, True)
    mouse = Misc.MouseLocation()
    Misc.SendMessage("{}".format(mouse))
    Misc.LeftMouseClick(mouse.X,mouse.Y,False)
    Misc.Pause(10)
    return
    
teleport(Player.Position.X,Player.Position.Y,Player.Position.Z)  
Misc.Pause(10)    
    #Target.WaitForTarget(900, True)
    #Target.TargetExecute(Rel.X, Rel.Y, Rel.Z)