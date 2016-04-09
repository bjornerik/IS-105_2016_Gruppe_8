# -*- coding: utf-8 -*-

import pygame
import time

pygame.init()

displayx=800
displayy=600

white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption('River crossing')
clock = pygame.time.Clock()

earth = pygame.image.load('jord.png')

water = pygame.image.load('vann.png')

chicken = pygame.image.load('chicken.png')

farmer = pygame.image.load('farmer.png')

grain = pygame.image.load('grain.png')

fox = pygame.image.load('fox.png')

boat = pygame.image.load('boat.png')

instructions1 = pygame.image.load('instructions1.png')

instructions2 = pygame.image.load('instructions2.png')

blood = pygame.image.load('blood.png')

class Database(object):
    cx = 10
    cy = 350
    
    gx = 50
    gy = 350
    
    fox = 80 
    foy = 340
    
    bx = 200
    by = 420    
    
    river_left = []
    boat = ["boat"]
    river_right = []    
    def __init__(self, start):
        self.river_left = start
        self.river_left.append(self.boat)
        
    def crossriver(self):
        if self.boat in self.river_left:
            self.remove(self.boat, "left")
            self.add(self.boat, "right")
            self.bx += 250
            if ['chicken'] in self.boat:
                self.cx += 250
            if ['grain'] in self.boat:
                self.gx += 250
            if ['fox'] in self.boat:
                self.fox += 250
                
        elif self.boat in self.river_right:
            self.remove(self.boat, "right")      
            self.add(self.boat, "left")
            self.bx -= 250
            if ['chicken'] in self.boat:
                self.cx -= 250
            if ['grain'] in self.boat:
                self.gx -= 250
            if ['fox'] in self.boat:
                self.fox -= 250

    def putin(self, item):
        if (item and self.boat in self.river_left) or (item and self.boat in self.river_right):
            if len(self.boat) >= 3:
                message("The boat is full")
            else:
                if (['man'] not in self.boat) and (len(self.boat) == 2) and (item != ['man']):
                    message("You can only place one item in addition to man in the boat")
                else:
                    if item in self.river_left:
                        self.remove(item, "left")
                        self.add(item, "boat")
                        if item == ['chicken']:
                            self.cx += 270 
                            self.cy += 40
                        if item == ['grain']:
                            self.gx += 230 
                            self.gy += 40  
                        if item == ['fox']:
                            self.fox += 200 
                            self.foy += 40                            
                            
                            
                    elif item in self.river_right:
                        self.remove(item, "right")
                        self.add(item, "boat")
                        if item == ['chicken']:
                            self.cx -= 220
                            self.cy += 40
                        if item == ['grain']:
                            self.gx -= 180 
                            self.gy += 40  
                        if item == ['fox']:
                            self.fox -= 130 
                            self.foy += 40                            
                    else:
                        message("The item is already in the boat")
        else: 
            message(str(item) + " and the boat needs to be on the same shore")


    def takeout(self, item):
        if self.boat in self.river_left:
            if item in self.boat:
                self.remove(item, "boat")
                self.add(item, "left")
                if item == ['chicken']:
                    self.cx -= 270 
                    self.cy -= 40
                if item == ['grain']:
                    self.gx -= 230 
                    self.gy -= 40  
                if item == ['fox']:
                    self.fox -= 200 
                    self.foy -= 40                  
            else:
                message(str(item) + " is not in the boat")

        elif self.boat in self.river_right:
            if item in self.boat:
                self.remove(item, "boat")
                self.add(item, "right")
                if item == ['chicken']:
                    self.cx += 220
                    self.cy -= 40
                if item == ['grain']:
                    self.gx += 180 
                    self.gy -= 40  
                if item == ['fox']:
                    self.fox += 130 
                    self.foy -= 40                
            else:
                message(str(item) + " is not in the boat") 
    
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
        fax = 130
        fay = 310    
        x = True
        while x:
            for event in pygame.event.get():         
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pass
                    if event.key == pygame.K_r:
                        pass
                    if event.key == pygame.K_a:
                        pass
                    if event.key == pygame.K_w:
                        pass
                    if event.key == pygame.K_s:
                        pass                
                    if event.key == pygame.K_e:
                        pass
                    if event.key == pygame.K_f:
                        pass
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:                    
                        d.putin(['man'])
                        x = False
                        return 'inboat'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        d.putin(['chicken'])
                        return 'leftshore'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:            
                        d.takeout(['chicken'])
                        return 'leftshore'            
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        d.putin(['grain'])
                        return 'leftshore' 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:            
                        d.takeout(['grain'])
                        return 'leftshore'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        d.putin(['fox'])
                        return 'leftshore'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_f:            
                        d.takeout(['fox'])
                        return 'leftshore'            
            
            gameDisplay.fill((white))
            earthObject(0,400)
            waterobject(200,450)
            earthObject(600,400)
            instruct1(0,0)
            farmerobject(fax,fay)
            grainobject(d.gx,d.gy)
            chickenobject(d.cx,d.cy)
            foxobject(d.fox,d.foy) 
            boatobject(d.bx,d.by)
        
            pygame.display.update()
            clock.tick(60)            
        
        
#Tilstandsklasse for båttilstand, inneholder @function enter som simulerer de forskjellige valgene man har på InBoat     
class InBoat(State):
    
    def enter(self):
        if (['chicken'] in d.river_left) and (['grain'] in d.river_left) or (['chicken'] in d.river_right) and (['grain'] in d.river_right):
            return 'lost'
        
        if (['chicken'] in d.river_left) and (['fox'] in d.river_left) and (['man'] not in d.river_left) or (['chicken'] in d.river_right) and (['fox'] in d.river_right) and (['man'] not in d.river_right):
            return 'lost'
        
        if d.boat in d.river_left:
            fax = 220
            fay = 350
        if d.boat in d.river_right:
            fax = 470
            fay = 350
        x = True
        while x:
            for event in pygame.event.get():         
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pass
                    if event.key == pygame.K_w:
                        pass
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:                    
                        if (d.boat in d.river_left):
                            d.takeout(['man'])
                            return 'leftshore'
                        elif (d.boat in d.river_right):
                            d.takeout(['man'])
                            return 'rightshore'
        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        d.crossriver()
                        return 'inboat'
            
            gameDisplay.fill((white))
            earthObject(0,400)
            waterobject(200,450)
            earthObject(600,400)
            instruct2(0,0)
            farmerobject(fax,fay)
            grainobject(d.gx,d.gy)
            chickenobject(d.cx,d.cy)
            foxobject(d.fox,d.foy) 
            boatobject(d.bx,d.by)
        
            pygame.display.update()
            clock.tick(60)         

#Tilstandsklasse for rightshore, inneholder @function enter som simulerer de forskjellige valgene man har på rightshore, har også en sjekk for om spillet er vunnet.    
class RightShore(State):    
    def enter(self):
        if (len(d.river_right) == 5) and (len(d.boat) == 1):
            return 'won'        
        fax = 600
        fay = 310    
        x = True
        while x:
            for event in pygame.event.get():         
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pass
                    if event.key == pygame.K_r:
                        pass
                    if event.key == pygame.K_a:
                        pass
                    if event.key == pygame.K_w:
                        pass
                    if event.key == pygame.K_s:
                        pass                
                    if event.key == pygame.K_e:
                        pass
                    if event.key == pygame.K_f:
                        pass
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:                    
                        d.putin(['man'])
                        x = False
                        return 'inboat'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        d.putin(['chicken'])
                        return 'rightshore'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:            
                        d.takeout(['chicken'])
                        return 'rightshore'            
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        d.putin(['grain'])
                        return 'rightshore' 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:            
                        d.takeout(['grain'])
                        return 'rightshore'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        d.putin(['fox'])
                        return 'rightshore'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_f:            
                        d.takeout(['fox'])
                        return 'rightshore'            
            
            gameDisplay.fill((white))
            earthObject(0,400)
            waterobject(200,450)
            earthObject(600,400)
            instruct1(0,0)
            farmerobject(fax,fay)
            grainobject(d.gx,d.gy)
            chickenobject(d.cx,d.cy)
            foxobject(d.fox,d.foy) 
            boatobject(d.bx,d.by)
        
            pygame.display.update()
            clock.tick(60)            

#Hvis forbudte tilstander skjer henviser man til denne tilstand.
class Lost(State):
    def enter(self):
        message("You lost!")

#Hvis alle kriteriene er møtt er spillet vunnet og man havner i denne tilstanden.    
class Won(State):
    def enter(self):
        message("You won!")
        
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

        
def earthObject(x,y):
    gameDisplay.blit(earth, (x,y))
    
def waterobject(x,y):
    gameDisplay.blit(water, (x,y))  
    
def boatobject(x,y):
    gameDisplay.blit(boat, (x,y))
    
def chickenobject(x,y):
    gameDisplay.blit(chicken, (x,y))

def farmerobject(x,y):
    gameDisplay.blit(farmer, (x,y))

def grainobject(x,y):
    gameDisplay.blit(grain, (x,y))

def foxobject(x,y):
    gameDisplay.blit(fox, (x,y))
    
def instruct1(x,y):
    gameDisplay.blit(instructions1,(x,y))
def instruct2(x,y):
    gameDisplay.blit(instructions2,(x,y))
    
def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayx/2),(displayy/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    
    time.sleep(2)
    





if __name__ == "__main__":
    d = Database([['chicken'], ['fox'], ['man'], ['grain']])
    a_map = Map('leftshore')
    a_game = StateMachine(a_map)
    a_game.play()       
    pygame.quit()
    quit()