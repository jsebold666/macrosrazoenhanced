from System.Collections.Generic import List
from System import Byte


if Player.Mount:
    Mobiles.UseMobile(Player.Serial)

else:
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMax = 1
    filter.Notorieties = List[Byte](bytes([1,2])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    mobiles = Mobiles.ApplyFilter(filter)
    mobile = Mobiles.Select(mobiles,'Nearest')
    Player.ChatSay(690, "All follow me")
    if mobile:
        Mobiles.UseMobile(mobile)