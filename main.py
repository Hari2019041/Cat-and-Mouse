from config import *
from functions import *
from Mouse import Mouse
from Cat import Cat
from Pond import Pond

class Simulation:
    def __init__(self):
        self.RUNNING = True
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.pond = Pond()
        self.mouse = Mouse(300, 300)
        self.cat = Cat()
        self.dash_boundary = (1-pi/4)*RADIUS
        self.circling_boundary = RADIUS/4
        self.mouse_in_position = False
        self.cat_opposite_mouse = False

    def show_center(self):
        pygame.draw.circle(SCREEN, WHITE, CENTER, 1, 1)

    def show_circling_boundary(self):
        pygame.draw.circle(SCREEN, GREEN, CENTER, self.circling_boundary, 1)

    def show_dash_boundary(self):
        pygame.draw.circle(SCREEN, RED, CENTER, self.dash_boundary, 1)

    def is_mouse_inside_pond(self):
        return distance(CENTER, self.mouse.position)<=RADIUS

    def is_cat_catch_mouse(self):
        return distance(self.cat.position, self.mouse.position)<=self.mouse.size+self.cat.size

    def is_cat_opposite_mouse(self):
        tangent_point, pos = create_tangent(self.cat.position)
        angle = calculate_angle(O=CENTER, A=tangent_point, C=self.mouse.position)
        return angle*180/pi>179

    def is_mouse_in_position(self):
        return distance(CENTER, self.mouse.position)>=self.circling_boundary-1

    def get_into_position(self):
        self.mouse.dash_tactic()

    def circling_tactic(self, radius):
        self.mouse.rotate(radius, "C")

    def escape_tactic(self):
        if self.mouse_in_position and self.cat_opposite_mouse:
            return self.mouse.dash_tactic()
        self.get_into_position()
        if not self.is_mouse_in_position():
            return
        self.mouse_in_position = True
        self.mouse.rotate(self.circling_boundary, "C")
        if not self.is_cat_opposite_mouse():
            return
        self.cat_opposite_mouse = True

    def start_simulation(self):
        while self.RUNNING:
            self.clock.tick(self.FPS)
            SCREEN.fill(WHITE)
            for event in pygame.event.get():
                self.RUNNING = False if event.type==pygame.QUIT else True

            self.pond.show()
            self.show_center()
            self.mouse.show()
            self.cat.show()
            self.cat.chase(self.mouse)
            self.show_circling_boundary()
            self.show_dash_boundary()

            self.escape_tactic()
            pygame.draw.line(SCREEN, BLACK, self.pond.center, self.mouse.position)
            pygame.draw.line(SCREEN, BLACK, self.pond.center, self.cat.position)
            pygame.display.update()


def main():
    set_window(TITLE, ICON)
    simulation = Simulation()
    simulation.start_simulation()

if __name__ == '__main__':
    main()
