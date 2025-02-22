import pygame
from constants import *  # Import everything from constants.py
from player import Player

# Define a background color
BACKGROUND_COLOR = (0, 0, 0)  # Black color

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        player.update(dt)
        player.draw(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

