import time

# Legger string i variabel for bruk i algoritmen.
# Lager en tuple av mulige baereobjekter for bonden
farmer,chicken,grain,fox=("farmer","chicken","grain","fox")
carryables=(chicken,grain,fox,None)

# Definerer forbudte sett
forbiddens=(set((chicken,grain)), set((fox,chicken)))

# Sjekker om forbudte tilstander skjer.
def mayhem(cfg):
    for shore in cfg[0]:
        if farmer not in shore:
            for forbidden in forbiddens:
                if shore.issuperset(forbidden):
                    return True
    return False

#Definererer naar spillet er ferdig
def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Definerer baaten som bonden kan ta med items i.
# Bonden maa ikke ha med noen items, man tolker det da som item "None"
# Til slutt returneres den nye tilstanden, hvis ikke tilstanden er mulig, returneres "None".
def ferry(cfg,item):
    desc = ""
    left,right=[set(x) for x in cfg[0]] # Lager kopier av sidene, da de vil bli endret.
    # Bestemmer hvor bonden er, og hvor han skal.
    if farmer in left:
        src,dst=left,right
        desc+= "->"
    else:
        src,dst=right,left
        desc+= "<-"
    # Sjekker om item'et bonden skal ha, faktisk er paa bondens side.
    if item and not item in src:
        return None
    
    src.remove(farmer)
    dst.add(farmer)
    if item:
        src.remove(item)
        dst.add(item)
        desc+=" with the "+item
    else:
        desc+=" alone"
    return ((left,right),desc) # return the resulting configuration

# pretty-print a configuration
def printcfg(cfg,level=0):
    left,right=cfg[0]
    verdict="(Not allowed)" if mayhem(cfg) else "(Ok)"
    print ("    "*level,", ".join(left),"  ~~~  ",", ".join(right),cfg[1],verdict)

# given a certain configuration, generate the configurations that could result from it
def onegeneration(cfg):
    followups=[]
    for item in carryables:
        followup=ferry(cfg,item)
        if not followup: continue
        followups.append(followup)
    return followups

# recursively generate from a given configuration
def generate(cfg,level=0):
    solutionstack.extend([None]*(level-len(solutionstack)+1))
    solutionstack[level]=cfg[1]
    printcfg(cfg,level)
    childs=onegeneration(cfg)
    for child in childs:
        if mayhem(child): # skip configurations which are not allowed
            continue
        if child[0] in previouscfgs: # skip shore configurations which have been seen before
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)

# starting configuration
cfg=((set((farmer,chicken,grain,fox)), set()),"")

# this records any previously encountered configurations
previouscfgs=[cfg[0]]

# keep a solution stack for later printing
solutionstack=[]

# go!
print ("Trace of the recursive solution-finding process:")
generate(cfg)

