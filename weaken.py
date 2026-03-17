import time

def journalStatus(journalStates, clear=True):
    for state in journalStates:
        texts = journalStates[state]
        for text in texts:
            if Journal.Search(text):
                if clear: Journal.Clear()
                return state
    #
    return None


    
def waitForSpell(timeout=None,target=None,msgs=None):
    if timeout is None: timeout = 3
    #
    jStatus = {
        'reags': ['More reagents are needed for this spell'],
        'mana': ['Insufficient mana for this spell.'],
        'casting':  ['You are already casting'],
        'fail':  ['The spell fizzles','Your concentration is disturbed'],
        'wait': ['You have not yet recovered from casting a spell'],
        'away': ['This is too far away']
    }
    startMana = Player.Mana
    #i = 0
    while time.time()<timeout:
        #i += 1
        #if i % 10000 == 0:
        #    Misc.SendMessage("TA DENTRO DO WHILE WAITFORSPELL: " + str(time.time()) +" "+ str(endtime))
        found = journalStatus(jStatus)
        if found in ['reags','mana','fail','casting','wait']:
            return found
                
        if target is None:
            if Player.Mana < startMana: break
        #
        
        Misc.Pause(10)
    #        
    
    #Target.Cancel()
    #
    return 'success'
    

def castSpell(name,timeout=None,target=None,msgs=None,retry=None,noWait=False):
    if timeout is None: timeout = 3
    if retry is None: retry=False
    #
    
    jStatus = {
        'reags': ['More reagents are needed for this spell'],
        'mana': ['Insufficient mana for this spell.'],
        'casting':  ['You are already casting'],
        'fail':  ['The spell fizzles','Your concentration is disturbed'],
        'wait': ['You have not yet recovered from casting a spell.'],
        'away': ['This is too far away']
    }
    
    
    isCasting = False
    endtime = time.time() + timeout
    while time.time()<endtime:
        if not isCasting:
            Journal.Clear()
            Spells.CastMagery(name)
            if noWait: return True
            isCasting = True
        #
        found = waitForSpell(endtime,target=target,msgs=msgs)
        if found == 'success': 
            return True
        elif found == 'timeout': 
            return False
        elif found == 'wait' and retry:
            isCasting = False
            continue
            
            #Player.HeadMessage(40,"FAIL: {}".format(name)+" "+found)
        Misc.Pause(10)
        return False
    #
    return True
    
    

def CLUSMY_WEAKEN():
    if Target.HasTarget():
        Target.LastQueued()
            
    
    if Timer.Check("cu") == False:
        Target.LastQueued()
        res=castSpell('Clumsy', timeout = 0.6, target =  0)
        if res:
            Target.LastQueued()
            Misc.Pause(50)
            Timer.Create("cu", 710)
        return
    else:
        Target.LastQueued()
        res = castSpell('Weaken', timeout = 0.6,  target = 0)
        if res:
            Target.LastQueued()
            Misc.Pause(30)
        else:
            Timer.Create("cu", 1)
        return
    return

    
CLUSMY_WEAKEN()
Misc.Pause(10)import time

def journalStatus(journalStates, clear=True):
    for state in journalStates:
        texts = journalStates[state]
        for text in texts:
            if Journal.Search(text):
                if clear: Journal.Clear()
                return state
    #
    return None


    
def waitForSpell(timeout=None,target=None,msgs=None):
    if timeout is None: timeout = 3
    #
    jStatus = {
        'reags': ['More reagents are needed for this spell'],
        'mana': ['Insufficient mana for this spell.'],
        'casting':  ['You are already casting'],
        'fail':  ['The spell fizzles','Your concentration is disturbed'],
        'wait': ['You have not yet recovered from casting a spell'],
        'away': ['This is too far away']
    }
    startMana = Player.Mana
    #i = 0
    while time.time()<timeout:
        #i += 1
        #if i % 10000 == 0:
        #    Misc.SendMessage("TA DENTRO DO WHILE WAITFORSPELL: " + str(time.time()) +" "+ str(endtime))
        found = journalStatus(jStatus)
        if found in ['reags','mana','fail','casting','wait']:
            return found
                
        if target is None:
            if Player.Mana < startMana: break
        #
        
        Misc.Pause(10)
    #        
    
    #Target.Cancel()
    #
    return 'success'
    

def castSpell(name,timeout=None,target=None,msgs=None,retry=None,noWait=False):
    if timeout is None: timeout = 3
    if retry is None: retry=False
    #
    
    jStatus = {
        'reags': ['More reagents are needed for this spell'],
        'mana': ['Insufficient mana for this spell.'],
        'casting':  ['You are already casting'],
        'fail':  ['The spell fizzles','Your concentration is disturbed'],
        'wait': ['You have not yet recovered from casting a spell.'],
        'away': ['This is too far away']
    }
    
    
    isCasting = False
    endtime = time.time() + timeout
    while time.time()<endtime:
        if not isCasting:
            Journal.Clear()
            Spells.CastMagery(name)
            if noWait: return True
            isCasting = True
        #
        found = waitForSpell(endtime,target=target,msgs=msgs)
        if found == 'success': 
            return True
        elif found == 'timeout': 
            return False
        elif found == 'wait' and retry:
            isCasting = False
            continue
            
            #Player.HeadMessage(40,"FAIL: {}".format(name)+" "+found)
        Misc.Pause(10)
        return False
    #
    return True
    
    

def CLUSMY_WEAKEN():
    if Target.HasTarget():
        Target.LastQueued()
            
    

    Target.LastQueued()
    res = castSpell('Weaken', timeout = 0.6,  target = 0)
    if res:
        Target.LastQueued()
        Misc.Pause(30)
    else:
        Timer.Create("cu", 1)
    return


    
CLUSMY_WEAKEN()
Misc.Pause(10)