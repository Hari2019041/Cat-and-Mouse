from config import *
from functions import *

class Pond:
    def __init__(self, color=BLUE):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.center = (self.x, self.y)
        self.color = color
        self.radius = HEIGHT//2 - MARGIN

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.radius, self.radius)
