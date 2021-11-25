def HelpMount():
    
    mob = Mobiles.FindBySerial(0x00C8)
    Misc.Pause(30)
    Player.HeadMessage( 62, "tira do paralyze esse cavalo!")
    if mob is not None:
        Player.HeadMessage( 62, "tira do paralyze esse cavalso!")
        Misc.SendMessage('passou')
        if mob.Paralized:
            Player.HeadMessage( 62, "tira do paralyze esse cavalo!")
            Spells.CastMagery("Feeblemind")
            Target.WaitForTarget(500,True)
            Target.TargetExecute(mob.Serial)
            
            Misc.Pause(30)
        elif mob.Poisoned:
            Player.HeadMessage( 62, "cura esse cavalo!")
            Spells.CastMagery("Cure")
            Target.WaitForTarget(1000,True)
            Target.TargetExecute(mob.Serial)
        elif mob.Hits < mob.HitsMax:
            Player.HeadMessage( 62, "heala esse cavalo!")
            Spells.CastMagery("Heal")
            Target.WaitForTarget(500,True)
            Target.TargetExecute(mob.Serial)
            Misc.Pause(30)
   
                
    return    


HelpMount()
Misc.Pause(50)