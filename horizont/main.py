import pygame
import math
class Main:
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
    pygame.display.set_caption('Horizonte Artificial')

    #Setar o ícone do programa
    icon = pygame.image.load('icon.ico').convert()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()
    x1 = -398
    y1 = -381

    # Set positions
    background_position = [x1, y1]

    # Load and set up graphics.
    background_image = pygame.image.load("background2.png")#.convert()
    static = pygame.image.load("static.png")

    done = False
    flag = 0
    angle = 0
    velocidade = 50
    descendo = True

    def rotaciona_horiz(image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image



    screen.blit(background_image, background_position)
    while not done:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True

       # Copy image to screen:
       screen.blit(rotaciona_horiz(background_image, angle), background_position)
       screen.blit(static, [0,0])

       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           angle = angle + .1
           descendo = False
       elif keys[pygame.K_RIGHT]:
           angle = angle - .1
           descendo = True
       elif keys[pygame.K_UP]:
           y1 = y1 - .1
       elif keys[pygame.K_DOWN]:
           y1 = y1 + .1
       elif descendo == True:
           angle = angle - .1
       else:
           angle = angle + .01

       # If we have done a full sweep, reset the angle to 0
       #if angle > 2 * PI:
       #    angle = angle - 2 * PI
       background_position = [x1, y1]
       pygame.display.flip()
       clock.tick(velocidade)
    pygame.quit()
