
import pygame
import random
pygame.init()

#combination of user and random input
skyr = int(input("What should the r value of the sky be?"))
skyg = random.randint(1,255)
skyb = random.randint(1,255)
sky = (skyr,skyg,skyb)

win = pygame.display.set_mode([600,400])
win.fill(sky)

grey = (200,200,200)
black = (75,75,75)
tan = (243,220,173)
orange = (242, 200, 116)
brown = (171,128,44)
green = (36,142,36)
white = (255,255,255)

#user input
rockr = int(input("What should the r value of the rock be? "))
rockg = int(input("What should the g value of the rock be? "))           
rockb = int(input("What should the b value of the rock be? "))           
rock_color = (rockr, rockg, rockb)


#animating the clouds
frames = 0
offset = 0
rect1_x = 400
rect1 = pygame.Rect(rect1_x,50,150,50)
rect2_x = 500
rect2 = pygame.Rect(rect2_x,30,150,50)
rect3_x = 390
rect3 = pygame.Rect(rect3_x,20,170,50)

rect4_x = 1
rect4 = pygame.Rect(rect4_x,40,150,50)
rect5_x = 100
rect5 = pygame.Rect(rect5_x,50,150,50)
rect6_x = 50
rect6 = pygame.Rect(rect6_x,20,150,50)

#animating simba
simbahand_offset = 0
simbahand1_y = 190 
simbahand2_y = 190

simbaleg_offset = 0
simbaleg1_x = 230
simbaleg2_x = 255

#animating birds
bird_offset = 0
bird1_y = 70
bird2_y = 50
bird3_y = 110

#animating tree
tree_offset = 0
tree2_offset = 0
tree_x = random.randint(90,110)
tree2_x = 490

#clouds loop
running = True
            
while frames < 40 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    frames += 1
    win.fill(sky)
    offset += 5
    
    rect1.x = rect1_x - offset
    rect1 = pygame.Rect(rect1.x,50,150,50)
    pygame.draw.ellipse(win,(245,245,245),rect1)
    
    rect2.x = rect2_x - offset
    rect2 = pygame.Rect(rect2.x,30,150,50)
    pygame.draw.ellipse(win,(250,250,250),rect2)
    
    rect3.x = rect3_x - offset
    rect3 = pygame.Rect(rect3.x,20,170,50)
    pygame.draw.ellipse(win,white,rect3)
    
    rect4.x = rect4_x - offset
    rect4 = pygame.Rect(rect4.x,40,150,50)
    pygame.draw.ellipse(win,(245,245,245),rect4)
    
    rect5.x = rect5_x - offset
    rect5 = pygame.Rect(rect5.x,50,150,50)
    pygame.draw.ellipse(win,(250,250,250),rect5)
    
    rect6.x = rect6_x - offset
    rect6 = pygame.Rect(rect6.x,20,150,50)
    pygame.draw.ellipse(win,white,rect6)
    
    #rock
    rectangle = pygame.Rect(200,330,250,200)
    pygame.draw.ellipse(win,rock_color,rectangle)

    #simbahands
    
    simbahand_offset -= 2
    simbahand1_y = simbahand1_y + simbahand_offset
    simbahand2_y = simbahand2_y + simbahand_offset
    pygame.draw.line(win,orange,(235,170),(210,simbahand1_y+simbahand_offset),10)
    pygame.draw.line(win,orange,(250,170),(275,simbahand2_y+simbahand_offset),10)
    
    while simbahand1_y <= 180:
        simbahand_offset += 2
        simbahand1_y = simbahand1_y + simbahand_offset
        simbahand2_y = simbahand2_y + simbahand_offset
        pygame.draw.line(win,orange,(235,170),(210,simbahand1_y-simbahand_offset),10)
        pygame.draw.line(win,orange,(250,170),(275,simbahand2_y-simbahand_offset),10)

    #torsooutersimba
    rect = pygame.Rect(227,160,32,60)
    pygame.draw.ellipse(win,orange,rect)
    
    #legssimba
    simbaleg_offset -= 2
    simbaleg1_x = simbaleg1_x + simbaleg_offset
    simbaleg2_x = simbaleg2_x - simbaleg_offset
    pygame.draw.line(win,orange,(235,200),(simbaleg1_x,235),10)
    pygame.draw.line(win,orange,(250,200),(simbaleg2_x,235),10)
        
    while simbaleg1_x <= 220 and simbaleg2_x >= 265:
        simbaleg_offset += 2
        simbaleg1_x = simbaleg1_x + simbaleg_offset
        simbaleg2_x = simbaleg2_x - simbaleg_offset
        pygame.draw.line(win,orange,(235,200),(simbaleg1_x,235),10)
        pygame.draw.line(win,orange,(250,200),(simbaleg2_x,235),10)
        
        
    #torsosimba
    rect = pygame.Rect(230,170,25,40)
    pygame.draw.ellipse(win,tan,rect)
        
    #arms
    pygame.draw.line(win,black,(285,270),(235,170),10)
    pygame.draw.line(win,black,(315,270),(250,170),10)
        
    #hands
    pygame.draw.circle(win,brown,(235,170),8)
    pygame.draw.circle(win,brown,(250,170),8)
        
    #simbaears
    pygame.draw.circle(win,orange,(235,140),5)
    pygame.draw.circle(win,orange,(250,140),5)
        
    #simbahead
    pygame.draw.circle(win,orange,(243,153),15)    

    #torso
    rect = pygame.Rect(280,230,40,100)
    pygame.draw.ellipse(win,black,rect)
        
    #head
    pygame.draw.polygon(win,grey, [(335, 200), (265, 200), (300,250)])
    pygame.draw.polygon(win,grey, [(317, 220), (283, 220), (300,330)])
        
    #torso
    r = pygame.Rect(290,275, 20,50)
    pygame.draw.ellipse(win,grey,r)
        
    #head
    pygame.draw.circle(win, black, (300,225), 19)
        
    #legs
    pygame.draw.line(win,black,(310,315),(340,335),10)
    pygame.draw.line(win,black,(290,315),(270,315),10)
    pygame.draw.line(win,black,(275,315),(275,340),10)

    #birds
    bird_offset += 1
    bird1_y = bird1_y + bird_offset
    pygame.draw.line(win,grey,(500,bird1_y),(510,75),5)
    pygame.draw.line(win,grey,(510,75),(520,bird1_y),5)
    
    bird2_y = bird2_y + bird_offset
    pygame.draw.line(win,grey,(400,bird2_y),(410,55),5)
    pygame.draw.line(win,grey,(410,55),(420,bird2_y),5)
    
    bird3_y = bird3_y + bird_offset
    pygame.draw.line(win,grey,(100,bird3_y),(110,115),5)
    pygame.draw.line(win,grey,(110,115),(120,bird3_y),5)
    
    while bird1_y >= 75 and bird2_y >= 55 and bird3_y >= 110:
        bird_offset -= 1
        bird1_y = bird1_y + bird_offset
        pygame.draw.line(win,grey,(500,bird1_y),(510,75),5)
        pygame.draw.line(win,grey,(510,75),(520,bird1_y),5)        

        bird2_y = bird2_y + bird_offset
        pygame.draw.line(win,grey,(400,bird2_y),(410,55),5)
        pygame.draw.line(win,grey,(410,55),(420,bird2_y),5)
        
        bird3_y = bird3_y + bird_offset
        pygame.draw.line(win,grey,(100,bird3_y),(110,115),5)
        pygame.draw.line(win,grey,(110,115),(120,bird3_y),5)
        
    #random tree animation
    tree_x = random.randint(90,110)
    pygame.draw.line(win,brown,(100,400),(100,250), 30)
    pygame.draw.polygon(win,green,[(tree_x,175),(50,250),(150,250)])
    pygame.draw.polygon(win,green,[(tree_x,200),(50,300),(150,300)])
    pygame.draw.polygon(win,green,[(tree_x,250),(50,350),(150,350)])
    
    #normal tree animation
    tree2_offset += 1
    tree2_x = tree2_x + tree2_offset
    pygame.draw.line(win,brown,(500,400),(500,250), 30)
    pygame.draw.polygon(win,green,[(tree2_x,175),(450,250),(550,250)])
    pygame.draw.polygon(win,green,[(tree2_x,175),(450,250),(550,250)])
    pygame.draw.polygon(win,green,[(tree2_x,200),(450,300),(550,300)])
    pygame.draw.polygon(win,green,[(tree2_x,250),(450,350),(550,350)])  
    
    
    while tree_x >= 110:
        tree_x = random.randint(90,110)
        pygame.draw.polygon(win,green,[(tree_x,175),(50,250),(150,250)])
        pygame.draw.polygon(win,green,[(tree_x,175),(50,250),(150,250)])
        pygame.draw.polygon(win,green,[(tree_x,200),(50,300),(150,300)])
        pygame.draw.polygon(win,green,[(tree_x,250),(50,350),(150,350)])
        
    while tree2_x >= 510:
        tree2_offset -= 1
        tree2_x = tree2_x + tree2_offset
        pygame.draw.polygon(win,green,[(tree2_x,175),(450,250),(550,250)])
        pygame.draw.polygon(win,green,[(tree2_x,175),(450,250),(550,250)])
        pygame.draw.polygon(win,green,[(tree2_x,200),(450,300),(550,300)])
        pygame.draw.polygon(win,green,[(tree2_x,250),(450,350),(550,350)])
        
    pygame.display.flip()
    pygame.time.wait(100)
    
    
    
    
    
    
    
    
    

    

# Turn in your Coding Exercise.
