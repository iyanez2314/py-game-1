import random

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        angel = random.uniform(0, 360)
        self.velocity = pygame.Vector2(1, 0).rotate(angel) * 100
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        # Check for collision with another CircleShape
        if isinstance(other, CircleShape):
            distance = self.position.distance_to(other.position)
            return distance < (self.radius + other.radius)
        return False
