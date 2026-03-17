
def getTarget():
    enemy =  Target.GetTargetFromList("para_enemy")
    
    if enemy == None:
        Player.HeadMessage( 34, "No enemy to target!")
    else:
        mobile = Mobiles.FindBySerial(enemy.Serial)
        Target.SetLast(enemy.Serial)
        Mobiles.Message(enemy, 34 ,"▁▃▅ HERE ▅▃▁ ")
        
getTarget()
Misc.Pause(5)