import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    AsteroidField.containers = (updatable) #type: ignore
    Asteroid.containers = (updatable, drawable_group, asteroids_group) #type: ignore
    Player.containers = (updatable, drawable_group) #type: ignore
    Shot.containers = (shot_group, updatable, drawable_group) #type: ignore

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while(True):
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids_group:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit(1)
            for shot in shot_group:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for drawable_item in drawable_group:
            drawable_item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
