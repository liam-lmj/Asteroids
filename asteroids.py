from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)

            split_vector_1 = self.velocity.rotate(angle)
            split_vector_2 = -self.velocity.rotate(angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_astroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid_1.velocity = split_vector_1 * 1.2

            new_astroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid_2.velocity = split_vector_2 * 1.2 

        self.kill()

        
        
