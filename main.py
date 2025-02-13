import pygame
import sys
from pygame import RESIZABLE

from cloud import Cloud
from button import Button

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

# Создание облаков
clouds = [Cloud(WIDTH, HEIGHT, "cloud.png") for _ in range(3)]

# Функции действий кнопок
#def start_game():
 #   print("Игра началась!")

def start_menu(title, buttons):
    while True:
        #def handle_events():
        global WIDTH, HEIGHT, screen, background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
                background = pygame.transform.scale(pygame.image.load("menu_background.png"), (WIDTH, HEIGHT))
                for button_list in [menu_buttons, easy_buttons, middle_buttons, hard_buttons, settings_buttons]:
                    for button in button_list:
                        button.update_position(WIDTH, HEIGHT)
            for button in buttons:
                button.handle_event(event)

        #draw_screen()
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        for cloud in clouds:
            cloud.update()
            cloud.draw(screen)
        for button in buttons:
            button.draw(screen)

        font = pygame.font.Font("pixel_font.ttf", 72)
        text_surface = font.render(title, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 70))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

#створюємо вінка
def easy_menu():
    start_menu("EASY LEVEL", easy_buttons)

def middle_menu():
    start_menu("MIDDLE LEVEL", middle_buttons)

def hard_menu():
    start_menu("HARD LEVEL", hard_buttons)

def settings_menu():
    start_menu("SETTINGS", settings_buttons)

def exit_game():
    print("Выход из игры!")
    pygame.quit()
    sys.exit()

def main_menu():
    start_menu("MENU", menu_buttons)

button_font = pygame.font.Font("pixel_font.ttf", 36)

# Создаём кнопки
menu_buttons = [
    Button(0, 160, "normal_button.png", "pressed_button.png", "EASY", button_font, size=(200, 70), action=easy_menu),
    Button(0, 240, "normal_button.png", "pressed_button.png", "MIDDLE", button_font, size=(200, 70), action=middle_menu),
    Button(0, 320, "normal_button.png", "pressed_button.png", "HARD", button_font, size=(200, 70), action=hard_menu),
    Button(0, 400, "normal_button.png", "pressed_button.png", "SETTINGS", button_font, size=(200, 70), action=settings_menu),
    Button(0, 480, "normal_button.png", "pressed_button.png", "EXIT", button_font, size=(200, 70), action=exit_game)
]

easy_buttons = [
    Button(0, 160, "normal_button.png", "pressed_button.png", "SCORE", button_font, size=(200, 70), action=None),
    Button(0, 240, "normal_button.png", "pressed_button.png", "START", button_font, size=(200, 70), action=None),
    Button(0, 320, "normal_button.png", "pressed_button.png", "BACK", button_font, size=(200, 70), action=main_menu)

]

middle_buttons = [
    Button(0, 160, "normal_button.png", "pressed_button.png", "SCORE", button_font, size=(200, 70), action=None),
    Button(0, 240, "normal_button.png", "pressed_button.png", "START", button_font, size=(200, 70), action=None),
    Button(0, 320, "normal_button.png", "pressed_button.png", "BACK", button_font, size=(200, 70), action=main_menu)

]

hard_buttons = [
    Button(0, 160, "normal_button.png", "pressed_button.png", "SCORE", button_font, size=(200, 70), action=None),
    Button(0, 240, "normal_button.png", "pressed_button.png", "START", button_font, size=(200, 70), action=None),
    Button(0, 320, "normal_button.png", "pressed_button.png", "BACK", button_font, size=(200, 70), action=main_menu)

]

settings_buttons = [
    Button(0, 320, "normal_button.png", "pressed_button.png", "BACK", button_font, size=(200, 70), action=main_menu)

]


if __name__ == "__main__":
    main_menu()

