import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y , radius):
        super().__init__(x, y , radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle_number = random.uniform(20, 50)

        random_angle = self.velocity.rotate(random_angle_number)
        invert_random_angle = self.velocity.rotate(-random_angle_number)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        first_splitted_asteroid = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        second_splitted_asteroid =  Asteroid(self.position[0], self.position[1], new_asteroid_radius)

        first_splitted_asteroid.velocity = random_angle * 1.2
        second_splitted_asteroid.velocity = invert_random_angle * 1.2

