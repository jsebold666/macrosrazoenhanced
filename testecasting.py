SharedDataName = "Magic Arrow"

if not Misc.CheckSharedValue(SharedDataName):
    Misc.SetSharedValue(SharedDataName,"Magic Arrow")

def controlSpell():
    return Misc.ReadSharedValue(SharedDataName)

    
def checkPoint(spell):
    Misc.SetSharedValue(SharedDataName,spell)
    '
enemy = Mobiles.FindBySerial(Target.GetLast())

    if Player.InRangeMobile(enemy,1):
        Spells.CastMagery("Harm")
        Target.WaitForTarget(5000,True)''
        Target.TargetExecute(enemy)
    else:
        spellcast = controlSpell()
        
        Spells.CastMagery(spellcast)
        Target.WaitForTarget(5000,True)
        Target.TargetExecute(enemy)

        
        if controlSpell() == "Magic Arrow":
           checkPoint("Fireball")
        else:
           checkPoint("Magic Arrow")