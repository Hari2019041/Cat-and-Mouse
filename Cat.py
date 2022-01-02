from config import *
from functions import *

class Cat:
    def __init__(self, x=WIDTH//2, y=MARGIN, color=BLACK):
        self.x, self.y = x, y
        self.position = (self.x, self.y)
        self.angular_position = pi/2
        self.center = CENTER
        self.size = 10
        self.radius = RADIUS + self.size
        self.speed = CAT_SPEED
        self.omega = self.speed/self.radius
        self.color = color

    def update_pos(self):
        self.position = self.x, self.y = point_on_circle(self.angular_position, self.radius)

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.position, self.size, self.size)

    def rotate(self, direction):
        self.angular_position += -self.omega if direction=="C" else self.omega
        self.update_pos()

    def chase(self, mouse):
        tangent_point, pos = create_tangent(self.position)
        angle = calculate_angle(O=tangent_point, A=pos, C=mouse.position)
        self.rotate("C") if angle<pi/2 else self.rotate("A")
