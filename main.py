import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def draw_heart(screen, lives_count, spacing=35, y=10):
    heart_img = pygame.image.load('sprite/heart.png').convert_alpha()
    heart_img = pygame.transform.scale(heart_img, (30, 30))
    total_width = lives_count * spacing
    start_x = SCREEN_WIDTH - total_width - 10

    for i in range(lives_count):
        screen.blit(heart_img, (start_x + i * spacing, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_font = pygame.font.SysFont('Comic Sans MS', 30)
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
        surface_txt = game_font.render(f"Score : {player.score}", True, "white")

        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids_group:
            if asteroid.is_colliding(player):
                player.lives_count -= 1
                if player.lives_count <= 0:
                    print("Game Over!")
                    sys.exit(1)
                player.respawn()
            for shot in shot_group:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split(player)

        screen.fill("black")
        screen.blit(surface_txt, (0,0))
        draw_heart(screen, player.lives_count)
        for drawable_item in drawable_group:
            drawable_item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
