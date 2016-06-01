from timeit import default_timer as timer
import time
import random

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

def searchFast(n,k):
    total = 0.0
    liste = list(range(n))
    start = timer()   
    fast_engine(liste,k)
    end = timer()
    total = total + (end-start)
    print ("Gjennomsnittlig tid for fast_engine er %f" %(total))
    
def searchSlow(n,k):
    total = 0.0
    liste = list(range(n))
    start = timer()   
    slow_engine(liste,k)
    end = timer()
    total = total + (end-start)
    print ("Gjennomsnittlig tid for slow_engine er %f" %(total))
    
searchFast(100, 1)
searchSlow(100, 1)
searchFast(100, 100)
searchSlow(100,100)
searchFast(100, random.randint(1,100))
searchSlow(100, random.randint(1,100))
searchFast(1000, 1)
searchSlow(1000, 1)
searchFast(1000,1000)
searchSlow(1000,1000)
searchFast(1000, random.randint(1,1000))
searchSlow(1000, random.randint(1,1000))
searchFast(10000, 1)
searchSlow(10000, 1)
searchFast(10000,10000)
searchSlow(10000,10000)
searchFast(10000, random.randint(1,10000))
searchSlow(10000, random.randint(1,10000))
searchFast(100000, 1)
searchSlow(100000, 1)
searchFast(100000,100000)
searchSlow(100000,100000)
searchFast(100000, random.randint(1,100000))
searchSlow(100000, random.randint(1,100000))