# -*- coding: utf-8 -*-

class River(object):
    
    river_left = []
    boat = ["boat"]
    river_right = []
    
    # Blir kalt hver gang klassen blir instansiert
    def __init__(self, initialValue): 
        self.startState = initialValue
        self.river_left = self.startState
        self.river_left.append(self.boat)

    def crossriver(self):
        if not ['man'] in self.boat:
            print ("Nobody is rowing")
        else:
            if self.boat in self.river_left:
                self.remove(self.boat, "left")
                if self.boat not in self.river_right:
                    self.add(self.boat, "right")
            elif self.boat in self.river_right:
                self.remove(self.boat, "right")       
                if self.boat not in self.river_left:
                    self.add(self.boat, "left")
    
    def putin(self, item):
        if (item and self.boat in self.river_left) or (item and self.boat in self.river_right):
            if len(self.boat) >= 3:
                print ("The boat is full")
            else:
                if (['man'] not in self.boat) and (len(self.boat) == 2) and (item != ['man']):
                    print ("You can only place one item in addition to man in the boat")
                else:
                    if item in self.river_left:
                        self.remove(item, "left")
                        self.add(item, "boat")
                    elif item in self.river_right:
                        self.remove(item, "right")
                        self.add(item, "boat")
                    else:
                        print ("The item is already in the boat")
        else: 
            print (str(item) + " and the boat needs to be on the same shore")
        
            
    def takeout(self, item):
        if self.boat in self.river_left:
            if item in self.boat:
                self.remove(item, "boat")
                self.add(item, "left")
            else:
                print (str(item) + " is not in the boat")
                
        elif self.boat in self.river_right:
            if item in self.boat:
                self.remove(item, "boat")
                self.add(item, "right")
            else:
                print (str(item) + " is not in the boat")            
            
        
                            
    def view(self):
        # Her implementeres logikken for "vakker" utskrift
        # ...
        print ("** Here is the state of the river-world:")

        a = "** [chicken fox grain man ---\\ \\_ _/ ________________ /---]"
        b = "** [chicken grain man ---\\ \\_ fox _/ ________________ /---]"
        c = "** [chicken fox man ---\\ \\_ grain _/ ________________ /---]"
        d = "** [fox grain man ---\\ \\_ chicken _/ ________________ /---]"
        e = "** [fox grain ---\\ \\_ chicken man _/ ________________ /---]"
        f = "** [fox grain---\\ _________________\\_ chicken man _/ /---]"
        g = "** [fox grain---\\ _________________\\_ chicken _/ /--- man]"
        h = "** [fox grain---\\ _________________\\_ _/ /--- chicken man]"
        i = "** [fox grain---\\ _________________\\_ man _/ /--- chicken]"
        j = "** [fox grain ---\\ \\_ man _/ ________________ /--- chicken]"
        k = "** [fox grain man ---\\ \\_ _/ ________________ /--- chicken]"
        l = "** [fox man ---\\ \\_ grain _/ ________________ /--- chicken]"
        m = "** [fox ---\\ \\_ grain man _/ ________________ /--- chicken]"
        n = "** [fox ---\\ ________________ \\_ grain man _/ /--- chicken]"
        o = "** [fox ---\\ ________________ \\_ grain _/ /--- chicken man]"
        p = "** [fox ---\\ ________________ \\_ _/ /--- chicken man grain]"
        q = "** [fox ---\\ ________________ \\_ man _/ /--- chicken grain]"
        r = "** [fox ---\\ ________________ \\_ chicken _/ /--- man grain]"
        t = "** [fox ---\\ ________________ \\_ man chicken_/ /--- grain]"
        u = "** [fox ---\\ \\_ chicken man _/ ________________ /--- grain]"
        v = "** [fox chicken ---\\ \\_ man _/ ________________ /--- grain]"
        w = "** [fox man ---\\ \\_ chicken _/ ________________ /--- grain]"
        x = "** [fox man chicken ---\\ \\_ _/ ________________ /--- grain]"
        y = "** [man chicken ---\\ \\_ fox _/ ________________ /--- grain]"
        z = "** [chicken ---\\ \\_ fox man _/ ________________ /--- grain]"
        aa = "** [chicken ---\\ ________________ \\_ fox man _/ /--- grain]"
        ab = "** [chicken ---\\ ________________ \\_ fox _/ /--- grain man]"
        ac = "** [chicken ---\\ ________________ \\_ man _/ /--- grain fox]"
        ad = "** [chicken ---\\ ________________ \\_ _/ /--- grain fox man]"
        ae = "** [chicken ---\\ \\_ man _/ ________________ /--- grain fox]"
        af = "** [chicken man ---\\ \\_ _/ ________________ /--- grain fox]"
        ag = "** [man ---\\ \\_ chicken _/ ________________ /--- grain fox]"
        ah = "** [---\\ \\_ man chicken _/ ________________ /--- grain fox]"
        ai = "** [---\\ ________________ \\_ man chicken _/ /--- grain fox]"
        aj = "** [---\\ ________________ \\_ man _/ /--- grain fox chicken]"
        ak = "** [---\\ ________________ \\_ chicken _/ /--- grain fox man]"
        al = "** [grain man ---\\ \\_ fox _/ ________________ /--- chicken]"
        am = "** [grain ---\\ \\_ fox man _/ ________________ /--- chicken]"
        an = "** [grain ---\\ ________________ \\_ fox man _/ /--- chicken]"
        ao = "** [grain ---\\ ________________ \\_ fox _/ /--- chicken man]"
        ap = "** [grain ---\\ ________________ \\_ _/ /--- chicken fox man]"
        aq = "** [grain ---\\ ________________ \\_ chicken _/ /--- man fox]"
        ar = "** [grain ---\\ ________________ \\_ chicken man _/ /--- fox]"
        at = "** [grain ---\\ \\_ chicken man _/ ________________ /--- fox]"
        au = "** [grain man ---\\ \\_ chicken _/ ________________ /--- fox]"
        av = "** [grain man chicken---\\ \\_ _/ ________________ /--- fox]"
        aw = "** [man chicken ---\\ \\_ grain _/ ________________ /--- fox]"
        ax = "** [chicken ---\\ \\_ grain man _/ ________________ /--- fox]"
        ay = "** [chicken ---\\ ________________ \\_ grain man _/ /--- fox]"
        az = "** [chicken ---\\ ________________ \\_ grain _/ /--- fox man]"
        
        # Bruk betingelse og finn ut tilstanden fra database (db, som er en liste av lister)
        # For eksempel, hvis alt er på venstre siden av elven, skriv ut allAtLeft "bilde"
        # Dette er ikke en korrekt kode, - man bør sjekke på flere tilstandsvariabler
        # eller implementere datastrukturer som genererer "bilder" automatisk, basert på innholdet
        # i databasen
        if len(self.river_left) == 5 and len(self.boat) == 1:
            print (a)
        elif (self.boat in self.river_left) and (['fox'] in self.boat) and (len(self.boat) == 2) and (len(self.river_left) == 4):
            print(b)
        elif (self.boat in self.river_left) and (['grain'] in self.boat) and (len(self.boat) == 2) and (len(self.river_left) == 4):
            print(c) 
        elif (self.boat in self.river_left) and (['chicken'] in self.boat) and (len(self.boat) == 2) and (len(self.river_left) == 4):
            print(d)
        elif (self.boat in self.river_left) and (['chicken'] in self.boat and ['man'] in self.boat) and (len(self.boat) == 3) and (len(self.river_left) == 3):
            print(e)
        elif self.boat in self.river_right and (['chicken'] in self.boat and ['man'] in self.boat) and (len(self.boat) == 3) and (len(self.river_right) == 1):
            print(f)
        elif self.boat in self.river_right and (['chicken'] in self.boat) and (['man' in self.river_right]) and (len(self.boat) == 2) and (len(self.river_right)) == 2:
            print(g)
        elif self.boat in self.river_right and (['chicken'] in self.river_right and ['man'] in self.river_right) and (len(self.boat) == 1) and len(self.river_right) == 3:
            print(h)
        elif self.boat in self.river_right and (['chicken'] in self.river_right and ['man'] in self.boat) and (len(self.boat) == 2) and len(self.river_right) == 2:
            print(i)
        elif self.boat in self.river_left and (['chicken'] in self.river_right and ['man'] in self.boat) and (len(self.boat) == 2) and len(self.river_right) == 1:
            print(j)
        elif self.boat in self.river_left and (['chicken'] in self.river_right) and (len(self.boat) == 1) and len(self.river_right) == 1:
            print(k)
        elif self.boat in self.river_left and (['chicken'] in self.river_right and ['grain'] in self.boat) and (len(self.boat) == 2) and len(self.river_right) == 1:
            print(l)
        elif self.boat in self.river_left and (['chicken'] in self.river_right and ['fox'] in self.river_left) and (len(self.river_left) == 2) and len(self.river_right) == 1:
            print(m)
        elif self.boat in self.river_right and (['chicken'] in self.river_right and ['fox'] in self.river_left) and (len(self.river_left) == 1) and len(self.river_right) == 2:
            print(n)
        elif self.boat in self.river_right and (['fox'] in self.river_left and ['grain'] in self.boat) and (len(self.boat) == 2) and len(self.river_left) == 1:
            print(o)
        
        else:
            print (";;; MISHAP - SOMETHING WENT WRONG!")
            
    # Denne funksjonen skal definere alle overgangene fra en tilstand til en annen
    # De kan være mange, så her må man skrive en smart kode
    # Eksperimentere først med enkelte kommandoer, og så implementere denne funksjonen
    def getNextValues(self, state, inp):
        # input her er et kommandonavn og den tilsvarende funksjonen må kalles opp
        pass
        
    # Database "saker", bør ligge i egen modul
    def database(self):
        print ("Left shore: ") 
        if len(self.river_left) == 0:
            print ("Empty")
        else:
            print (str(self.river_left))
        print ("Right shore: ")
        if len (self.river_right) == 0:
            print ("Empty")
        else:
            print (str(self.river_right))
            
    def add(self, item, shore):
        if shore == "left":
            self.river_left.append(item)
        elif shore == "right":
            self.river_right.append(item)
        elif shore == "boat":
            self.boat.append(item)
            
    def remove(self, item, shore):
        if shore == "left":
            self.river_left.remove(item) 
        elif shore == "right":
            self.river_right.remove(item)
        elif shore == "boat":
                self.boat.remove(item)
            
def displaycommands():
    print ("The following commands is valid ")
    print ("quit")
    print ("database")
    print ("view")
    print ("putin")
    print ("takeout")
    print ("crossriver")
    
def main():
    r = River([['chicken'], ['fox'], ['man'], ['grain']])
    x = True
    print ("Write cmd to display commands")
    while x:
        command = input("> ")
        if command == "cmd":
            displaycommands()
        
        elif command == "quit":
            x = False
        
        elif command == "view":
            r.view()
        
        elif command == "database":
            r.database()
            
        elif command == "putin":
            objekt = input("What will you put in the boat?\n> ")
            r.putin([str(objekt)])
        
        elif command == "takeout":
            objekt = input("What will you take out?\n> ")
            r.takeout([str(objekt)])
        
        elif command == "crossriver":
            r.crossriver()
            
        else:
            print ("Invalid command")
            displaycommands()
        
        if (len(r.river_right) == 5) and (len(r.boat) == 1):
            input("You won, congratulations! Press enter to end")
            x = False
        
        if (['chicken'] in r.river_left) and (['grain'] in r.river_left) and (['man'] not in r.river_left) or (['chicken'] in r.river_right) and (['grain'] in r.river_right) and (['man'] not in r.river_right):
            print("The chicken ate the grain. You lost!")
            x = False
        
        if (['chicken'] in r.river_left) and (['fox'] in r.river_left) and (['man'] not in r.river_left) or (['chicken'] in r.river_right) and (['fox'] in r.river_right) and (['man'] not in r.river_right):
            print("The fox ripped apart the chicken. You lost!")
            x = False

main()