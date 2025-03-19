import pygame
from src.utils import load_image

class Enemy:
    def __init__(self, x, y, size, speed, image_path, WIDTH, HEIGHT):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.image = load_image(image_path, (size, size))  # Масштабируем изображение
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def move_towards(self, player):
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
        if self.y < player.y:
            self.y += self.speed
        elif self.y > player.y:
            self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, player):
        return (player.x < self.x + self.size and player.x + player.size[0] > self.x and
                player.y < self.y + self.size and player.y + player.size[1] > self.y)