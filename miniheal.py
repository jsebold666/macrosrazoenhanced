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



def castSpell(name,timeout=None,target=None,msgs=None,retry=None,noWait=False):
    if timeout is None: timeout = 3
    if retry is None: retry=False
    #
    
    jStatus = {
        'reags': ['More reagents are needed for this spell'],
        'mana': ['Insufficient mana for this spell.'],
        'casting':  ['You are already casting'],
        'fail':  ['The spell fizzles','Your concentration is disturbed'],
        'wait': ['You have not yet recovered from casting a spell.']
    }
    
    
    isCasting = False
    while True:
        if not isCasting:
            Journal.Clear()
            Spells.CastMagery(name)
            if noWait: return True
            isCasting = True
        #
        found = waitForSpell(timeout,target=target,msgs=msgs)
        if found == 'success': return True
        if found == 'wait' and retry:
            isCasting = False
            continue
            
        Player.HeadMessage(40,"FAIL: {}".format(name)+" "+found)
        return False
    #
    return True
    
    
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
    endtime = time.time() + timeout
    while time.time()<endtime:
        
        found = journalStatus(jStatus)
        if found in ['reags','mana','fail','casting','wait']:
            return found
                
        if target is None:
            if Player.Mana < startMana: break
        #
        elif Target.HasTarget():
            if target == 'self':
                Target.SelfQueued()
            elif target==0:
                Target.LastQueued()
            elif target>0:
                Target.TargetExecute(target)
            break
    #        
    Target.Cancel()
    #
    return 'success' if time.time()<endtime else 'timeout'
    

def wait_for_target(timeout):
    Journal.Clear()
    time = 0
    while time <= timeout:
        Misc.Pause(10)
        time += 10
        if Target.HasTarget():
            #Player.HeadMessage(13,"SUCCESS: TARGET")
            return True
        if Journal.Search("disturbed"):
            #Player.HeadMessage(40,"FAIL: {disturbed}")
            return False
        if Journal.Search("fizzles"):
            #Player.HeadMessage(40,"FAIL: {fizzles}")
            return False
        if Journal.Search("recovered"):
            #Player.HeadMessage(40,"FAIL: {recovered}")
            return False
        if Journal.Search("mana"):
            #Player.HeadMessage(40,"FAIL: {mana}")
            return False
        if Journal.Search("away"):
            #Player.HeadMessage(40,"FAIL: {away}")
            return False
    return True
    
            
def MiniHeal():
    if Target.HasTarget():
        Target.Cancel()
    if not Player.YellowHits:
        if not Player.Poisoned:
            Spells.CastMagery("Heal")
            #Target.WaitForTarget(700, True)
            if wait_for_target(550):
                Target.SelfQueued()
                Misc.Pause(30)
            return
        elif Timer.Check("cure") == False:
            Spells.CastMagery("Cure")
            #Target.WaitForTarget(700, True)
            if wait_for_target(600):
                Target.SelfQueued()
                Misc.Pause(30)
                Timer.Create("cure", 300)
            return
    elif Player.GetSkillValue('Bushido') > 50:
        Spells.CastBushido('Confidence')
        Misc.Pause(10)
    return   
    

MiniHeal()
Misc.Pause(50)