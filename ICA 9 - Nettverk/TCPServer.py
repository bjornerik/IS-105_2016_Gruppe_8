# -*- coding: utf-8 -*-
import socket
import sys

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg :
    sys.exit()
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()       

#Database som lagrer posisjonenen til alle itemsene i spillet, samt lagring av alle funksjoner for endring av posisjonene.
class Database(object):
    river_left = []
    boat = ["boat"]
    river_right = []    
    def __init__(self, start):
        self.river_left = start
        self.river_left.append(self.boat)
        
    def view(self, addr):
        first = ("Left shore:\n") 
        if len(self.river_left) == 0:
            second = ("Empty\n")
        else:
            second = (str(self.river_left) + "\n")
        third = ("Right shore:\n")
        if len (self.river_right) == 0:
            fourth = ("Empty\n")
        else:
            fourth = (str(self.river_right) + "\n")
            
        message = str(first + second + third + fourth)
        s.sendto(message, addr)
            
    def crossriver(self, addr):
        if self.boat in self.river_left:
            self.remove(self.boat, "left")
            if self.boat not in self.river_right:
                self.add(self.boat, "right")
                message = 'The boat crossed to the right shore'
        elif self.boat in self.river_right:
            self.remove(self.boat, "right")       
            if self.boat not in self.river_left:
                self.add(self.boat, "left")
                message = 'The boat crossed to the left shore'
                
        s.sendto(message, addr)

    def putin(self, item, addr):
        if (item and self.boat in self.river_left) or (item and self.boat in self.river_right):
            if len(self.boat) >= 3:
                message = ("The boat is full")
            else:
                if (['man'] not in self.boat) and (len(self.boat) == 2) and (item != ['man']):
                    message = ("You can only place one item in addition to man in the boat")
                else:
                    if item in self.river_left:
                        self.remove(item, "left")
                        self.add(item, "boat")
                        message = str(item) + (' is added to the boat')
                    elif item in self.river_right:
                        self.remove(item, "right")
                        self.add(item, "boat")
                        message = str(item) + (' is added to the boat')
                    else:
                        message = ("The item is already in the boat")
        else: 
            message = (str(item) + " and the boat needs to be on the same shore")
        
        s.sendto(message, addr)


    def takeout(self, item, addr):
        if self.boat in self.river_left:
            if item in self.boat:
                self.remove(item, "boat")
                self.add(item, "left")
                message = str(item) + ' is removed from the boat'
            else:
                message = (str(item) + ' is not in the boat')

        elif self.boat in self.river_right:
            if item in self.boat:
                self.remove(item, "boat")
                self.add(item, "right")
                message = str(item) + ' is removed from the boat'
            else:
                message = (str(item) + " is not in the boat") 
                
        s.sendto(message, addr)
    
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
        dt = s.recvfrom(1024)
        data = dt[0]
        addr = dt[1]             
        
        if data == "jump in" and (d.boat in d.river_left):
            d.putin(['man'], addr)
            return 'inboat'
        
        elif data == "view":
            d.view(addr)
            return 'leftshore'
        
        elif data == "cmd":
            message = ("The following commands is valid:\njump in\nputin + object\ntakeout + object\nview")
            s.sendto(message, addr)
            return 'leftshore'
            
        elif 'putin' in data:
            datalist = data.split()
            d.putin([datalist[-1]], addr)
            return 'leftshore'
        
        elif 'takeout' in data:
            datalist = data.split()
            d.takeout([datalist[-1]], addr)
            return 'leftshore'
            
        else:
            message = ("Invalid command\nType cmd to display commands")
            s.sendto(message,addr)
            return 'leftshore'        
        
#Tilstandsklasse for båttilstand, inneholder @function enter som simulerer de forskjellige valgene man har på InBoat     
class InBoat(State):
    
    def enter(self):
        if (['chicken'] in d.river_left) and (['grain'] in d.river_left) or (['chicken'] in d.river_right) and (['grain'] in d.river_right):
            return 'lost'
        
        if (['chicken'] in d.river_left) and (['fox'] in d.river_left) and (['man'] not in d.river_left) or (['chicken'] in d.river_right) and (['fox'] in d.river_right) and (['man'] not in d.river_right):
            return 'lost'
        
        dt = s.recvfrom(1024)
        data = dt[0]
        addr = dt[1]
        
        if data == "jump out" and (d.boat in d.river_left):
            d.takeout(['man'], addr)
            return 'leftshore'
        elif data == "jump out" and (d.boat in d.river_right):
            d.takeout(['man'], addr)
            return 'rightshore'
        
        elif data == "view":
            d.view(addr)
            return 'inboat'
        
        elif data == "cmd":
            message = ("The following commands is valid:\njump out\view\ncrossriver")
            s.sendto(message, addr)            
            return 'inboat'
            
        elif data == "crossriver":
            d.crossriver(addr)
            return 'inboat'
            
        else:
            message = ("Invalid command\nType cmd to display commands")
            s.sendto(message,addr)
            return 'inboat' 

#Tilstandsklasse for rightshore, inneholder @function enter som simulerer de forskjellige valgene man har på rightshore, har også en sjekk for om spillet er vunnet.    
class RightShore(State):
    def enter(self):
        if (len(d.river_right) == 5) and (len(d.boat) == 1):
            return 'won'
            
        dt = s.recvfrom(1024)
        data = dt[0]
        addr = dt[1]
        
        if data == "jump in" and (d.boat in d.river_right):
            d.putin(['man'], addr)
            return 'inboat'
        
        elif data == "view":
            d.view(addr)
            return 'rightshore'
        
        elif data == "cmd":
            message = ("The following commands is valid:\njump in\nputin + object\ntakeout + object\nview")
            s.sendto(message, addr)
            return 'rightshore'
            
        elif 'putin' in data:
            datalist = data.split()
            d.putin([datalist[-1]], addr)
            return 'rightshore'
        
        elif 'takeout' in data:
            datalist = data.split()
            d.takeout([datalist[-1]], addr)
            return 'rightshore'
            
        else:
            message = ("Invalid command\nType cmd to display commands")
            s.sendto(message,addr)
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
       
    
    