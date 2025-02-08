import pygame
import sys
from pygame import RESIZABLE

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 960, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Menu test")


background = pygame.image.load("MenuBackground.png")  # Укажите ваш файл
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабируем под экран

# Скорость обновления кадров
#clock = pygame.time.Clock()

def main_menu():
    global screen, WIDTH, HEIGHT, background  # Используем глобальные переменные

    running = True
    while running:
        screen.fill((0, 0, 0))  # Очищаем экран

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
                background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабируем фон

        # Отображаем фон
        screen.blit(background, (0, 0))

        # Отрисовка текста
        font = pygame.font.Font(None, 72)
        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()  # Обновляем экран
  #      clock.tick(60)  # Ограничение FPS

if __name__ == "__main__":
    main_menu()
