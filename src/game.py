import pygame
import random
import math
from src.player import Player
from src.enemy import Enemy
from src.bullet import Bullet
from src.utils import load_image

class Game:
    def __init__(self):
        pygame.init()  # Инициализация Pygame
        # Получаем размеры экрана после инициализации Pygame
        info = pygame.display.Info()
        self.WIDTH, self.HEIGHT = info.current_w, info.current_h  # Разрешение экрана
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # Оконный режим
        pygame.display.set_caption("Vampire Survivors Clone")
        self.clock = pygame.time.Clock()
        self.player = Player(self.WIDTH, self.HEIGHT)  # Передаем размеры экрана в Player
        self.enemies = []
        self.bullets = []
        self.score = 0
        self.spawn_rate = 30
        self.enemy_types = [
            {"size": 120, "speed": 2, "image": "assets/images/enemy1.png"},  # Увеличиваем размер
            {"size": 180, "speed": 1, "image": "assets/images/enemy2.png"},  # Увеличиваем размер
            {"size": 90, "speed": 3, "image": "assets/images/enemy3.png"},  # Увеличиваем размер
        ]

    def spawn_enemy(self):
        side = random.choice(["top", "bottom", "left", "right"])
        enemy_type = random.choice(self.enemy_types)
        if side == "top":
            x = random.randint(0, self.WIDTH - enemy_type["size"])
            y = 0
        elif side == "bottom":
            x = random.randint(0, self.WIDTH - enemy_type["size"])
            y = self.HEIGHT - enemy_type["size"]
        elif side == "left":
            x = 0
            y = random.randint(0, self.HEIGHT - enemy_type["size"])
        elif side == "right":
            x = self.WIDTH - enemy_type["size"]
            y = random.randint(0, self.HEIGHT - enemy_type["size"])
        self.enemies.append(Enemy(x, y, enemy_type["size"], enemy_type["speed"], enemy_type["image"], self.WIDTH, self.HEIGHT))

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Закрытие окна (крестик)
                    running = False
                if event.type == pygame.KEYDOWN:  # Обработка нажатия клавиш
                    if event.key == pygame.K_ESCAPE:  # Выход по нажатию ESC
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    angle = math.atan2(mouse_y - self.player.y, mouse_x - self.player.x)
                    self.bullets.append(Bullet(self.player.x + self.player.size[0] // 2, self.player.y + self.player.size[1] // 2, 7 * math.cos(angle), 7 * math.sin(angle), self.WIDTH, self.HEIGHT))

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            if random.randint(1, self.spawn_rate) == 1:
                self.spawn_enemy()

            for enemy in self.enemies[:]:
                enemy.move_towards(self.player)
                enemy.draw(self.screen)
                if enemy.check_collision(self.player):
                    print("Game Over! Final Score:", self.score)
                    running = False

            for bullet in self.bullets[:]:
                bullet.move()
                bullet.draw(self.screen)
                if bullet.is_off_screen():
                    self.bullets.remove(bullet)
                    continue
                for enemy in self.enemies[:]:
                    if bullet.check_collision(enemy):
                        self.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        self.score += 10
                        break

            self.player.draw(self.screen)

            font = pygame.font.SysFont("Arial", 24)
            score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            if self.score > 0 and self.score % 100 == 0:
                self.spawn_rate = max(10, self.spawn_rate - 5)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()