import pygame
import time
import RiverCrossing

pygame.init()

displayx=800
displayy=600

white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption('River crossing solution')
clock = pygame.time.Clock()

earth = pygame.image.load('jord.png')

water = pygame.image.load('vann.png')

chicken = pygame.image.load('chicken.png')

farmer = pygame.image.load('farmer.png')

grain = pygame.image.load('grain.png')

fox = pygame.image.load('fox.png')

boat = pygame.image.load('boat.png')

instructions = pygame.image.load('instructions.png')

blood = pygame.image.load('blood.png')
        
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

    
def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (150,30)
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)
    
def gameloop():
    fax = 220
    fay = 350    
    faxchange = 0
    
    cx = 10
    cy = 350
    cxchange = 0
    
    gx = 70
    gy = 350
    gxchange = 0
    
    fox = 130 
    foy = 340
    foxchange = 0 
    
    bx = 200
    by = 420
    bchange = 0
    
    victory = False
    finished = False
    grain = True
    
    
    
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True          
            
                                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    message(RiverCrossing.solutionstack[1])
                    cx += 650
                    fax += 250
                    bx += 250
                    
                if event.key == pygame.K_2:
                    message(RiverCrossing.solutionstack[2])
                    fax -= 250
                    bx -= 250
                    
                if event.key == pygame.K_3:
                    message(RiverCrossing.solutionstack[3])
                    fax += 250
                    bx += 250 
                    gx += 660
                    
                if event.key == pygame.K_4:
                    message(RiverCrossing.solutionstack[4])
                    fax -= 250
                    bx -= 250 
                    cx -= 650
                    
                if event.key == pygame.K_5:
                    message(RiverCrossing.solutionstack[5])
                    fax += 250
                    bx += 250
                    fox += 470
                    
                if event.key == pygame.K_6:
                    message(RiverCrossing.solutionstack[6])
                    fax -= 250
                    bx -= 250
                    
                if event.key == pygame.K_7:
                    message(RiverCrossing.solutionstack[7])
                    fax += 250
                    bx += 250
                    cx += 650
                    victory = True
    
        gameDisplay.fill((white))
        earthObject(0,400)
        waterobject(200,450)
        earthObject(600,400)
        farmerobject(fax,fay)
        grainobject(gx,gy)
        chickenobject(cx,cy)
        foxobject(fox,foy) 
        boatobject(bx,by)
        pygame.draw.line(gameDisplay, black, (325,0), (325,75))
        pygame.draw.line(gameDisplay, black, (0,75), (325,75))
        
        if victory:
            message('Du vant!!')
    
        pygame.display.update()
        clock.tick(60)    
        
gameloop()
pygame.quit()
quit()