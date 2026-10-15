from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape): 

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.randint(20, 50)
        first_vec = self.velocity.rotate(random_angle)
        second_vec = self.velocity.rotate(-random_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        first_ast = Asteroid(self.position.x, self.position.y, new_rad)
        second_ast = Asteroid(self.position.x, self.position.y, new_rad)

        first_ast.velocity = first_vec * 1.2
        second_ast.velocity = second_vec * 1.2