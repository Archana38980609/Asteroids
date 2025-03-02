import pygame
import sys
import random
from constants import *  # Import everything from constants.py
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

BACKGROUND_COLOR = (0, 0, 0)  # Black color

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # NEW: Shot group

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)  # NEW: Add shots to groups
    AsteroidField.containers = (updatable,)

    # Create player at center
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.shots_group = shots  # NEW: Player can now shoot bullets

    asteroid_field = AsteroidField()

    # Spawn initial asteroids, ensuring they do NOT collide with the player
    for _ in range(5):  # Spawning 5 asteroids
        while True:  # Keep trying until a safe location is found
            x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
            velocity = pygame.Vector2(random.uniform(-50, 50), random.uniform(-50, 50))
            
            # Ensure asteroid does NOT spawn too close to player
            distance = pygame.Vector2(x - player.position.x, y - player.position.y).length()
            if distance > 100:  # Only spawn if 100+ pixels away from player
                Asteroid(x, y, ASTEROID_MAX_RADIUS, velocity)
                break  # Stop trying once a valid position is found

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        # Check for player-asteroid collisions
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()

        # NEW: Check for shot-asteroid collisions and split asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collide(asteroid):  
                    shot.kill()  # Remove the bullet
                    asteroid.split()  # NEW: Split instead of just removing
                    break  # Stop checking once this shot has hit something

        # Draw everything
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
