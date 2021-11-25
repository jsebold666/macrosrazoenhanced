# Survival for Dexxers - Made by Mark (marcosgribeiro@gmail.com) @ September, 2020.

from datetime import datetime, timedelta
from System.Collections.Generic import List
from System import Byte 


#------------------ VARIABLES
#**CHAGE_ME** 
PET = 0x000628C0
#**CHAGE_ME** 

# ---------------------------------------------------------------------
# --------------------------- TIMERS ----------------------------------
# ---------------------------------------------------------------------
timer_warning = datetime.now()- timedelta(seconds=10)
timer_healpot = datetime.now()- timedelta(seconds=12)
timer_buffhealing = datetime.now()- timedelta(seconds=8)
timer_apple = datetime.now()- timedelta(seconds=122000) 
alert_mortal = True  
    
#if datetime.now() >= timer_alert_mortal+timedelta(seconds=22)

# ---------------------------------------------------------------------
# --------------------------- STATUS ----------------------------------
# ---------------------------------------------------------------------
status_str = 109
status_dex = 58

def MultiTrapPouchUse():
    pouches = []
    for item in Player.Backpack.Contains:
        if "pouch" in str(item):
            pouches.append(item.Serial)
    
    for pouch in pouches:
        trapped = Misc.ReadSharedValue(str(pouch))

        if trapped == "trapped":
            Misc.SetSharedValue(str(pouch), "empty")
            Player.HeadMessage( 13, "USING POUCH")
            Items.UseItem(pouch)
            return

if __name__ == '__main__':
  
    while not Player.IsGhost:  
        mob = Mobiles.FindBySerial(Target.GetLast())
        Misc.Pause(100)
        if mob is not None:
            if Player.DistanceTo(mob) < 16:
                if Player.Str < status_str and not Target.HasTarget():
                    Items.UseItemByID(0x0F09)
                    Misc.Pause(600)
                
                if Player.Dex < status_dex and not Target.HasTarget():
                    Items.UseItemByID(0x0F08)
                    Misc.Pause(600)
        # ---------------------------------------------------------------------
        # --------------------------- ALERTS ----------------------------------
        # ---------------------------------------------------------------------

        if not Player.Visible or Target.HasTarget():
            continue
             
        #CHECKING FOR ESSENTIAL PVP RESOURCES AND ALERT       
        if datetime.now() >= timer_warning+timedelta(seconds=10):
            timer_warning = datetime.now()
            Player.HeadMessage( 82, "[Running] Survival")
            
            # CHECKING FOR ---> REFRESH POTS <----
            refresh = Items.BackpackCount(0xf0b, -1) 
            if refresh == 0:
                Player.HeadMessage( 32, "[DANGER] OUT OF REFRESH!")
            else:
                if refresh < 3:
                    Player.HeadMessage( 34, "[Alert] Refresh pots!")
                elif refresh < 10:
                    Player.HeadMessage( 52, "[Warning] Refresh pots!") 
            # CHECKING FOR ---> POUCHES <----
            trappedpouch =  True
            for item in Player.Backpack.Contains:
                if "pouch" in str(item):
                    
                    trapped = Misc.ReadSharedValue(str(item.Serial))
                    Player.HeadMessage( 32, "POUCH NOT TRAPPEDS")
                   
                    if trapped == 0:
                        trapped_pouch =  True
                        break
            if not trappedpouch:
                Player.HeadMessage( 32, "POUCH NOT TRAPPED")
        
        # ---------------------------------------------------------------------
        # ------------------------- BANDAGES ----------------------------------
        # --------------------------------------------------------------------- 
        if not Player.BuffsExist("Healing") and Player.Hits < Player.HitsMax*0.8:
            lasttarget = Target.GetLast()
            Items.UseItemByID( 0x0E21, -1 )
            Target.WaitForTarget( 400, True )
            Target.Self()
            Target.SetLast(lasttarget) 
            Misc.Pause(500)        
        
        # ---------------------------------------------------------------------
        # --------------------------- APPLE -----------------------------------
        # ---------------------------------------------------------------------      
        if datetime.now() >= timer_apple+timedelta(seconds=122000):
            if Player.YellowHits and Player.Hits < Player.HitsMax*0.8:
                Player.HeadMessage( 52, "USING APPLE")  
                apple = Items.BackpackCount(0x2fd8, -1) 
                if(apple > 0): 
                    Items.UseItemByID(0x2fd8,-1)
                    Misc.Pause(400)
                    timer_apple = datetime.now() 
        
        # ---------------------------------------------------------------------  
        # ------------------------ CURE / HEAL --------------------------------
        # ---------------------------------------------------------------------
        
        
        if Player.Poisoned and not Target.HasTarget():
            Items.UseItemByID(0xf07,-1)
            Misc.Pause(400)
        if not Player.YellowHits and not Player.Poisoned and Player.Hits < Player.HitsMax*0.7 and not Target.HasTarget():
            if datetime.now() >= timer_healpot +timedelta(seconds=12):
                Items.UseItemByID(0xf0c,-1)
                timer_healpot = datetime.now()
                Player.HeadMessage( 62, "Heal pot!!")
                Misc.Pause(400)
                
  
                
                
        # ---------------------------------------------------------------------  
        # ------------------------ buff evil omen --------------------------------
        # ---------------------------------------------------------------------
        
        if Player.BuffsExist("Evil Omen"):
            Player.HeadMessage( 62, "Remove Evil Omen!!")
            Items.UseItemByID(0x0F0A,-1)        
                
        # ---------------------------------------------------------------------
        # --------------------------- REFRESH ---------------------------------
        # ---------------------------------------------------------------------
        if Player.Stam < Player.StamMax*0.5 and not Target.HasTarget():
            refresh = Items.BackpackCount(0xf0b, -1) 
            if(refresh > 0): 
                Items.UseItemByID(0xf0b,-1)
                Player.HeadMessage( 62, "Refresh pot!!")
                Misc.Pause(400)
        
        # ---------------------------------------------------------------------
        # ----------------------- Auto-Pouch if Paralyze ----------------------
        # ---------------------------------------------------------------------
        if Player.Paralized and Player.Hits > 40:
            MultiTrapPouchUse()
        Misc.Pause(150)
        
        
        
        
    # ---------------------------------------------------------------------
    # ----------------- Deslogar Morto - Proteger o PET--------------------
    # ---------------------------------------------------------------------
    if Player.IsGhost:
        Misc.Disconnect()           