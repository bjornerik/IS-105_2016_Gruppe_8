farmer,chicken,grain,fox=("farmer","chicken","grain","fox")
carryables=(chicken,grain,fox,None)

forbiddens=(set((chicken,grain)), set((fox,chicken)))

def mayhem(cfg):
    for shore in cfg[0]:
        if farmer not in shore:
            for forbidden in forbiddens:
                if shore.issuperset(forbidden):
                    return True
    return False

def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Let the farmer ferry across the river, taking an item with him.
# 'item' can be None is the farmer is to take nothing with him.
# Return the new configuration, or None is the crossing can't be performed
# because the item is not on the same shore as the farmer.
def ferry(cfg,item):
    left,right=[set(x) for x in cfg[0]] # make copies, because 'left' and 'right' will be mutated
    # determine on which shore the farmer is, and to which shore he will ferry
    if farmer in left:
        src,dst=left,right
    else:
        src,dst=right,left
    # make sure that if there's an item to carry, it is on the same shore as the farmer
    if item and not item in src:
        return None
    # cross the farmer and possibly the item
    desc="The farmer goes -->" if farmer in left else "The farmer goes <--"
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

print ("\nThe solution to the problem:")
for step in solutionstack:
    if step:
        print ("  ",step)