potID = 0x0F06
potID2 = 0x0F0D
Journal.Clear()
pots = Items.FindByID(potID,-1,Player.Backpack.Serial)
potsexp = Items.FindByID(potID2,-1,Player.Backpack.Serial)


def PbConflag():  
    Items.UseItem(pots)
    Target.WaitForTarget(2000)
    Target.LastQueued()
           
PbConflag()
Misc.Pause(10)