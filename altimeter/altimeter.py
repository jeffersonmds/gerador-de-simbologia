import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.141592653
pygame.init()

# 600x600 sized screen
screen = pygame.display.set_mode([600, 600])

# This sets the name of the window
pygame.display.set_caption('Altimetro')

clock = pygame.time.Clock()

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("background_altimeter.png").convert()
seta3 = pygame.image.load("seta3.png")#.convert()
seta1 = pygame.image.load("seta1.png")#.convert()
seta2 = pygame.image.load("seta2.png")#.convert()

seta1.set_colorkey(BLACK)

done = False
angle = 0
descendo = True

def rotaciona_alt(image, angle):
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
    screen.blit(rotaciona_alt(seta3, angle), background_position)
    screen.blit(rotaciona_alt(seta1, angle), background_position)
    screen.blit(rotaciona_alt(seta2, angle), background_position)

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


    #x = 127.5 * math.sin(angle) + 171.5
    #y = 127.5 * math.cos(angle) + 129.5
    # Draw the line from the center to the calculated end spot
    #pygame.draw.line(screen, WHITE, [171.5, 129.5], [x, y], 6)
    #screen.blit(seta1, [x, y])


    velocidade = 100

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
        angle = angle + .1
        descendo = False
    elif keys[pygame.K_DOWN]:
        angle = angle - .1
        descendo = True
    elif descendo == True:
        angle = angle - .1
    else:
        angle = angle + .1
    # If we have done a full sweep, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI

    pygame.display.flip()
    clock.tick(velocidade)

pygame.quit()
