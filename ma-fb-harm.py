
def MA_FB_HARM():
    #seq = Misc.ReadSharedValue("Sequencing")
    mob = Mobiles.FindBySerial(Target.GetLast())
    if mob:
        if Player.DistanceTo( mob ) <= 1:
            Spells.CastMagery("Harm")
            Target.WaitForTarget(700, True)
            Target.LastQueued()
            return
    if Timer.Check("ma") == False:
        Spells.CastMagery("Magic Arrow")
        Target.WaitForTarget(175, True)
        Target.LastQueued()
        Misc.Pause(10)
        Timer.Create("ma", 150)
        return
    else:
        Spells.CastMagery("Fireball")
        Target.WaitForTarget(900, True)
        Target.LastQueued()
        Misc.Pause(10)
        return
    return

MA_FB_HARM()
Misc.Pause(5)