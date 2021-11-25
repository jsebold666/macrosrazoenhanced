
def POISON_LIGHT():
    #seq = Misc.ReadSharedValue("Sequencing")
    
    if Timer.Check("ligh") == False:
        Spells.CastMagery('Lightning')
        Target.WaitForTarget(450, True)
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

POISON_LIGHT()
Misc.Pause(10)