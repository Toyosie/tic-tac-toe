import pygame as pg, sys
from pygame.locals import *
import time

#initializing global variables
XO = 'x'
winner = None
draw = False
width = 500
height = 400
white = (255, 255, 255)
line_colour = (10, 10, 10)

# 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]

#to initialize a pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption("tIc tAc tOe")

#to load the images
opening = pg.image.load('open.png')
ximg = pg.image.load('X.png')
oimg = pg.image.load('O.png')

#resizing the images
ximg = pg.transform.scale(ximg, (80,80))
oimg = pg.transform.scale(oimg,(80,80))
opening = pg.transform.scale(opening, (width,height+100))



