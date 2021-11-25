def PARA():
    #seq = Misc.ReadSharedValue("Sequencing")
    teste = False;
    if teste == False:
        Spells.CastMagery("Paralyze")
        Target.WaitForTarget(900, True)
        Target.LastQueued()
        Misc.Pause(50)
        return
   

PARA()
Misc.Pause(10)