import time
import datetime
def journalStatus(journalStates, clear=True):
    for state in journalStates:
        texts = journalStates[state]
        for text in texts:
            if Journal.Search(text):
                if clear: Journal.Clear()
                return state
    return None
    
def waitForSpell(timeout,target=None,msgs=None):
    if timeout is None: timeout = 0.65
    jStatus = {
        'reags': ['More reagents are needed for this spell'],
        'mana': ['Insufficient mana for this spell.'],
        'casting':  ['You are already casting'],
        'fail':  ['The spell fizzles','Your concentration is disturbed'],
        'wait': ['You have not yet recovered from casting a spell'],
        'away': ['This is too far away']
    }
    startMana = Player.Mana
    while time.time()< timeout:
        found = journalStatus(jStatus)
        if found in ['reags','mana','fail','casting','wait']:
            return found
                
        if target is None:
            if Player.Mana < startMana: break
            Misc.SendMessage("aguarda o wait: ")
        return 'wait'
    return 'success'
    

def castSpell(name,timeout,target):
    if timeout is None: timeout = 0.5
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
    while time.time() < endtime:
        if not isCasting:
            Journal.Clear()
            Spells.CastMagery(name)
            isCasting = True
        #
        found = waitForSpell(endtime,target=target,msgs='aa')
        if found == 'success': 
            isCasting = False
            return True
        elif found == 'timeout': 
            isCasting = False
            return False
        elif found == 'wait':
            isCasting = True
            continue
        elif found == 'fail':
            isCasting = False
            Timer.Create("fireball", 1)
            continue
        else:
            isCasting = False
            continue
    return True
    
    

def WE_CL():
    if Target.HasTarget():
        Target.LastQueued()
    if Timer.Check("fireball") == False or Timer.Remaining("fireball") == 0:
        Target.LastQueued()
        res=castSpell('Magic Arrow', timeout = 0.65, target =  0)
        Misc.Pause(20)
        if res:
            Misc.Pause(50)
        Timer.Create("fireball", 578)
        Target.ClearQueue()
        return
    else:
        t0 = time.time()
        Target.LastQueued()
        
        res = castSpell('Fireball', timeout = 1.1,  target = 0)
        Misc.Pause(20)
        if res:
            Misc.Pause(30)
        Target.ClearQueue()
        t1 = time.time()
        diff = t1 - t0
        med = (diff * 1000) / 2
        Misc.SendMessage( "Tempo da operacao: " + str(med) + " ms" )
        return
    return

    
WE_CL()
Misc.Pause(10)