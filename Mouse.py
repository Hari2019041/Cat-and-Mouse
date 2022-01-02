from config import *
from functions import *

class Mouse:
    def __init__(self, x=WIDTH//2, y=HEIGHT//2, color=GRAY):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.angular_position = calculate_angle(self.position)
        self.size = 2
        self.speed = MOUSE_SPEED
        self.radius_of_rotation = 0
        self.color = color
        self.angle = 0

    def show(self):
        pygame.draw.circle(SCREEN, self.color, self.position, self.size, self.size)

    def update_pos(self, radius):
        self.position = self.x, self.y = point_on_circle(self.angular_position, radius)

    def is_on_land(self):
        return distance(CENTER, self.position)>=RADIUS

    def rotate(self, radius, direction):
        self.omega = self.speed/radius
        self.angular_position += -self.omega if direction=="C" else self.omega
        self.radius_of_rotation = radius
        self.update_pos(radius)

    def translate(self, angle):
        self.x += self.speed*cos(angle)
        self.y -= self.speed*sin(angle)
        self.position = (self.x, self.y)

    def dash_tactic(self):
        angle = calculate_angle(self.position)
        self.translate(angle)
        self.speed = 1000 if self.is_on_land() else self.speed

    def away_tactic(self, cat):
        angular_position = cat.angular_position+pi
        away_point = point_on_circle(angular_position)
        pygame.draw.line(SCREEN, BLACK, cat.position, away_point)
        pygame.draw.line(SCREEN, BLACK, self.position, away_point)
        angle = calculate_angle(away_point)
        self.translate(angle)
