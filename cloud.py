import pygame
import random

WIDTH, HEIGHT = 768, 768

class Cloud:
    def __init__(self, screen_width, screen_height, image_path):
        """Инициализация облака, появляющегося слева и двигающегося вправо."""
        self.image = pygame.image.load(image_path)

        # Генерация случайного размера облака
        size_factor = random.uniform(0.8, 1.5)  # Масштаб от 80% до 150%
        self.width = int(150 * size_factor)
        self.height = int(60 * size_factor)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Устанавливаем начальную позицию (слева за экраном)
        self.x = -self.width  # Теперь облако появляется слева
        self.y = random.randint(10, 250)  # Высота появления

        # Случайная скорость (вправо)
        self.speed = random.uniform(2, 4)

    def update(self):
        """Обновляет положение облака (движение вправо)."""
        self.x += self.speed  # Двигаем облако вправо

        # Если облако полностью ушло за правый край экрана - перезапускаем его
        if self.x > WIDTH:
            self.reset()

    def reset(self):
        """Перезапускает облако слева с новым размером и высотой."""
        self.x = -self.width  # Снова появляется слева за экраном
        self.y = random.randint(50, 250)  # Новая случайная высота

        # Генерация нового размера облака
        size_factor = random.uniform(0.8, 1.5)
        self.width = int(100 * size_factor)
        self.height = int(60 * size_factor)
        self.image = pygame.transform.scale(pygame.image.load("cloud.png"), (self.width, self.height))

        # Новая случайная скорость
        self.speed = random.uniform(2, 4)

    def draw(self, screen):
        """Рисует облако на экране."""
        screen.blit(self.image, (self.x, self.y))