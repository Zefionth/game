import pygame
import math
from src.utils import load_image

class Player:
    def __init__(self, WIDTH, HEIGHT):
        self.image = load_image("assets/images/player.png", (150, 150))  # Увеличиваем размер
        self.size = self.image.get_size()
        self.x = WIDTH // 2 - self.size[0] // 2
        self.y = HEIGHT // 2 - self.size[1] // 2
        self.speed = 5
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def move(self, keys):
        move_x, move_y = 0, 0
        if keys[pygame.K_w] and self.y > 0:
            move_y -= 1
        if keys[pygame.K_s] and self.y < self.HEIGHT - self.size[1]:
            move_y += 1
        if keys[pygame.K_a] and self.x > 0:
            move_x -= 1
        if keys[pygame.K_d] and self.x < self.WIDTH - self.size[0]:
            move_x += 1

        # Нормализация движения
        if move_x != 0 or move_y != 0:
            length = math.sqrt(move_x**2 + move_y**2)
            move_x, move_y = move_x / length, move_y / length
        self.x += move_x * self.speed
        self.y += move_y * self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))