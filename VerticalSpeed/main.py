import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.141592653
pygame.init()

# 400x400 sized screen
screen = pygame.display.set_mode([400, 400])

# This sets the name of the window
pygame.display.set_caption('Indicador de Velocidade Vertical')

clock = pygame.time.Clock()
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("indicador.png")#.convert()
seta = pygame.image.load("seta_vsi.png")

done = False
angle = 0
descendo = True
velocidade = 50

def rotaciona_vsi(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

while not done:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

   # Copy image to screen:
   screen.blit(background_image, background_position)
   screen.blit(rotaciona_vsi(seta, angle), background_position)

   # Get the current mouse position. This returns the position
   # as a list of two numbers.
   #player_position = pygame.mouse.get_pos()
   #x = player_position[0]
   #y = player_position[1]

   # Copy image to screen:
   #screen.blit(player_image, [x, y])

   # Draw the outline of a circle to 'sweep' the line around
   #box_dimensions = [45, 2, 255, 255]
   #pygame.draw.ellipse(screen, GREEN, box_dimensions, 2)
   """
   x = 127.5 * math.sin(angle) + 200
   y = 127.5 * math.cos(angle) + 200
   # Draw the line from the center to the calculated end spot
   pygame.draw.line(screen, WHITE, [200, 200], [x, y], 5)
   #screen.blit(seta1, [x, y])"""




   """
   keys = pygame.key.get_pressed()
   if keys[pygame.K_UP]:
       if descendo == True:
           if velocidade - 10 == 0:
               velocidade = 10;
               descendo = False
               angle = angle - .01
       else:
           velocidade -= 10
           angle = angle + .01
   else:
       if descendo == True:
           angle = angle - .01    # Decrease the angle by 0.03 radians
           #flag = 1;
       else:
           angle = angle + .01

   if keys[pygame.K_DOWN]:
       velocidade += 10
   else:
       if flag == 0:
           angle = angle - .01    # Decrease the angle by 0.03 radians
           flag = 1;"""

   keys = pygame.key.get_pressed()
   if keys[pygame.K_UP]:
       angle = angle + .9
       descendo = False
   elif keys[pygame.K_DOWN]:
       angle = angle - .9
       descendo = True
   elif descendo == True:
       angle = angle - .9
   else:
       angle = angle + .9

   # If we have done a full sweep, reset the angle to 0
   #if angle > 2 * PI:
   #    angle = angle - 2 * PI

   pygame.display.flip()
   clock.tick(velocidade)

pygame.quit()

