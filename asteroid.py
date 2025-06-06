import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for container in Asteroid.containers:
            container.add(self)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(
            screen,
            "gray",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            width=2,
        )

    def update(self, dt):
        # Move in a straight line
        self.position += self.velocity * dt

    def split(self):
        # Split the asteroid into two smaller asteroids
        if self.radius > 10:
            new_radius = self.radius // 2
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            # Randomize the velocity of the new asteroids
            asteroid1.velocity.rotate_ip(30)
