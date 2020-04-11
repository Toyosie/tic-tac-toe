import pygame as pg, sys
from pygame.locals import *
import time

#initializing global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_colour = (10, 10, 10)

# 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]

