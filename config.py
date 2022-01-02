import pygame
import random
from math import cos, sin, asin, acos, pi

pygame.init()
pygame.font.init()
pygame.mixer.init()

# Configurations
WIDTH = 600
HEIGHT = 600
MARGIN = 50
TITLE = "Cat and Mouse"
ICON = pygame.image.load('icon.png')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTER = (WIDTH//2, HEIGHT//2)
RADIUS = HEIGHT//2 - MARGIN
MOUSE_SPEED = 1
CAT_SPEED = 4*MOUSE_SPEED

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 200, 255)

def set_window(TITLE, ICON):
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)
