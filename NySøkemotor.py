import Ordliste as ol
from timeit import default_timer as timer

liste = ol.Ordliste
def fast_engine(liste, word):
    for item in liste:
        if item == word:
            return True
    return False

def slow_engine(liste, word):
    boolean = False
    for item in liste:
        if item == word:
            boolean = True
    return boolean

def test():
    total = 0.0
    for i in range(1000):
        start = timer()   
        fast_engine(liste,"hei")
        end = timer()
        total = total + (end-start)
    print "Gjennomsnittlig tid for fast_engine er %f" %(total/1000)
    
def test2():
    total = 0.0
    for i in range(1000):
        start = timer()   
        slow_engine(liste,"hei")
        end = timer()
        total = total + (end-start)
    print "Gjennomsnittlig tid for slow_engine er %f" %(total/1000)
    

test()
test2()