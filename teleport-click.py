def Teleport():
    if not Target.HasTarget("Neutral"):
        Target.Cancel()
    if Target.HasTarget():
        mouse = Misc.MouseLocation()
        Misc.SendMessage("{}".format(mouse))
        Misc.LeftMouseClick(mouse.X,mouse.Y,False)
    else:
        if not Player.Visible and Player.GetSkillValue("ninjitsu") >= 100 and Player.GetSkillValue("hiding") >= 100:
            Spells.CastNinjitsu("Shadowjump")
        else:    
            if Items.BackpackCount(0x1F42, 0) > 0:
                Items.UseItemByID(0x1F42, 0)
            else:
                Spells.CastMagery("Teleport")
         
Teleport()