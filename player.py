import pygame

import circleshape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        for container in Player.containers:
            container.add(self)

    def draw(self, screen):
        # Draw the player as a triangle
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        # Rotate the player based on the turn speed and delta time
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                return
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        # Move the player forward in the direction it is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_RADIUS * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius
        shot = Shot(shot_position.x, shot_position.y, PLAYER_RADIUS / 4)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
