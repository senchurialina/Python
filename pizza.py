import pygame 
import random

pygame.init()
pygame.mixer.init()


# display
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Bouncing Ball")

black = (0, 0, 0)

pygame.mixer.music.load("Sounds/lobbybgmusic.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#balls
position= [random.randint(200,250), random.randint(100,250)] 
ball2= [random.randint(100,150), random.randint(300,350)] 
ball3= [random.randint(360,410), random.randint(400,450)]   

#speeds
speed = [3,3]
speed2 = [4,4]
speed3 = [5,5]

#colors 
color1 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
color2 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
color3 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

radius = 20 
running = True

while running:  
    for event in pygame.event.get():   
        if event.type == pygame.KEYDOWN:   
            if event.key in (pygame.K_x, pygame.K_q, pygame.K_e): 
                running = False 

    
    screen.fill(black) 

    # draw balls
    pygame.draw.circle(screen, color1, position, radius)
    pygame.draw.circle(screen, color2, ball2, radius)
    pygame.draw.circle(screen, color3, ball3, radius)

    #movement
    position[0] += speed[0]
    position[1] += speed[1]
    ball2[0] += speed2[0]
    ball2[1] += speed2[1]
    ball3[0] += speed3[0]
    ball3[1] += speed3[1]

    
    pygame.time.wait(10)

    #ball 1
    if position[0] + radius > 500 or position[0] - radius < 0:  
        speed[0] = -speed[0]
        color1 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    if position[1] + radius > 500 or position[1] - radius < 0:
        speed[1] = -speed[1]
        color1 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

    #ball 2
    if ball2[0] + radius > 500 or ball2[0] - radius < 0:  
        speed2[0] = -speed2[0]
        color2 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    if ball2[1] + radius > 500 or ball2[1] - radius < 0:
        speed2[1] = -speed2[1]
        color2 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

    #ball 3
    if ball3[0] + radius > 500 or ball3[0] - radius < 0:  
        speed3[0] = -speed3[0]
        color3 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    if ball3[1] + radius > 500 or ball3[1] - radius < 0:
        speed3[1] = -speed3[1]
        color3 = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

    pygame.display.update()