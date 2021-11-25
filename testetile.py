
TreeStaticID = ["0x00C5", 3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3274, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]

def cutInfront():
    """Get player position and direction. Check for graphic in front for targetting"""
    playerPos = Player.Position
    playerX = Player.Position.X
    playerY = Player.Position.Y
    playerZ = Player.Position.Z
    direction = Player.Direction

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
        
        Misc.SendMessage('Tiles: (X:%i, Y:%i, Z:%i, Facing:%s)' % (tileX, tileY, tileZ, direction))
        
    tileinfo = Statics.GetStaticsTileInfo(tileX, tileY, Player.Map)
    if tileinfo.Count > 0:
        for tile in tileinfo:
            if tile.StaticID not in TreeStaticID:
                Misc.SendMessage('Tem Arvore (X: %i, Y: %i, Z: %i, ID: %s)' % (tileX, tileY, tile.StaticZ, tile.StaticID), 66)
                
                Spells.CastMagery("Teleport")
                Target.WaitForTarget(10000)
                Target.TargetExecute(tileX - 1, tileY - 4, Player.Position.Z +60)
            else:
                Misc.SendMessage('Nao tem Arvore')
                Spells.CastMagery("Teleport")
                Target.WaitForTarget(10000)
                Target.TargetExecute(tileX, tileY, Player.Position.Z +60)

    else:
        Misc.SendMessage('Nao tirou as informacoes')
        Spells.CastMagery("Teleport")
        Target.WaitForTarget(10000)
        Target.TargetExecute(tileX, tileY, Player.Position.Z +60)
        Misc.NoOperation()
        
cutInfront()
Misc.Pause(10)