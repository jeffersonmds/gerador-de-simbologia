"""
import pygame, sys, time
from math import *
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

surface = pygame.display.set_mode((500,500),0, 30)

class PlaceHolder:
    def __init__(self, win, left, top, width, height, color):
        self.win = win
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color

    def move(self,x,y,duration):
        #self.rect = self.rect.move(self.velocity[0],self.velocity[1])
        xpointlist = [60, 60]
        ypointlist = [236, 136]
        self.rect.left += x
        self.rect.top += y
        self.duration = duration
        counter = 0
        rate = 10
        for counter in range(len(xpointlist)-1):
            dx = x - xpointlist[counter]
            dy = y - ypointlist[counter]
            distance = sqrt(dx*dx + dy*dy)
            return distance
        duration = distance/rate

    def draw(self):
        pygame.draw.ellipse(surface, self.color, self.rect, 0)

class projectWin:
    def __init__(self, width, height, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.width = width
        self.height = height
        self.placeHolders = []
        self.placeHolders.append(PlaceHolder(surface, 1, 236, 10, 10, GREEN))
        #placeHolder1 = PlaceHolder(surface, 10, 236, 10, 10, GREEN)

    def grid(self):
        for i in range(24, 499, 25): #draw the vertical lines
            pygame.draw.line(surface, WHITE, (i, 0), (i, 499), 1)
        for j in range(24, 499, 25): #draw the horizontal lines
        pygame.draw.line(surface, WHITE, (0, j), (499, j), 1)

    def path(self):
        #the two lines are separated for ease of change
        #line 1
        pygame.draw.line(surface, GREEN, (0, 224), (49, 224), 2)
        pygame.draw.line(surface, GREEN, (49, 224), (49, 149), 2)
        pygame.draw.line(surface, GREEN, (49, 149), (349, 149), 2)
        pygame.draw.line(surface, GREEN, (349, 149), (349, 274), 2)
        pygame.draw.line(surface, GREEN, (349, 274), (99, 274), 2)
        pygame.draw.line(surface, GREEN, (99, 274), (99, 349), 2)
        pygame.draw.line(surface, GREEN, (99, 349), (374, 349), 2)
        pygame.draw.line(surface, GREEN, (374, 349), (374, 224), 2)
        pygame.draw.line(surface, GREEN, (374, 224), (499, 224), 2)

        #line 2
        pygame.draw.line(surface, GREEN, (0, 249), (74, 249), 2)
        pygame.draw.line(surface, GREEN, (74, 249), (74, 174), 2)
        pygame.draw.line(surface, GREEN, (74, 174), (324, 174), 2)
        pygame.draw.line(surface, GREEN, (324, 174), (324, 249), 2)
        pygame.draw.line(surface, GREEN, (324, 249), (75, 249), 2)
        pygame.draw.line(surface, GREEN, (74, 249), (74, 374), 2)
        pygame.draw.line(surface, GREEN, (74, 374), (399, 374), 2)
        pygame.draw.line(surface, GREEN, (399, 374), (399, 249), 2)
        pygame.draw.line(surface, GREEN, (399, 249), (499, 249), 2)

    def base(self): #what the player has to protect
        base = pygame.Rect(474, 187, 99, 99)
        pygame.draw.ellipse(surface, BLUE, base, 0)

pygame.init()

win = projectWin(500, 500, 'Project 2 v1.00')
Quit = False
while not Quit:
    surface.fill(BLACK)
    #draw the grid, path, and base on the screen
    win.grid()
    win.path()
    win.base()
    for i in win.placeHolders: #draw and move the placeholder enemy assets
        i.move(59, 0, duration)
        i.move(0, -100, duration)
        i.draw()
    pygame.display.update()
    time.sleep(0.02)
    for event in pygame.event.get():
        if event.type == QUIT:
            Quit = True

pygame.quit() #always exit cleanly
sys.exit()"""