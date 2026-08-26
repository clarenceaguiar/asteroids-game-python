import random
from typing import override

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position: pygame.Vector2 = self.position + (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle: float = random.uniform(20, 50)
            rotate1: pygame.Vector2 = self.velocity.rotate(random_angle)
            rotate2: pygame.Vector2 = self.velocity.rotate(-random_angle)
            new_radius: float = self.radius - ASTEROID_MIN_RADIUS
            asteroid1: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = rotate1 * 1.2
            asteroid2.velocity = rotate2 * 1.2
