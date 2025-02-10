import pygame
import sys
from pygame import RESIZABLE

# 🎮 Инициализация pygame
pygame.init()

# 🎨 Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK_BLUE = (7, 91, 89)
DARK_BLUE = (13, 150, 147)  # Серый цвет текста при нажатии

# 📏 Параметры экрана
WIDTH, HEIGHT = 768, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Menu Test")

# 📌 Фон меню
background = pygame.image.load("menu_background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабируем под экран

# 🔘 Класс кнопки с текстом
class Button:
    def __init__(self, x, y, normal_image, pressed_image, text, font, size=(150, 50), action=None):
        """Инициализация кнопки"""
        self.normal_image = pygame.image.load(normal_image)  # Обычное состояние
        self.pressed_image = pygame.image.load(pressed_image)  # Состояние нажатия

        self.normal_image = pygame.transform.scale(self.normal_image, size)
        self.pressed_image = pygame.transform.scale(self.pressed_image, size)

        self.size = size  # Сохраняем размер кнопки
        self.x = x  # Смещение по горизонтали (от центра экрана)
        self.y = y  # Смещение по вертикали (от центра экрана)

        self.image = self.normal_image  # Текущее изображение
        self.rect = self.normal_image.get_rect(center=(WIDTH // 2 + self.x, self.y))

        # 🔤 **Добавляем текст**
        self.text = text
        self.font = font
        self.text_color_normal = DARK_BLUE  # Цвет текста по умолчанию
        self.text_color_pressed = BLACK_BLUE  # Цвет текста при нажатии
        self.text_color = self.text_color_normal  # Текущий цвет текста

        self.action = action  # Действие при нажатии
        self.pressed = False  # Флаг нажатия

    def update_position(self, new_width, new_height):
        """Обновляет позицию кнопки при изменении размера экрана"""
        self.rect.center = (new_width // 2 + self.x, self.y)

    def draw(self, screen):
        """Рисует кнопку на экране"""
        screen.blit(self.image, self.rect.topleft)

        # Отрисовка текста поверх кнопки
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        """Обрабатывает события кнопки"""
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.image = self.pressed_image  # Меняем картинку при нажатии
            self.text_color = self.text_color_pressed  # Меняем цвет текста
            self.pressed = True

        elif event.type == pygame.MOUSEBUTTONUP and self.pressed:
            self.image = self.normal_image  # Возвращаем обычное состояние
            self.text_color = self.text_color_normal  # Возвращаем цвет текста
            self.pressed = False
            if self.action:
                self.action()  # Выполняем действие кнопки

# 🎯 **Функции действий кнопок**
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

button_font = pygame.font.Font("pixel_font.ttf", 36)  # Используем кастомный шрифт


# 🔘 **Создаём 4 кнопки с текстом**
button1 = Button(0, 160, "normal_button.png", "pressed_button.png", "EASY", button_font, size=(200, 70), action=start_game)
button2 = Button(0, 240, "normal_button.png", "pressed_button.png", "MIDDLE", button_font, size=(200, 70), action=settings)
button3 = Button(0, 320, "normal_button.png", "pressed_button.png", "HARD", button_font, size=(200, 70), action=about)
button4 = Button(0, 400, "normal_button.png", "pressed_button.png", "SETTINGS", button_font, size=(200, 70), action=exit_game)

buttons = [button1, button2, button3, button4]  # Список кнопок для удобства

def handle_events():
    """Функция обработки событий (закрытие окна, изменение размера, клик)"""
    global WIDTH, HEIGHT, screen, background  # Глобальные переменные
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
            background = pygame.transform.scale(pygame.image.load("menu_background.png"), (WIDTH, HEIGHT))
            # 🔥 Обновляем позиции кнопок при изменении размера окна
            for button in buttons:
                button.update_position(WIDTH, HEIGHT)

        for button in buttons:  # Обрабатываем все кнопки
            button.handle_event(event)

def draw_screen():
    """Функция отрисовки экрана"""
    screen.fill(BLACK)  # Очищаем экран
    screen.blit(background, (0, 0))  # Отображаем фон

    # 📝 **Отрисовка заголовка "MENU"**
    font = pygame.font.Font("pixel_font.ttf", 72)  # Загружаем кастомный шрифт
    text_surface = font.render("MENU", True, WHITE)  # Создаём текст
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 70))  # Размещаем по центру
    screen.blit(text_surface, text_rect)  # Рисуем текст на экране

    # 🔘 **Отрисовка всех кнопок**
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()  # Обновляем экран

def main_menu():
    """Главный игровой цикл"""
    while True:
        handle_events()  # Обрабатываем события
        draw_screen()  # Отрисовываем экран

# 🚀 **Запуск игры**
if __name__ == "__main__":
    main_menu()

