import Ordliste as ol
from timeit import default_timer as timer
import time

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
    for i in range(5):
        start = timer()   
        fast_engine(liste,"abandon")
        end = timer()
        total = total + (end-start)
        time.sleep(1)
    print "Gjennomsnittlig tid for fast_engine er %f" %(total/5)
    
def test2():
    total = 0.0
    for i in range(5):
        start = timer()   
        slow_engine(liste,"abandon")
        end = timer()
        total = total + (end-start)
        time.sleep(1)
    print "Gjennomsnittlig tid for slow_engine er %f" %(total/5)
    

test()
test2()