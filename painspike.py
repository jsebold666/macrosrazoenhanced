potID = 0x2268
Journal.Clear()
pots = Items.FindByID(potID,-1,Player.Backpack.Serial)


def PainThrow():
    if Items.BackpackCount(potID, -1) == 0:
        Player.HeadMessage(30, 'Out of scroll pain')
    else:
        stack = pots.Serial
        Items.UseItem(stack)
        Target.WaitForTarget(2000)
        Target.LastQueued()
        Misc.Pause(600)
           
PainThrow()