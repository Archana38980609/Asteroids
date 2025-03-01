import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)
        right = pygame.Vector2(1, 0).rotate(-self.rotation) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius / 2 - right
        c = self.position - forward * self.radius / 2 + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, direction, dt):
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)
        self.position += forward * direction * PLAYER_SPEED * dt

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rotate(-1, dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(1, dt)
        
        if keys[pygame.K_UP]:
            self.move(1, dt)
        if keys[pygame.K_DOWN]:
            self.move(-1, dt)