import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidField = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable,drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField()
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        updatable.update(dt)    
        screen.fill('black')
        for dr in drawable:
            dr.draw(screen, 'white')

        for ast in asteroids:
           if ast.collides_with(player):
               log_event("player_hit")
               print("Game over!")
               sys.exit(1)

        for ast in asteroids:
            for sh in shots:
                if sh.collides_with(ast):
                    log_event("asteroid_shot")
                    sh.kill()
                    ast.split()
                    
               
        pygame.display.flip()   
            
            

if __name__ == "__main__":
    main()
