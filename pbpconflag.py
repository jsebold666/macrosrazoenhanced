potID = 0x0F06
potID2 = 0x0F0D
Journal.Clear()
pots = Items.FindByID(potID,-1,Player.Backpack.Serial)
potsexp = Items.FindByID(potID2,-1,Player.Backpack.Serial)


def PbConflag():
    mob = Mobiles.FindBySerial(Target.GetLast())
    
    stack = pots.Serial
    stack2 = potsexp.Serial
    if mob is not None:

        Misc.Pause(100)
        if not mob.Paralized:
            if Items.BackpackCount(potID2, -1) != 0:
                Items.UseItem(potsexp)
            Misc.Pause(400)
            if not Player.HasSpecial and Player.Mana >= 25:
                Player.WeaponSecondarySA()
                Target.WaitForTarget(1500)
                Target.LastQueued()
                
            Misc.Pause(50)
        else:
            if Player.DistanceTo( mob ) <= 6:
                Items.UseItem(pots)
                Target.WaitForTarget(1500)
                Target.LastQueued()
       
           
PbConflag()
Misc.Pause(10)