def HelpFriend():
  
    mob = Target.GetTargetFromList("mob")
    Misc.Pause(30)

    if mob is not None:
      
        Misc.SendMessage('passou')
        if mob.Paralized:
            Spells.CastMagery("Feeblemind")
            Target.WaitForTarget(500,True)
            Target.TargetExecute(mob.Serial)
            
            Misc.Pause(30)
        elif mob.Poisoned:
            Spells.CastMagery("Cure")
            Target.WaitForTarget(1000,True)
            Target.TargetExecute(mob.Serial)
        elif mob.Hits < mob.HitsMax:
            Spells.CastMagery("Heal")
            Target.WaitForTarget(500,True)
            Target.TargetExecute(mob.Serial)
            Misc.Pause(30)
   
                
    return    


HelpFriend()
Misc.Pause(50)