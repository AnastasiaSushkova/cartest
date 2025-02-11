import pygame
import sys
import random
from pygame import RESIZABLE

# Инициализация pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK_BLUE = (7, 91, 89)
DARK_BLUE = (13, 150, 147)

# Параметры экрана
WIDTH, HEIGHT = 768, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Menu Test")

# Фон меню
background = pygame.image.load("menu_background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

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


# Создание облаков
clouds = [Cloud(WIDTH, HEIGHT, "cloud.png") for _ in range(3)]

class Button:
    def __init__(self, x, y, normal_image, pressed_image, text, font, size=(150, 50), action=None):
        """Инициализация кнопки"""
        self.normal_image = pygame.image.load(normal_image)
        self.pressed_image = pygame.image.load(pressed_image)
        self.normal_image = pygame.transform.scale(self.normal_image, size)
        self.pressed_image = pygame.transform.scale(self.pressed_image, size)
        self.size = size
        self.x = x
        self.y = y
        self.image = self.normal_image
        self.rect = self.normal_image.get_rect(center=(WIDTH // 2 + self.x, self.y))
        self.text = text
        self.font = font
        self.text_color_normal = DARK_BLUE
        self.text_color_pressed = BLACK_BLUE
        self.text_color = self.text_color_normal
        self.action = action
        self.pressed = False

    def update_position(self, new_width, new_height):
        self.rect.center = (new_width // 2 + self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.image = self.pressed_image
            self.text_color = self.text_color_pressed
            self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP and self.pressed:
            self.image = self.normal_image
            self.text_color = self.text_color_normal
            self.pressed = False
            if self.action:
                self.action()

# Функции действий кнопок
def start_game():
    print("Игра началась!")

def settings():
    print("Открываем настройки!")

def about():
    print("О программе!")

def exit_game():
    print("Выход из игры!")
    pygame.quit()
    sys.exit()

button_font = pygame.font.Font("pixel_font.ttf", 36)

# Создаём кнопки
buttons = [
    Button(0, 160, "normal_button.png", "pressed_button.png", "EASY", button_font, size=(200, 70), action=start_game),
    Button(0, 240, "normal_button.png", "pressed_button.png", "MIDDLE", button_font, size=(200, 70), action=settings),
    Button(0, 320, "normal_button.png", "pressed_button.png", "HARD", button_font, size=(200, 70), action=about),
    Button(0, 400, "normal_button.png", "pressed_button.png", "SETTINGS", button_font, size=(200, 70), action=exit_game)
]

def handle_events():
    global WIDTH, HEIGHT, screen, background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
            background = pygame.transform.scale(pygame.image.load("menu_background.png"), (WIDTH, HEIGHT))
            for button in buttons:
                button.update_position(WIDTH, HEIGHT)
        for button in buttons:
            button.handle_event(event)

def draw_screen():
    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    for cloud in clouds:
        cloud.update()
        cloud.draw(screen)
    for button in buttons:
        button.draw(screen)

    font = pygame.font.Font("pixel_font.ttf", 72)
    text_surface = font.render("MENU", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 70))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def main_menu():
    while True:
        handle_events()
        draw_screen()

if __name__ == "__main__":
    main_menu()

