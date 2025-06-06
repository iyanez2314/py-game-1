import pygame

import player
from asteroid import Asteroid
from constants import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Group Test")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    p = player.Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    Asteroid(100, 100, 30)
    Asteroid(200, 150, 20)
    Asteroid(300, 200, 40)
    Asteroid(200, 120, 30)
    Asteroid(200, 200, 20)
    Asteroid(300, 200, 40)

    Asteroid(100, 100, 30)
    Asteroid(200, 150, 20)
    Asteroid(300, 200, 40)
    Asteroid(200, 120, 30)
    Asteroid(200, 200, 20)
    Asteroid(300, 200, 40)

    Asteroid(100, 100, 30)
    Asteroid(200, 150, 20)
    Asteroid(300, 200, 40)
    Asteroid(200, 120, 30)
    Asteroid(200, 200, 20)
    Asteroid(300, 200, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill("black")

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    print("Shot hit asteroid!")
                    # Handle collision (e.g., remove asteroid, remove shot, etc.)
                    asteroid.kill()
                    shot.kill()

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
