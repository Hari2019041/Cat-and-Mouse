import pygame
import random
import math

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

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 70, 255)

def setWindow(TITLE, ICON):
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)


class Mouse:
    def __init__(self, x, y, color=GRAY):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.speed = 1
        self.color = color
        self.size = 2

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.position, self.size, self.size)

    def move(self, angle):
        self.x += self.speed*math.cos(angle)
        self.y -= self.speed*math.sin(angle)
        self.position = (self.x, self.y)

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
        self.RUNNING = True
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.pond = Pond()
        self.mouse = Mouse(WIDTH//2, HEIGHT//2)
        self.cat = Cat()


    def startSimulation(self):
        while self.RUNNING:
            self.clock.tick(self.FPS)
            SCREEN.fill(WHITE)
            for event in pygame.event.get():
                self.RUNNING = False if event.type == pygame.QUIT else True
            self.pond.show()
            self.mouse.show()
            self.mouse.move(math.pi/2)

            pygame.display.update()


def main():
    simulation = Simulation()
    simulation.startSimulation()

if __name__ == '__main__':
    main()
