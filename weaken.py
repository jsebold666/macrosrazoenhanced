
def WEAKEN():
    #seq = Misc.ReadSharedValue("Sequencing")
    
    if Timer.Check("ligh") == False:
        Spells.CastMagery('Weaken')
        Target.WaitForTarget(250, True)
        Target.LastQueued()
        Misc.Pause(60)
        
        return
    else:
        Spells.CastMagery("Poison")
        Target.WaitForTarget(900, True)
        Target.LastQueued()
        Misc.Pause(50)
        Timer.Create("ligh", 350)
        return
    return

WEAKEN()
Misc.Pause(10)