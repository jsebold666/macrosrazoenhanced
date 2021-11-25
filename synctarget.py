from datetime import datetime, timedelta, time
from System.Collections.Generic import List
from System import Byte


Journal.Clear()
while True:
    Misc.Pause(100)
    if Journal.SearchByType("","Alliance"):
        line = Journal.GetTextByType("Alliance")
        if len(line) > 0:
            if "Target:" in line[0]:
            #Player.HeadMessage(13,line[0])
                try:
                    serial = int(line[0].split("|")[1])
                    Player.HeadMessage( 14,"* Target Sync *")
                    Target.SetLast(serial)
                    #Player.ChatParty("READY")

                except:
                    Player.HeadMessage( 33,"CANT CONVERT")
                
                Journal.Clear()

Misc.Pause(50)
            