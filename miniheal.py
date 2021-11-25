def MiniHeal():
    if not Player.YellowHits:
        if not Player.Poisoned:
            Spells.CastMagery("Heal")
            Target.WaitForTarget(450, True)
            Target.SelfQueued()
            Misc.Pause(10)
        else:
            Spells.CastMagery("Cure")
            Target.WaitForTarget(450, True)
            Target.SelfQueued()
            Misc.Pause(10)
    elif Player.GetSkillValue('Chivalry') > 30:
            Spells.CastChivalry("Remove Curse")
            Target.WaitForTarget(800,True)
            Target.SelfQueued()
    elif Player.GetSkillValue('Bushido') > 50:
        Spells.CastBushido('Confidence')
        Misc.Pause(10)
    return   
MiniHeal()
Misc.Pause(50)