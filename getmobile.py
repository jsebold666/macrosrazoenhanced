from datetime import datetime, timedelta
from System.Collections.Generic import List
from System import Byte

timer_stuck = datetime.now()

def FindEnemy():
    tfilter = Mobiles.Filter()
    tfilter.Enabled = True
    tfilter.RangeMin = 0
    tfilter.RangeMax = 5
    tfilter.IsHuman = False
    tfilter.IsGhost = False
    #Notorieties: blue = 1, green = 2, gray = 3, gray crim = 4, orange = 5, red = 6, yellow = 7
    tfilter.Notorieties = List[Byte](bytes([3,4,5,6]))
    tfilter.Friend = False
    enemies = Mobiles.ApplyFilter(tfilter)
    Misc.Pause(50)

    return enemies

def attackEnemy():
    timer_stuck = datetime.now()
    timer_walking = datetime.now()
    Misc.Pause(200)
    mob = None
    while not Player.IsGhost:
        if mob is None or Mobiles.FindBySerial(mob.Serial) is None:
            enemies = FindEnemy()
        elif (mob is not None) and (Player.DistanceTo(mob) > 5):
            if ( datetime.now() > timer_walking + timedelta(seconds=5)):
                timer_walking = datetime.now()
                Player.HeadMessage(53, 'Approaching enemy')
                Misc.Pause(100)
                Player.HeadMessage(70, 'Done!!')
        enemies = FindEnemy()
        if len(enemies) < 2:
            
            Target.ClearLastandQueue()
            Target.Cancel()
        if len(enemies) > 0:    
            nearest = enemies[0]
            for enemy in enemies:
                if Player.DistanceTo(enemy) < Player.DistanceTo(nearest):
                    nearest = enemy
                if (timer_stuck + timedelta(seconds=10) < datetime.now() or mob and mob.IsGhost):
                    Misc.IgnoreObject(mob)
                    mob = None
                    Player.HeadMessage(34, 'Mob ignored')


            if mob != nearest:
                timer_stuck = datetime.now()
                mob = nearest
                Player.Attack(mob)
                Player.HeadMessage(53, 'Attack enemy')
            
        
attackEnemy()