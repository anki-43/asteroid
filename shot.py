from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS,LINE_WIDTH

class Shot(CircleShape): 

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    
        
