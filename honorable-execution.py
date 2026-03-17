
from System.Collections.Generic import List
from System import Byte

def MobKill():
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMin = 0 
    filter.RangeMax = 16 
    filter.IsHuman = False
    filter.Notorieties = List[Byte](bytes([3])) # optional, numbers = notoritety codes
    mobs = Mobiles.ApplyFilter(filter)
    Misc.Pause(10)
    mob = Mobiles.Select(mobs, 'Nearest') # multiple selectors possible
    Misc.Pause(10)
    if (mob == None):
        Player.HeadMessage(34,"No mob found")
        return
    elif Player.Mana < Player.ManaMax:
        if Player.DistanceTo(mob) > 2:
            Player.HeadMessage(13,"APPROACH")
            Target.SetLast(mob)
            Timer.Create("timeout",4000)
        while Player.DistanceTo(mob) > 2 and Timer.Check("timeout") == True:
            Misc.Pause(50)
        if Timer.Check("timeout") == False:
            Player.HeadMessage(34,"Timeout")
        elif Player.DistanceTo(mob) <= 2:
            
            if not Player.BuffsExist("Honorable Execution"):
                Spells.CastBushido("Honorable Execution")
                Player.HeadMessage(13,"NOW")
                Player.Attack(mob.Serial)
                Misc.Pause(10)
            
    else:
        Player.HeadMessage(13,"Nothing to do")
        return
    return
MobKill()
Misc.Pause(10)