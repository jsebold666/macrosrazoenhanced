enemy = Mobiles.FindBySerial(Target.GetLast())

Spells.CastMagery( 'Teleport' )
Target.WaitForTarget( 2000, False )
Target.TargetExecuteRelative(enemy, 11 )