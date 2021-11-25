
def DISTURBED():
  
    if Timer.Check("ma") == False:
        Spells.CastMagery("Poison")
        Target.WaitForTarget(450, True)
        Target.LastQueued()
        Misc.Pause(60)
        Timer.Create("ma", 350)
        return
    else:
        Spells.CastMagery("Weaken")
        Target.WaitForTarget(900, True)
        Target.LastQueued()
        Misc.Pause(50)
        return
    return

DISTURBED()
Misc.Pause(10)