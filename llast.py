
def CountTrapPouchUse():
    mob = Mobiles.FindBySerial(Target.GetLast())
    if mob is not None:
        Target.TargetExecuteRelative( mob.Serial, 11)
        
CountTrapPouchUse()