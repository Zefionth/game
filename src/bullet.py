import pygame
from src.utils import load_image

class Bullet:
    def __init__(self, x, y, dx, dy, WIDTH, HEIGHT):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = load_image("assets/images/bullet.png", (60, 60))
        self.size = self.image.get_size()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))

    def is_off_screen(self):
        return self.x < 0 or self.x > self.WIDTH or self.y < 0 or self.y > self.HEIGHT

    def check_collision(self, enemy):
        return (self.x > enemy.x and self.x < enemy.x + enemy.size and
                self.y > enemy.y and self.y < enemy.y + enemy.size)