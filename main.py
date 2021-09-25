import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 600
MARGIN = 50
TITLE = "Cat and Mouse"
ICON = pygame.image.load('icon.png')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def setWindow(TITLE, ICON):
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)

#Colors
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Mouse:
    def __init__(self):
        pass

    def show(self):
        pass


class Cat:
    def __init__(self):
        pass

    def show(self):
        pass


class Pond:
    def __init__(self, color=BLUE):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.center = (self.x, self.y)
        self.color = color
        self.size = WIDTH//2 - MARGIN

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.size, self.size)


class Simulation:
    def __init__(self):
        pass

    def startSimulation(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
