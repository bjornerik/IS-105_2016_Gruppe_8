import pygame
import time

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

def forbidden(x):
    if x == 1:
        gameDisplay.blit(blood,(0,300))
        message("The wolf ripped apart the chicken! "
                "You LOST!")
    elif x == 2:
        gameDisplay.blit(blood,(600,300))
        message("The wolf ripped apart the chicken! "
                "You LOST!")
    elif x == 3:
        message("The chicken has eaten all the grain! "
                "You LOST!")
        
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
    
def instruct(x,y):
    gameDisplay.blit(instructions,(x,y))
    
def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((displayx/2),(displayy/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    
    time.sleep(10)
    
    gameloop()
    
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
                    if not gx == 280 or fox == 280:
                        if cx == 10:
                            cx += 270 
                            cy += 40
                        elif cx == 660:
                            cx -= 130
                            cy += 40
                        else:
                            pass
                if event.key == pygame.K_r:
                    if bx == 200:
                        if cx == 280:
                            cx += 250
                        elif gx == 280:
                            gx += 250
                        elif fox == 280:
                            fox += 250
                        fax += 250
                        bx += 250   
                    elif bx == 450:
                        if cx == 530:
                            cx -= 250
                        elif gx == 530:
                            gx -= 250
                        elif fox == 530:
                            fox -= 250
                        fax -= 250
                        bx -= 250
                    else:
                        pass
                if event.key == pygame.K_a:
                    if cx == 280:
                        cx -= 270 
                        cy -= 40
                    elif cx == 530:
                        cx += 130
                        cy -= 40
                    else:
                        pass
                if event.key == pygame.K_w:
                    if not cx == 280 or fox == 280:
                        if gx == 70:
                            gx += 210 
                            gy += 40
                        if cx == 730:
                            gx -= 200
                            gy += 40
                if event.key == pygame.K_s:
                    if gx == 280:
                        gx -= 210 
                        gy -= 40
                    if gx == 530:
                        gx += 200
                        gy -= 40
                if event.key == pygame.K_e:
                    if not cx == 280 or gx == 280:
                        if fox == 130:
                            fox += 150 
                            foy += 40
                        if fox == 600:
                            fox -= 70
                            foy += 40
                if event.key == pygame.K_f:
                    if fox == 280:
                        fox -= 150 
                        foy -= 40
                    if fox == 530:
                        fox += 70
                        foy -= 40
            
            if bx == 200 and fox == 600 and cx == 660:
                forbidden(2)
            
            if bx == 200 and cx == 660 and gx == 730:
                forbidden(3)
            
            if bx == 450 and cx == 10 and fox == 130:
                forbidden(1)
            
            if bx == 450 and cx == 10 and gx == 70:
                forbidden(3)
                        
            if fox == 600 and gx == 730 and cx == 660:
                victory = True     
    
        fax += faxchange
        cx += cxchange
        gx += gxchange
        fox += foxchange
    
        gameDisplay.fill((white))
        earthObject(0,400)
        waterobject(200,450)
        earthObject(600,400)
        instruct(0,0)
        farmerobject(fax,fay)
        grainobject(gx,gy)
        chickenobject(cx,cy)
        foxobject(fox,foy) 
        boatobject(bx,by)
        
        if victory:
            message('Du vant!!')
    
        pygame.display.update()
        clock.tick(60)    
        
gameloop()
pygame.quit()
quit()