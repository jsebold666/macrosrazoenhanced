from System.Collections.Generic import List
from System import Byte

potID = 0x0F06
pots = Items.FindByID(potID,-1,Player.Backpack.Serial)
potIDexp = 0x0F0D
potsExp = Items.FindByID(potIDexp,-1,Player.Backpack.Serial)

Journal.Clear()




mob = Mobiles.FindBySerial(Target.GetLast()) 

if mob is not None:
    Misc.SendMessage("Attack Next")
    Player.Attack(Target.GetLast()) 
    Misc.SendMessage("using explo")
    Items.UseItem(pots)
    if not Player.HasSpecial and Player.Mana >= 25:
        Player.WeaponSecondarySA()
    if(mob.Paralized):
        Target.LastQueued()
else: 
    if not Player.HasSpecial and Player.Mana >= 25:
        Player.WeaponSecondarySA()
    Misc.SendMessage("Dont have target")
