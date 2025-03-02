import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity  # Set velocity for movement

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (200, 200, 200),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt  # Move the asteroid

    def split(self):
        """Splits the asteroid into two smaller asteroids if it's large enough."""
        self.kill()  # Remove this asteroid

        # If the asteroid is too small, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  

        # Generate a random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocities for the smaller asteroids
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2  # Move faster
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Opposite direction

        # Compute the new smaller asteroid radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the same position
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)
