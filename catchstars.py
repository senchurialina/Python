import pygame
import random
from sys import exit 

# ADD IMAGE  CHECKED   
# SHOW "GAME OVER"
# INCREASE LIVES (COLLECT COIN)+ ADD TIME WAIT SO IT WONT RESPAWN EVERY ROUND  CHECKED (EXCEPT WAIT)


pygame.init()

# Screen + colors
screen = pygame.display.set_mode([800,400])
pygame.display.set_caption("Catch the Falling Stars")

ground_color = (16,0,22)
background_color = (28,29,86)
spaceship_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
star_color = (255,244,234)
potion_color = (255,0,0)
red = (255,0,0)
black = (0,0,0)

ground = pygame.Rect(0,350,800,50)   # x,y,width,height
spaceship = pygame.Rect(400,320,50,20) 
star = pygame.Rect(random.randint(50,750),20,30,30)
potion = pygame.Rect(random.randint(250,600),40,30,30)     # EXTRA LIVES


background_image = pygame.image.load("Images/Untitled design (1).png")
background_image = pygame.transform.scale(background_image, (800,400))

spaceship_image = pygame.image.load("Images/planet2.png")
spaceship_image = pygame.transform.scale(spaceship_image, (50,20))

star_image = pygame.image.load("Images/star.png")
star_image = pygame.transform.scale(star_image, (20,20))

potion_image = pygame.image.load("Images/potion-b.png")
potion_image = pygame.transform.scale(potion_image, (30,30))


running = True
clock = pygame.time.Clock()
spaceship_speed = 29
star_speed = 8
potion_speed = 6

score = 0
lives = 5

def respawn_star():
  star.x = random.randint(50,750)
  star.y = 20
def respawn_potion():
 potion.x = random.randint(250,600)    
 potion.y = 20
 
game_font = pygame.font.SysFont(None,40)

game_over = pygame.font.SysFont(None,100)

is_game_over = False

while running: 
  # Event Loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        spaceship.x = spaceship.x - spaceship_speed
      if event.key == pygame.K_RIGHT:
        spaceship.x = spaceship.x + spaceship_speed
        
  #background
  screen.blit(background_image,(0,0))
  if is_game_over:
    continue
  
  # STAR
  star.y = star.y + star_speed
  # star respawn + collision with spaceship  
  if star.bottom >= ground.top:
    respawn_star()
    lives = lives - 1
    if lives <= 0:
      gameover = game_over.render("GAMEOVER!", True, red)
      screen.blit(gameover, (200,150))
      is_game_over = True
  if star.colliderect(spaceship):
    respawn_star()
    score = score + 1
  
  # POTION
  potion.y = potion.y + potion_speed
  if potion.bottom >= ground.top:
   respawn_potion()
  if potion.colliderect(spaceship):
    respawn_potion()
    lives = lives + 1

  

  # SCORE BOARD
  score_surface = game_font.render(f"Score: {score}", True, black)
  screen.blit(score_surface, (20,20))
  lives_surface = game_font.render(f"Lives: {lives}", True, black)
  screen.blit(lives_surface, (690,20))
  
  # IMAGES + GROUND
  # ground
  pygame.draw.rect(screen,ground_color,ground)
  # spaceship
  screen.blit(spaceship_image, spaceship)
  # star
  screen.blit(star_image, star)
  # Potion(xtra lives)
  screen.blit(potion_image, potion)
  pygame.display.update()
  clock.tick(20)