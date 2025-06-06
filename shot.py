import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for container in Shot.containers:
            container.add(self)

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(
            screen,
            "yellow",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            width=2,
        )

    def update(self, dt):
        # Move in a straight line
        self.position += self.velocity * dt
