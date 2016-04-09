# -*- coding: utf-8 -*-

#Database som lagrer posisjonenen til alle itemsene i spillet, samt lagring av alle funksjoner for endring av posisjonene.
class Database(object):
    river_left = []
    boat = ["boat"]
    river_right = []    
    def __init__(self, start):
        self.river_left = start
        self.river_left.append(self.boat)
        
    def view(self):
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
            
    def crossriver(self):
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

#Tilstandsmaskin for skifte mellom tilstander for mann
class StateMachine(object):

    def __init__(self, state):
        self.state = state

    def play(self):
        currentState = self.state.firstState()
        wonState = self.state.nextState('won')
        lostState = self.state.nextState('lost')

        while currentState != wonState and currentState != lostState:
            nextStateName = currentState.enter()
            currentState = self.state.nextState(nextStateName)

        currentState.enter()

#Funksjon til metaklasse
def enter():
    pass

#State klasse som tilstandene skal arve fra    
State = type("State", (object,), {"enter":enter})

#Tilstandsklasse for startstilstand, inneholder @function enter som simulerer de forskjellige valgene man har på leftshore.        
class LeftShore(State):    
    def enter(self):
        print ("Type cmd to display commands")
        inp = input ("> ")
        
        if inp == "jump in" and (d.boat in d.river_left):
            d.putin(['man'])
            return 'inboat'
        
        elif inp == "view":
            d.view()
            return 'leftshore'
        
        elif inp == "cmd":
            print ("The following commands is valid:")
            print ("jump in")
            print ("putin")
            print ("takeout")
            print ("view")
            return 'leftshore'
            
        elif inp == "putin":
            item = input("What item do you want to put in the boat?\n")
            d.putin([str(item)])
            return 'leftshore'
        
        elif inp == "takeout":
            item = input("What item do you want to take out of the boat\n")
            d.takeout([str(item)])
            return 'leftshore'
            
        else:
            print ("Invalid command")
            return 'leftshore'        
        
#Tilstandsklasse for båttilstand, inneholder @function enter som simulerer de forskjellige valgene man har på InBoat     
class InBoat(State):
    
    def enter(self):
        if (['chicken'] in d.river_left) and (['grain'] in d.river_left) or (['chicken'] in d.river_right) and (['grain'] in d.river_right):
            return 'lost'
        
        if (['chicken'] in d.river_left) and (['fox'] in d.river_left) and (['man'] not in d.river_left) or (['chicken'] in d.river_right) and (['fox'] in d.river_right) and (['man'] not in d.river_right):
            return 'lost'
        
        print ("Type cmd to display commands")
        inp = input ("> ")
        
        if inp == "jump out" and (d.boat in d.river_left):
            d.takeout(['man'])
            return 'leftshore'
        elif inp == "jump out" and (d.boat in d.river_right):
            d.takeout(['man'])
            return 'rightshore'
        
        elif inp == "view":
            d.view()
            return 'inboat'
        
        elif inp == "cmd":
            print ("The following commands is valid:")
            print ("jump out")
            print ("view")
            print ("crossriver")
            return 'inboat'
            
        elif inp == "crossriver":
            d.crossriver()
            return 'inboat'
            
        else:
            print ("Invalid command")
            return 'leftshore' 

#Tilstandsklasse for rightshore, inneholder @function enter som simulerer de forskjellige valgene man har på rightshore, har også en sjekk for om spillet er vunnet.    
class RightShore(State):
    def enter(self):
        if (len(d.river_right) == 5) and (len(d.boat) == 1):
            return 'won'
            
        print ("Type cmd to display commands")
        inp = input ("> ")
        
        if inp == "jump in" and (d.boat in d.river_right):
            d.putin(['man'])
            return 'inboat'
        
        elif inp == "view":
            d.view()
            return 'rightshore'
        
        elif inp == "cmd":
            print ("The following commands is valid:")
            print ("jump in")
            print ("putin")
            print ("takeout")
            print ("view")
            return 'rightshore'
            
        elif inp == "putin":
            item = input("What item do you want to put in the boat?\n")
            d.putin([str(item)])
            return 'rightshore'
        
        elif inp == "takeout":
            item = input("What item do you want to take out of the boat\n")
            d.takeout([str(item)])
            return 'rightshore'
            
        else:
            print ("Invalid command")
            return 'rightshore'   

#Hvis forbudte tilstander skjer henviser man til denne tilstand.
class Lost(State):
    def enter(self):
        print ("You lost!")

#Hvis alle kriteriene er møtt er spillet vunnet og man havner i denne tilstanden.    
class Won(State):
    def enter(self):
        print ("You won!")
        
#Map holder en database over de forskjellige tilstandene og bistår tilstandsmaskinen i bytte mellom tilstander.
class Map(object):

    States = {
        'leftshore': LeftShore(),
        'inboat': InBoat(),
        'rightshore': RightShore(),
        'won' : Won(),
        'lost' : Lost()
        }

    def __init__(self, startState):
        self.startState = startState

    def nextState(self, state):
        val = Map.States.get(state)
        return val

    def firstState(self):
        return self.nextState(self.startState)

#Lager en instans av databasen, kartet og tilstandsmaskinen og setter igang maskinen.
if __name__ == '__main__':
    d = Database([['chicken'], ['fox'], ['man'], ['grain']])
    a_map = Map('leftshore')
    a_game = StateMachine(a_map)
    a_game.play()    
       
    
    