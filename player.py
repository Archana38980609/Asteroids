import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SCREEN_WIDTH, SCREEN_HEIGHT 
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = None  # Set this in main()
        self.shoot_timer = 0  # Timer for rate limiting

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

    def shoot(self):
        """Creates and fires a shot only if cooldown has expired."""
        if self.shoot_timer <= 0 and self.shots_group is not None:
            shot = Shot(self.position.x, self.position.y, -self.rotation)
            self.shots_group.add(shot)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset cooldown timer

    def update(self, dt):
        """Handles movement, shooting cooldown, and updates."""
        super().update(dt)

        # Reduce the shoot timer each frame
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rotate(-1, dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(1, dt)
        
        if keys[pygame.K_UP]:
            self.move(1, dt)
        if keys[pygame.K_DOWN]:
            self.move(-1, dt)

        if keys[pygame.K_SPACE]:  # Fire bullet if allowed
            self.shoot()

        if self.position.x > SCREEN_WIDTH + self.radius: 
            self.position.x = 0 - self.radius 
        elif self.position.x < 0 - self.radius: 
            self.position.x = SCREEN_WIDTH + self.radius 

        if self.position.y > SCREEN_HEIGHT + self.radius: 
            self.position.y = 0 - self.radius 
        elif self.position.y < 0 - self.radius: 
            self.position.y = SCREEN_HEIGHT + self.radius 
