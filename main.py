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
CENTER = (WIDTH//2, HEIGHT//2)
RADIUS = HEIGHT//2 - MARGIN

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

def calculate_angle(C, O=CENTER, A=(CENTER[0]+RADIUS*math.cos(0), CENTER[1]-RADIUS*math.sin(0))):
    OC = distance(O, C)
    AC = distance(A, C)
    OA = distance(O, A)
    if OC != 0:
        angle = math.acos((OC**2+OA**2-AC**2)/(2*OA*OC))
        angle = 2*math.pi-angle if O == CENTER and C[1] > O[1] else angle
    else:
        angle = 0
    return angle

def create_tangent(point):
    angle = calculate_angle(point)
    tangent_angle = (angle-math.pi/2)%(2*math.pi)
    tangent_point = CENTER[0]+RADIUS*math.cos(angle), CENTER[1]-RADIUS*math.sin(angle)
    r = 100
    pos = tangent_point[0]+r*math.cos(tangent_angle), tangent_point[1]-r*math.sin(tangent_angle)
    return tangent_point, pos

class Mouse:
    def __init__(self, x=WIDTH//2, y=HEIGHT//2, color=GRAY):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.angular_position = calculate_angle(self.position)
        self.speed = 1
        self.color = color
        self.size = 2
        self.angle = 0

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.position, self.size, self.size)

    def rotate(self, radius, direction):
        self.angular_position += -self.omega if direction=="C" else self.omega
        self.update_pos()

    def translate(self, angle):
        self.x += self.speed*math.cos(angle)
        self.y -= self.speed*math.sin(angle)
        self.position = (self.x, self.y)

    def dash_tactic(self):
        angle = calculate_angle(self.position)
        self.translate(angle)

    def away_tactic(self, cat):
        angular_position = cat.angular_position+math.pi
        away_point = CENTER[0] + RADIUS*math.cos(angular_position), CENTER[1] - RADIUS*math.sin(angular_position)
        pygame.draw.line(SCREEN, BLACK, cat.position, away_point)
        pygame.draw.line(SCREEN, BLACK, self.position, away_point)

        angle = calculate_angle(away_point)
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

    def chase(self, mouse):
        tangent_point, pos = create_tangent(self.position)
        angle = calculate_angle(O=tangent_point, A=pos, C=mouse.position)
        self.rotate("C") if angle < math.pi/2 else self.rotate("A")

class Pond:
    def __init__(self, color=BLUE):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.center = (self.x, self.y)
        self.color = color
        self.radius = HEIGHT//2 - MARGIN

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.radius, self.radius)


class Simulation:
    def __init__(self):
        self.RUNNING = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.pond = Pond()
        self.mouse = Mouse(300, 350)
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
            self.mouse.dash_tactic()
            # self.mouse.away_tactic(self.cat)
            # self.cat.rotate("C")
            self.cat.chase(self.mouse)
            # self.mouse.translate(-math.pi/4)
            pygame.draw.line(SCREEN, WHITE, self.pond.center, self.mouse.position)
            # create_tangent(self.cat.position)
            pygame.display.update()


def main():
    set_window(TITLE, ICON)
    simulation = Simulation()
    simulation.start_simulation()

if __name__ == '__main__':
    main()
