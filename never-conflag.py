potID = 0x0F06

Player.WeaponSecondarySA()
if Items.BackpackCount(potID, -1) == 0:
    Player.HeadMessage(30, 'Out of Conflag pots')
    Misc.Pause(10)
else:
    Journal.Clear()
    enemy = Mobiles.FindBySerial(Target.GetLast())
    Misc.Pause(10)
    Misc.Pause(1000)
    if enemy != None:
        if Player.DistanceTo(enemy) <= 10:
            Items.UseItemByID(potID)
            Misc.Pause(100)
            if Journal.Search("You cannot use that"):
                Misc.Pause(10)
            Target.WaitForTarget(50)
            Player.HeadMessage(30, 'CONFLAG ENEMY')
            Target.TargetExecute(enemy)
            Spells.CastMagery('Energic Bolt')
            Target.WaitForTarget(800, True)
            Target.LastQueued()
            Misc.Pause(600)



