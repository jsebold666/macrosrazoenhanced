mob = 0x0008321B  # mob or player serial

while True:
    Player.UseSkill('Anatomy')
    Target.WaitForTarget(3500)
    if Target.HasTarget():
        Target.TargetExecute(mob)
    Misc.Pause