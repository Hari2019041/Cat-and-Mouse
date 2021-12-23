import pygame
import random
import math
import time

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
BLUE = (0, 200, 255)

def set_window(TITLE, ICON):
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)

def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

class Mouse:
    def __init__(self, x=WIDTH//2, y=HEIGHT//2, color=GRAY):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.speed = 1
        self.color = color
        self.size = 2
        self.angle = 0

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.position, self.size, self.size)

    def translate(self, angle):
        self.x += self.speed*math.cos(angle)
        self.y -= self.speed*math.sin(angle)
        self.position = (self.x, self.y)

    def dash_tactic(self, pond):
        center = pond.center
        dis = distance(self.position, center)
        if dis != 0:
            angle = math.asin(abs((center[1]-self.y)/dis))
            if self.x > center[0]:
                angle *= -1 if self.y > center[1] else 1
            else:
                angle = math.pi - angle if self.y < center[1] else angle + math.pi
        else:
            angle = 0
        self.translate(angle)

class Cat:
    def __init__(self, x=WIDTH//2, y=MARGIN, color=BLACK):
        self.size = 10
        self.speed = 4
        self.center = (WIDTH//2, HEIGHT//2)
        self.angular_position = math.pi/2
        self.radius = HEIGHT//2 - MARGIN + self.size
        self.omega = self.speed/self.radius
        self.x = self.center[0] + self.radius*math.cos(self.angular_position)
        self.y = self.center[1] - self.radius*math.sin(self.angular_position)
        self.position = (self.x, self.y)
        self.color = color

    def update_pos(self):
        self.x = self.center[0] + self.radius*math.cos(self.angular_position)
        self.y = self.center[1] - self.radius*math.sin(self.angular_position)
        self.position = (self.x, self.y)

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.position, self.size, self.size)

    def rotate(self, direction):
        self.angular_position += -self.omega if direction=="C" else self.omega
        self.update_pos()

class Pond:
    def __init__(self, color=BLUE):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.center = (self.x, self.y)
        self.color = color
        self.size = HEIGHT//2 - MARGIN

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.size, self.size)


class Simulation:
    def __init__(self):
        self.RUNNING = True
        self.clock = pygame.time.Clock()
        self.FPS = 24
        self.pond = Pond()
        self.mouse = Mouse(150, 150)
        self.cat = Cat()

    def start_simulation(self):
        while self.RUNNING:
            self.clock.tick(self.FPS)
            SCREEN.fill(WHITE)
            for event in pygame.event.get():
                self.RUNNING = False if event.type == pygame.QUIT else True
            self.pond.show()
            pygame.draw.circle(SCREEN, WHITE, (WIDTH//2, HEIGHT//2), 1, 1)
            self.mouse.show()
            self.cat.show()
            self.mouse.dash_tactic(self.pond)
            self.cat.rotate("C")
            # self.mouse.translate(-math.pi/4)
            pygame.draw.line(SCREEN, WHITE, self.pond.center, self.mouse.position)
            pygame.display.update()



def main():
    set_window(TITLE, ICON)
    simulation = Simulation()
    simulation.start_simulation()

if __name__ == '__main__':
    main()
