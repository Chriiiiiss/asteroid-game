import pygame
from pygame.math import Vector2
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.cooldown = 0
        self.score = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) #type: ignore

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius #type: ignore
        b = self.position - forward * self.radius - right #type: ignore
        c = self.position - forward * self.radius + right #type: ignore

        return [a, b, c]


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                return
            self.shoot()
            self.cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

