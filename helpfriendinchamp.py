def helpfriendinchamp():
    
    mob = Mobiles.FindBySerial(0x000C64A8)
    Player.HeadMessage( 13, "ta de olho")

      
    Misc.SendMessage('passou')
    if mob.Poisoned:
        Spells.CastMagery("Cure")
        Target.WaitForTarget(350,True)
        Target.TargetExecute(mob.Serial)
    elif mob.Hits < mob.HitsMax:
        Spells.CastMagery("Heal")
        Target.WaitForTarget(350,True)
        Target.TargetExecute(mob.Serial)
        Misc.Pause(5)
        
    elif mob.IsGhost:
        Spells.CastMagery("Resurrectin")
        Target.WaitForTarget(500,True)
        Target.TargetExecute(mob.Serial)
        Misc.Pause(5)
   
    return
helpfriendinchamp()
Misc.Pause(10)