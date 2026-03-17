# Survival for Dexxers - Made by Mark (marcosgribeiro@gmail.com) @ September, 2020.

from datetime import datetime, timedelta
from System.Collections.Generic import List
from System import Byte
 
# SET False IF YOU WANT DO DISABLE AUTO-CONFLAG
auto_conflag = True
# SET False IF YOU WANT DO DISABLE AUTO-POUCH
auto_pouch = True
# SET False IF YOU WANT DO DISABLE AUTO USE OF POTS (STR, AGI, HEAL, CURE and REFRESH)
auto_chug_pots = True
# ---------------------------------------------------------------------
# --------------------------- STATUS ----------------------------------
# ---------------------------------------------------------------------
status_str_mais_um = 118
status_dex_mais_um = 50
            


if Player.GetRealSkillValue('Alchemy') == 0:
    status_str_mais_um = 117
    status_dex_mais_um = 52
elif Player.GetRealSkillValue('Alchemy') < 66:
    status_str_mais_um = 117
    status_dex_mais_um = 52
elif Player.GetRealSkillValue('Alchemy') < 99:
    status_str_mais_um = 117
    status_dex_mais_um = 52
else:
    status_str_mais_um = 117
    status_dex_mais_um = 52
guardlines = [['Heartwood'],[6911, 255],[7168, 512],['Cove'],[2200, 1110],[2250, 1160],['Cove'],[2200, 1160],[2286, 1246],['Britain'],[1416, 1498],[1740, 1777],['Britain'],[1500, 1408],[1546, 1498],['Britain'],[1385, 1538],[1416, 1777],['Britain'],[1416, 1777],[1740, 1837],['Britain'],[1385, 1777],[1416, 1907],['Britain'],[1093, 1538],[1385, 1907],['Britain'],[1492, 1602],[1500, 1621],['Britain'],[1500, 1610],[1508, 1626],['Britain'],[1576, 1584],[1600, 1600],['Britain'],[1456, 1512],[1472, 1528],['Britain'],[1472, 1512],[1480, 1520],['Britain'],[1486, 1684],[1494, 1692],['Britain'],[1494, 1676],[1502, 1700],['Britain'],[1424, 1712],[1432, 1736],['Britain'],[1432, 1712],[1440, 1724],['Britain'],[1608, 1584],[1632, 1592],['Britain'],[1616, 1576],[1624, 1584],['Britain'],[1544, 1760],[1560, 1776],['Britain'],[1560, 1760],[1568, 1768],['AWheatfieldinBritain1'],[1120, 1776],[1152, 1808],['AWheatfieldinBritain2'],[1184, 1808],[1216, 1840],['AWheatfieldinBritain3'],[1216, 1872],[1248, 1904],['ACarrotFieldinBritain1'],[1208, 1712],[1224, 1736],['AnOnionFieldinBritain1'],[1224, 1712],[1240, 1736],['ACabbageFieldinBritain1'],[1176, 1672],[1192, 1695],['ATurnipFieldinBritain1'],[1192, 1672],[1208, 1696],['AWheatfieldinBritain4'],[1104, 1608],[1136, 1640],['AWheatfieldinBritain5'],[1136, 1560],[1168, 1592],['ATurnipFieldinBritain2'],[1208, 1592],[1224, 1616],['ACarrotFieldinBritain2'],[1224, 1592],[1240, 1616],['Jhelom'],[1303, 3670],[1492, 3895],['Jhelom'],[1338, 3895],[1412, 3923],['Jhelom'],[1383, 3951],[1492, 4045],['Jhelom'],[1352, 3800],[1368, 3832],['Jhelom'],[1368, 3808],[1376, 3824],['Jhelom'],[1432, 3768],[1464, 3776],['Jhelom'],[1440, 3776],[1464, 3784],['Minoc'],[2411, 366],[2546, 607],['Minoc'],[2548, 495],[2620, 550],['Minoc'],[2564, 585],[2567, 627],['Minoc'],[2567, 585],[2628, 646],['Minoc'],[2499, 627],[2567, 690],['Minoc'],[2457, 397],[2497, 405],['Minoc'],[2465, 405],[2473, 413],['Minoc'],[2481, 405],[2489, 413],['Ocllo'],[3587, 2456],[3706, 2555],['Ocllo'],[3706, 2460],[3708, 2555],['Ocllo'],[3587, 2555],[3693, 2628],['Ocllo'],[3590, 2628],[3693, 2686],['Ocllo'],[3693, 2555],[3754, 2699],['Ocllo'],[3754, 2558],[3761, 2699],['Ocllo'],[3761, 2555],[3768, 2699],['Ocllo'],[3695, 2699],[3761, 2712],['Ocllo'],[3664, 2608],[3680, 2624],['Ocllo'],[3664, 2640],[3672, 2656],['Ocllo'],[3672, 2648],[3680, 2656],['Trinsic'],[1856, 2636],[1931, 2664],['Trinsic'],[1816, 2664],[2099, 2895],['Trinsic'],[2099, 2782],[2117, 2807],['Trinsic'],[1970, 2895],[2017, 2927],['Trinsic'],[1796, 2696],[1816, 2763],['Trinsic'],[1800, 2796],[1816, 2848],['Trinsic'],[1834, 2728],[1856, 2744],['Trinsic'],[2024, 2784],[2040, 2804],['Trinsic'],[2026, 2804],[2040, 2806],['Trinsic'],[2024, 2806],[2040, 2813],['Trinsic'],[1923, 2786],[1935, 2808],['Trinsic'],[1935, 2786],[1942, 2800],['Vesper'],[2893, 598],[3014, 648],['Vesper'],[2816, 648],[3065, 1013],['Vesper'],[2734, 944],[2816, 948],['Vesper'],[2728, 948],[2816, 1001],['Vesper'],[2952, 864],[2968, 896],['Vesper'],[2968, 872],[2976, 888],['Vesper'],[2776, 952],[2792, 984],['Vesper'],[2768, 960],[2776, 976],['Vesper'],[2892, 901],[2908, 920],['Vesper'],[2908, 904],[2916, 912],['Yew'],[92, 656],[441, 881],['Yew'],[441, 746],[657, 881],['Yew'],[258, 881],[657, 1261],['Yew'],[657, 922],[699, 1229],['Yew'],[657, 806],[674, 834],['Yew'],[718, 874],[756, 896],['Yew'],[600, 808],[624, 832],['AFieldofSheepinYew1'],[664, 928],[686, 950],['AFieldofSheepinYew2'],[664, 1168],[686, 1190],['AFarminYew'],[560, 1088],[582, 1110],['AWheatfieldinYew1'],[560, 1232],[576, 1248],['AWheatfieldinYew2'],[368, 1176],[382, 1208],['Wind'],[5294, 19],[5366, 139],['Wind'],[5132, 58],[5213, 126],['Wind'],[5197, 126],[5252, 204],['Wind'],[5132, 3],[5202, 58],['Wind'],[5252, 112],[5294, 170],['Wind'],[5213, 98],[5252, 126],['Wind'],[5279, 57],[5294, 112],['Wind'],[5252, 170],[5284, 178],['Wind'],[5286, 25],[5294, 57],['Wind'],[5252, 178],[5272, 183],['Wind'],[5252, 183],[5262, 193],['Wind'],[5159, 15],[5184, 24],['Wind'],[5159, 24],[5168, 40],['Wind'],[5175, 24],[5184, 32],['Wind'],[5212, 159],[5221, 183],['Wind'],[5221, 171],[5228, 183],['Wind'],[5206, 164],[5212, 179],['Wind'],[5303, 28],[5319, 42],['SerpentsHold'],[2868, 3324],[3073, 3519],['SerpentsHold'],[2960, 3400],[2976, 3416],['SerpentsHold'],[2968, 3416],[2976, 3432],['SerpentsHold'],[3008, 3450],[3022, 3464],['SkaraBrae'],[538, 2107],[688, 2297],['SkaraBrae'],[600, 2232],[616, 2256],['SkaraBrae'],[592, 2240],[600, 2256],['SkaraBrae'],[616, 2240],[624, 2256],['SkaraBrae'],[552, 2168],[568, 2192],['SkaraBrae'],[568, 2168],[576, 2176],['Nujelm'],[3475, 1000],[3835, 1435],['Nujelm'],[3736, 1184],[3752, 1207],['Nujelm'],[3728, 1192],[3736, 1207],['Nujelm'],[3728, 1288],[3751, 1303],['Nujelm'],[3728, 1303],[3744, 1312],['Nujelm'],[3728, 1312],[3740, 1320],['Nujelm'],[3728, 1320],[3744, 1343],['Nujelm'],[3744, 1328],[3751, 1343],['Nujelm'],[3760, 1216],[3772, 1240],['Nujelm'],[3772, 1220],[3776, 1236],['Nujelm'],[3776, 1224],[3784, 1232],['Nujelm'],[3728, 1248],[3744, 1272],['Nujelm'],[3744, 1264],[3752, 1272],['Nujelm'],[3744, 1248],[3752, 1256],['Moonglow'],[4535, 844],[4555, 847],['Moonglow'],[4530, 847],[4561, 908],['Moonglow'],[4521, 914],[4577, 963],['Moonglow'],[4278, 915],[4332, 934],['Moonglow'],[4283, 944],[4336, 1017],['Moonglow'],[4377, 1015],[4436, 1052],['Moonglow'],[4367, 1050],[4509, 1195],['Moonglow'],[4539, 1036],[4566, 1054],['Moonglow'],[4517, 1053],[4540, 1075],['Moonglow'],[4389, 1198],[4436, 1237],['Moonglow'],[4466, 1211],[4498, 1236],['Moonglow'],[4700, 1108],[4717, 1126],['Moonglow'],[4656, 1127],[4682, 1140],['Moonglow'],[4678, 1162],[4703, 1187],['Moonglow'],[4613, 1196],[4636, 1218],['Moonglow'],[4646, 1212],[4660, 1229],['Moonglow'],[4677, 1214],[4703, 1236],['Moonglow'],[4622, 1316],[4644, 1340],['Moonglow'],[4487, 1353],[4546, 1374],['Moonglow'],[4477, 1374],[4546, 1409],['Moonglow'],[4659, 1387],[4699, 1427],['Moonglow'],[4549, 1482],[4578, 1509],['Moonglow'],[4405, 1451],[4428, 1474],['Moonglow'],[4483, 1468],[4504, 1481],['Moonglow'],[4384, 1152],[4392, 1176],['Moonglow'],[4392, 1160],[4408, 1168],['Moonglow'],[4400, 1152],[4408, 1160],['Moonglow'],[4480, 1056],[4488, 1072],['Moonglow'],[4488, 1060],[4492, 1068],['Moonglow'],[4476, 1060],[4480, 1068],['Magincia'],[3653, 2046],[3680, 2094],['Magincia'],[3752, 2046],[3804, 2094],['Magincia'],[3680, 2045],[3752, 2094],['Magincia'],[3652, 2094],[3812, 2274],['Magincia'],[3649, 2256],[3703, 2303],['Magincia'],[3680, 2152],[3704, 2160],['Magincia'],[3720, 2216],[3736, 2232],['Delucia'],[5123, 3942],[5315, 4064],['Delucia'],[5147, 4064],[5272, 4084],['Delucia'],[5235, 3930],[5315, 3942],['Delucia'],[5194, 4053],[5204, 4073],['Papua'],[5639, 3095],[5831, 3318],['Papua'],[5831, 3237],[5851, 3267],['Papua'],[5757, 3150],[5781, 3174],['PalaceofParoxysmus'],[6191, 311],[6561, 671],['Moongates'],[1330, 1991],[1343, 2004],['Moongates'],[1494, 3767],[1506, 3778],['Moongates'],[2694, 685],[2709, 701],['Moongates'],[1823, 2943],[1834, 2954],['Moongates'],[761, 741],[780, 762],['Moongates'],[638, 2062],[650, 2073],['Moongates'],[4459, 1276],[4475, 1292],['Moongates'],[3554, 2132],[3572, 2150]]

def InGuardLines(x,y):
    if x is None:
        x = Player.Position.X
    if y is None:
        y = Player.Position.Y
            
    i = 0
    while i< len(guardlines):
        Px = guardlines[i+1][0]
        Py = guardlines[i+1][1]
        Rx = guardlines[i+2][0]
        Ry = guardlines[i+2][1]
        if( ( x <= max(Px, Rx)) and (x >= min(Px, Rx)) and (y <= max(Py, Ry)) and (y >= min(Py, Ry)) ):
            return True
        i = i + 3
    return False

def MultiTrapPouchUse():
    pouches = []
    try:
        with open(str(Misc.CurrentScriptDirectory())+'\\'+Player.Name+"-pouches.txt", 'r') as pouches_file:
            # Read and print the entire file line by line
            for line in pouches_file:
                for item in Player.Backpack.Contains:
                    if "pouch" in str(item) and str(item.Serial) in str(line):
                        pouches.append(line.rstrip())
    except EnvironmentError:
        pouches_file = open(str(Misc.CurrentScriptDirectory())+'\\'+Player.Name+"-pouches.txt", 'w')
    
    with open(str(Misc.CurrentScriptDirectory())+'\\'+Player.Name+"-pouches.txt", 'w') as pouches_file:
        for item in Player.Backpack.Contains:
            if "pouch" in str(item) and str(item.Serial) not in str(pouches):
                pouches.append(str(item.Serial) + ", False")
        used = False
        i = -1
        for pouch in pouches:
            i += 1
            if "True" in str(pouch):
                #Player.HeadMessage( 13, "USING POUCH")
                Items.UseItem(int(pouch.split(',')[0]))
                Misc.Pause(600)
                pouches[i] = str(pouch.split(',')[0]) + ", False" 
                used = True
                break
        for pouch in pouches:
            pouches_file.write(str(pouch))
            pouches_file.write("\n")
        if not used and Timer.Check("pouches") == False:
            Misc.SendMessage("[DANGER] NO POUCHES TRAPPED")
            Timer.Create("pouches",3000)
    return        
 
def CountTrapPouchUse():
    pouches = 0
    try:
        with open(str(Misc.CurrentScriptDirectory())+'\\'+Player.Name+"-pouches.txt", 'a+') as pouches_file:
            pouches_file.seek(0)
            # Read and print the entire file line by line
            for line in pouches_file:
                if "True" in str(line.rstrip()):
                    pouches+=1
            return pouches   
    except EnvironmentError:
        pouches_file = open(str(Misc.CurrentScriptDirectory())+'\\'+Player.Name+"-pouches.txt", 'w')

        
if __name__ == '__main__':
    while True:
        # Auto chug strength and agility pots when target is close enough
        mob = Mobiles.FindBySerial(Target.GetLast())
        Misc.Pause(10)
        
        # Do not interrupt if target is up or player is invisible
        if not Player.Visible or Target.HasTarget() or Player.IsGhost:
            continue
            
        # Handle bushido mage for keeping counter attack buff activated    
        if Player.GetSkillValue('Bushido') > 50 and not Player.SpellIsEnabled('Counter Attack') and mob is not None:
            Spells.CastBushido("Counter Attack")
            Misc.Pause(600) 
        
        # Handle bushido mage for keeping counter attack buff activated    
        if Player.GetSkillValue('Bushido') > 50 and not Player.SpellIsEnabled('Lightning Strike') and mob is not None:
            Spells.CastBushido("Lightning Strike")
            Misc.Pause(600)     
            
        
        if mob is not None and auto_chug_pots:
            if Player.DistanceTo(mob) < 16:
                #Player.HeadMessage(13,mob.Name)
                if Player.Str < 117 and not Target.HasTarget():
                    Items.UseItemByID(0x0F09)
                    Misc.Pause(600)
                
                if Player.Dex < 52 and not Target.HasTarget():
                    Items.UseItemByID(0x0F08)
                    Misc.Pause(600)
        
  
        #if Player.GetItemOnLayer("LeftHand") is not None:
        #    if Items.GetPropStringList(Player.GetItemOnLayer("LeftHand")) is not None and 'two-handed' in Items.GetPropStringList(Player.GetItemOnLayer("LeftHand")) and 'Balanced' not in Items.GetPropStringList(Player.GetItemOnLayer("LeftHand")):
        #        Items.WaitForProps(Player.GetItemOnLayer("LeftHand"),600)
        #        Misc.SendMessage(str(Items.GetPropStringList(Player.GetItemOnLayer("LeftHand"))))
        #if Player.GetItemOnLayer("LeftHand") is not None:
        #    if 'two-handed' in Items.GetPropStringList(Player.GetItemOnLayer("LeftHand")) and 'Balanced' not in Items.GetPropStringList(Player.GetItemOnLayer("LeftHand")):
        #        if auto_chug_pots:
        #            auto_chug_pots = False
        #    else:
        #        auto_chug_pots = True
                
        
            
        # ---------------------------------------------------------------------
        # --------------------------- ALERTS ----------------------------------
        # ---------------------------------------------------------------------

        #CHECKING FOR ESSENTIAL PVP RESOURCES AND ALERT       
        if not Timer.Check("timer_warning"):
            Timer.Create("timer_warning", 10000)
            Misc.SendMessage("[Running]", 12)
            Misc.Pause(50)
            # CHECKING FOR ---> BANDAGES <----  
            bands = Items.BackpackCount(0xe21, -1) 
            if bands == 0:
                #Player.HeadMessage( 32, "[DANGER] OUT OF BANDAGES!")
                Misc.Pause(10)
            else:
                if bands < 10:
                    Player.HeadMessage( 36, "[Alert] Bandages!")
                    Misc.Pause(10)
                elif bands < 20:
                    #Player.HeadMessage( 52, "[Warning] Bandages!")  
                    Misc.Pause(10)
            # CHECKING FOR ---> REFRESH POTS <----
            refresh = Items.BackpackCount(0xf0b, -1) 
            if refresh == 0:
                Misc.SendMessage("[DANGER] OUT OF REFRESH!", 32)
                Misc.Pause(10)
            else:
                if refresh < 10:
                    Misc.SendMessage("[Alert] Refresh pots!", 32)
                    Misc.Pause(10)
                elif refresh < 20:
                    Misc.SendMessage( "[Warning] Refresh pots!", 32)     
                    Misc.Pause(10)
            # CHECKING FOR ---> POUCHES <----
            if CountTrapPouchUse() == 0:
                Misc.SendMessage( "[DANGER] POUCH NOT TRAPPED", 32)
                Misc.Pause(10)
            if not auto_chug_pots:
                Misc.SendMessage("Unbalanced, autopotions off", 32)
                Misc.Pause(10)
            if Player.Str < 117 and not Target.HasTarget():
                Misc.SendMessage("STR Low", 32)
                Misc.Pause(10)
                
            if Player.Dex < 52 and not Target.HasTarget():
                Misc.SendMessage("Dex Low", 32)
                Misc.Pause(10)
        # ---------------------------------------------------------------------
        # --------------------------- APPLE -----------------------------------
        # ---------------------------------------------------------------------      
        if Player.YellowHits:
            if not Timer.Check("timer_apple"):
                if Player.Hits <= 50:
                    Misc.Pause(10)
                    apple = Items.BackpackCount(0x2fd8, 0x0488) 
                    if(apple > 0): 
                        Items.UseItemByID(0x2fd8,0x0488)
                        Misc.Pause(600)
                        Timer.Create("timer_apple", 120000) 
                        Timer.Create("timer_mortal",1) 
                        
        # ---------------------------------------------------------------------
        # --------------------------- HEALING ---------------------------------
        # ---------------------------------------------------------------------
        if Player.YellowHits and not Timer.Check("timer_mortal"):
            Timer.Create("timer_mortal",8000)
        if not Player.YellowHits and Timer.Check("timer_mortal"):
            Timer.Create("timer_mortal",1) 
        
        bandages = Items.BackpackCount(0x0E21, -1) 
        if(bandages > 0): 
            if not Player.BuffsExist("Healing"):
                if not Player.YellowHits:
                    if Player.Poisoned or Player.Hits < Player.HitsMax*0.95:
                        #Player.HeadMessage(13,"STARTING BANDAGE")
                        last = Target.GetLast()
                        Items.UseItemByID(0x0E21, -1 )
                        Target.WaitForTarget( 500, True )
                        Target.Self()
                        Target.SetLast(last)
                        Timer.Create("timer_healing", 10000)
                        Misc.Pause(600)
                elif Timer.Remaining("timer_mortal") < 5000:
                #Player.HeadMessage(23,"STARTING BANDAGE COM MORTAL")
                    last = Target.GetLast() 
                    Items.UseItemByID( 0x0E21, -1 )
                    Target.WaitForTarget( 400, True )
                    Target.Self()
                    Target.SetLast(last)
                    Timer.Create("timer_healing", 10000)
                    Misc.Pause(600)
            elif Player.YellowHits and Timer.Remaining("timer_healing") > 9000 and Timer.Remaining("timer_mortal") > 5000:
                if Timer.Remaining("timer_mortal") < 5000:
                #Player.HeadMessage(45,"RE-STARTING BANDAGE COM MORTAL")
                    last = Target.GetLast() 
                    Items.UseItemByID( 0x0E21, -1 )
                    Target.WaitForTarget( 400, True )
                    Target.Self()
                    Target.SetLast(last)
                    Timer.Create("timer_healing", 10000)
                    Misc.Pause(600)
                    
            elif Journal.Search('fingers slip!') and Timer.Remaining("timer_healing") > 8000: 
                Journal.Clear()
                Player.HeadMessage(13,"RESTARTING BANDAGE")
                last = Target.GetLast() 
                Items.UseItemByID( 0x0E21, -1 )
                Target.WaitForTarget( 400, True )
                Target.Self()
                Target.SetLast(last)
                Timer.Create("timer_healing", 10000)
                Misc.Pause(600)
              
            elif Journal.Search('DEFENSE CHANCE REDUCED'): 
                Journal.Clear()
                Misc.SendMessage("DEFENSE REDUCED", 22)
                Misc.Pause(600)
        # ---------------------------------------------------------------------  
        # ------------------------ CURE / HEAL --------------------------------
        # ---------------------------------------------------------------------
        #if Player.Poisoned and Player.Hits < Player.HitsMax*0.75 and auto_chug_pots:
            #cure = Items.BackpackCount(0xf07, -1) 
            #if(cure > 3): 
                #Items.UseItemByID(0xf07,-1)
                #Misc.Pause(600)            
        if not Player.YellowHits and Player.Hits < 115  and auto_chug_pots:
            if not Timer.Check("timer_healpot"):
                heal = Items.BackpackCount(0xf0c, -1) 
                if(heal > 3): 
                    Items.UseItemByID(0xf0c,-1)
                    Timer.Create("timer_healpot", 10100) 
                    Misc.SendMessage("Heal pot!!", 38)
                    Misc.Pause(600)
        
        # ---------------------------------------------------------------------
        # --------------------------- REFRESH ---------------------------------
        # ---------------------------------------------------------------------
        if Player.Stam < Player.StamMax*0.7 and auto_chug_pots:
            refresh = Items.BackpackCount(0xf0b, -1) 
            if(refresh > 3): 
                Items.UseItemByID(0xf0b,-1)
                Misc.SendMessage("Refresh pot!!" , 62)
                Misc.Pause(600)
        
            
        # ---------------------------------------------------------------------
        # --------------------- CONFLAG if enemy Paralyze ---------------------
        # ---------------------------------------------------------------------
        if auto_conflag and mob is not None and mob.Paralized and mob.Hits < mob.HitsMax*0.4 and mob.IsHuman and Player.DistanceTo(mob) <= 12 and Items.BackpackCount(0x0F06, -1) > 0:
            guardszone = InGuardLines(mob.Position.X, mob.Position.Y)
            if not guardszone:
                conflag = Items.BackpackCount(0x0F06, -1) 
                if(conflag > 0 and not Timer.Check("timer_conflag")): 
                    Timer.Create("timer_conflag", 30000)
                    Items.UseItemByID(0x0F06)
                    Target.WaitForTarget(200,True)
                    Target.TargetExecute(mob)
                    Misc.Pause(600)
        # ---------------------------------------------------------------------
        # --------------------- Chug poison pot when EO -----------------------
        # ---------------------------------------------------------------------
        if Player.BuffsExist("Evil Omen") and not Player.Poisoned and auto_chug_pots:
            lesser_poison_pot = Items.BackpackCount(0x0F0A, -1) 
            if(lesser_poison_pot > 0): 
                Items.UseItemByID(0x0F0A)
                Misc.Pause(600)

        Misc.Pause(10)
        # ---------------------------------------------------------------------
        # ----------------------- Auto-Pouch if Paralyze ----------------------
        # ---------------------------------------------------------------------
        if Player.Paralized and Player.Hits > 80 and not Timer.Check("timer_pouch") and auto_pouch:
            Timer.Create("timer_pouch", 3000)
            MultiTrapPouchUse()

        Misc.Pause(10)           

