potID = 0x226A
Journal.Clear()
pots = Items.FindByID(potID,-1,Player.Backpack.Serial)


def StrangleThrow():
    if Items.BackpackCount(potID, -1) == 0:
        Player.HeadMessage(30, 'Out of scroll strangle')
        Spells.CastNecro("Strangle")
        Target.WaitForTarget(3000)
        Misc.Pause(600)
    else:
        stack = pots.Serial
        Items.UseItem(stack)
        Target.WaitForTarget(2000)
        Misc.Pause(600)
           
StrangleThrow()