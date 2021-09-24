import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 600
HEIGHT = 600
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
    def __init__(self):
        pass

    def show(self):
        pass


class Simulation:
    def __init__(self):
        pass

    def startSimulation(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
