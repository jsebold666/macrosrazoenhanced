def HelpFriendsChamp():
    
    mob = Target.GetTargetFromList("enemy")
    Misc.Pause(5)

    if mob is not None:
      
        Misc.SendMessage('passou')
        if mob.Paralized:
            Spells.CastMagery("Feeblemind")
            Target.WaitForTarget(500,True)
            Target.TargetExecute(mob.Serial)
            
            Misc.Pause(5)
        elif mob.Poisoned:
            Spells.CastMagery("Cure")
            Target.WaitForTarget(500,True)
            Target.TargetExecute(mob.Serial)
        elif mob.Hits < mob.HitsMax:
            Spells.CastMagery("Heal")
            Target.WaitForTarget(350,True)
            Target.TargetExecute(mob.Serial)
            Misc.Pause(5)
   
                
    return    


HelpFriendsChamp()
Misc.Pause(5)