# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    AsteroidField.containers = (group_updatable)
    Shot.containers = (group_shots, group_updatable, group_drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in group_updatable:
            updatable.update(dt)

        for asteroid in group_asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit()
        
        for asteroid in group_asteroids:
            for shot in group_shots:
                if (asteroid.check_collision(shot)):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for drawable in group_drawable:
            drawable.draw(screen)
        
        pygame.display.flip()

        # limit framerate to 60FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()