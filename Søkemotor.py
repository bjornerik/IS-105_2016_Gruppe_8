import Ordliste as ol
from timeit import default_timer as timer

liste = ol.Ordliste
def fast_engine(liste, word):
    for item in liste:
        if item == word:
            print word + " er funnet i listen."
            return True
    print word + " er ikke funnet i listen"
    return False

def slow_engine(liste, word):
    boolean = False
    for item in liste:
        if item == word:
            boolean = True
    return boolean


def test():
    fast_engine(liste,"hei")
    
def test2():
    slow_engine(liste, "hei")
    

start = timer()   
test()
end = timer()
start2 = timer()
test2()
end2 = timer()
print "Tid brukt med fast_engine er %f" %(end-start)
print "Tid bruk med slow_engine er %f" %(end2-start2)