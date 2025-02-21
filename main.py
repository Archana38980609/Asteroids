import pygame
from constants import *  # Import everything from constants.py

# Define a background color
BACKGROUND_COLOR = (0, 0, 0)  # Black color

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
