import pygame
import sys
import random
from constants import *
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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Initialize scoring system
    score = 0
    font = pygame.font.SysFont(None, 36)  # Set up font for score display

    # Initialize lives and respawn variables
    lives = 3
    respawn_timer = 0
    respawn_delay = 2  # seconds
    player_alive = True

    # Create player at center
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.shots_group = shots

    asteroid_field = AsteroidField()

    # Spawn initial asteroids, ensuring they do NOT collide with the player
    for _ in range(5):
        while True:
            x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
            velocity = pygame.Vector2(random.uniform(-50, 50), random.uniform(-50, 50))
            distance = pygame.Vector2(x - player.position.x, y - player.position.y).length()
            if distance > 100:
                Asteroid(x, y, ASTEROID_MAX_RADIUS, velocity)
                break

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dt = clock.tick(60) / 1000
        asteroid_field.update(dt)
        updatable.update(dt)

        if player_alive:
            # Check for player-asteroid collisions
            for asteroid in asteroids:
                if player.collide(asteroid):
                    lives -= 1
                    player_alive = False
                    respawn_timer = respawn_delay
                    print(f'Life lost! Lives remaining: {lives}')
                    if lives <= 0:
                        print("Game over!")
                        pygame.quit()
                        sys.exit()
                    # Remove player from drawable and updatable groups
                    player.kill()
                    break
        else:
            respawn_timer -= dt
            if respawn_timer <= 0 and lives > 0:
                # Respawn the player at center
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                player.shots_group = shots
                Player.containers = (updatable, drawable)  # Ensure new player is added to groups
                player_alive = True

        # Check for shot-asteroid collisions with scoring
        for shot in list(shots):
            for asteroid in list(asteroids):
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    # Example scoring (you can update to your scoring scheme)
                    size_score_map = {
                        ASTEROID_MAX_RADIUS: 25,
                        ASTEROID_MIN_RADIUS * 2: 35,
                        ASTEROID_MIN_RADIUS: 50
                    }
                    asteroid_score = size_score_map.get(asteroid.radius, 0)
                    score += asteroid_score
                    break

        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Display the score and lives on screen
        score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
        lives_surface = font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        screen.blit(lives_surface, (10, 50))

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
