from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        pos_vec, neg_vec = self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1, ast2 = [Asteroid(self.position.x, self.position.y, new_radius) for _ in range(2)]
        ast1.velocity = pos_vec * 1.2
        ast2.velocity = neg_vec
        
