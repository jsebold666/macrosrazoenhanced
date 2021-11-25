from System.Collections.Generic import List
from System import Byte
 
def mobs_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
 
 
use_eoo = 1
use_df = 0
use_cw = 1
ls_or_ability = 2 # ls == 1
 
 
use_honor = 1
 
#Player.InvokeVirtue()
        
def fighting(enemy): 
 
    
    Player.Attack(nearest)  
    
    if not Player.BuffsExist('Enemy Of One')and use_eoo == 1 and Player.Mana >= 12:
        Spells.CastChivalry('Enemy Of One')
        Misc.Pause(500)
    elif not Player.BuffsExist('Divine Fury') and use_df == 1 and Player.Mana >= 8:
        Spells.CastChivalry('Divine Fury')
        Misc.Pause(500)
    elif not Player.BuffsExist('Consecrate Weapon') and use_cw == 1  and Player.Mana >= 6:
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)
    else:
        if nearby_enemies_len == 1:
            if ls_or_ability == 1:
                if not Player.SpellIsEnabled('Lightning Strike') and Player.Mana >= 6:
                    Spells.CastBushido('Lightning Strike')
            elif ls_or_ability == 2:
                if not Player.HasSpecial and Player.Mana >= 25:
                    Player.WeaponPrimarySA()
            Misc.Pause(500)
        elif nearby_enemies_len >=2:
            if not Player.SpellIsEnabled('Momentum Strike') and Player.Mana >= 6:
                    Spells.CastBushido('Momentum Strike')
            
 
 
 
 
 
while not Player.IsGhost and Player.Visible:
    
    victims = mobs_list(6)
    
    if len(victims) > 0:
        nearest = Mobiles.Select(victims, 'Nearest')
        #Misc.SendMessage ('nearest: {}'.format(nearest.Name))
        
        if use_honor == 1:
            Journal.Clear()
            Player.InvokeVirtue("Honor")
            Target.WaitForTarget(1000)
            Target.TargetExecute(nearest)
            Journal.WaitJournal('Honorable',1000)
            #Misc.Pause(1000)
 
        while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=6:#:
            #Misc.SendMessage('FIGHTING WITH : {}'.format (nearest.Name))
            nearby_enemies_len = len(mobs_list(1))
            #Misc.SendMessage (nearby_enemies_len)
            fighting(nearest)
            Misc.Pause(100)
            
    else:
        #Misc.SendMessage('no enemy')
        Misc.Pause(100)
