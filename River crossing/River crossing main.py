import pygame
import time
import RiverCrossing

pygame.init()

displayx=800
displayy=600

white = (255,255,255)

gameDisplay = pygame.display.set_mode((displayx,displayy))
pygame.display.set_caption('River crossing solution')
clock = pygame.time.Clock()

earth = pygame.image.load('jord.png')
earthx = 200
earthy = 200

water = pygame.image.load('vann.png')
waterx = 400
watery = 150

chicken = pygame.image.load('chicken.png')

farmer = pygame.image.load('farmer.png')

grain = pygame.image.load('grain.png')

fox = pygame.image.load('fox.png')

def earthObject(x,y):  
    gameDisplay.blit(earth, (x,y))
    
def waterobject(x,y):
    gameDisplay.blit(water, (x,y))  
    
def chickenobject(x,y):
    gameDisplay.blit(chicken, (x,y))

def farmerobject(x,y):
    gameDisplay.blit(farmer, (x,y))

def grainobject(x,y):
    gameDisplay.blit(grain, (x,y))

def foxobject(x,y):
    gameDisplay.blit(fox, (x,y))
    
def gameloop():
    fax = 0
    fay = 320    
    faxchange = 0
    
    cx = 100
    cy = 350
    cxchange = 0
    
    gx = 60
    gy = 350
    gxchange = 0
    
    fox = 150 
    foy = 350
    foxchange = 0 
    
    finished = False
    
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    faxchange += 5
                    cxchange += 5
                if event.key == pygame.K_q:
                    faxchange -= 5
                if event.key == pygame.K_s:
                    faxchange += 5
                    gxchange  += 5
                if event.key == pygame.K_d:
                    faxchange -= 5
                    cxchange -= 5  
                if event.key == pygame.K_f:
                    faxchange += 5
                    foxchange += 5
                if event.key == pygame.K_w:
                    faxchange += 5
                
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    faxchange = 0    
                    cxchange = 0
                if event.key == pygame.K_q:
                    faxchange = 0  
                if event.key == pygame.K_s:
                    faxchange = 0
                    gxchange = 0   
                if event.key == pygame.K_d:
                    faxchange = 0
                    cxchange = 0       
                if event.key == pygame.K_w:
                    faxchange = 0
            
            if event.type == pygame.QUIT:
                finished = True    
    
        fax += faxchange
        cx += cxchange
        gx += gxchange
        fox += foxchange
    
        gameDisplay.fill((white))
        earthObject(0,400)
        waterobject(200,450)
        earthObject(600,400)
        farmerobject(fax,fay)
        grainobject(gx,gy)
        chickenobject(cx,cy)
        foxobject(fox,foy)   
    
        pygame.display.update()
        clock.tick(60)    
        
gameloop()
pygame.quit()
quit()