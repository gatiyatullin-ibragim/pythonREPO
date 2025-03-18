import pygame
import sys
from datetime import datetime
import math

pygame.init()

# Окно и параметры
RES = WIDTH, HEIGHT = 1400, 1000
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2

# Создаём окно
surface = pygame.display.set_mode(RES)
pygame.display.set_caption("Mickey Clock")

# Загрузка изображений
bg = pygame.image.load("clock.jpg").convert_alpha()
minute_hand = pygame.image.load("min.png").convert_alpha()
sec_hand = pygame.image.load("sec.png").convert_alpha()

# Настройки шрифта
font = pygame.font.SysFont("Verdana", 30)
clock = pygame.time.Clock()

# Центр часов
clock_center = (H_WIDTH, H_HEIGHT)

def blithand(surf, image, center, angle):
    """Отрисовка повёрнутого изображения"""
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, rotated_rect.topleft)

# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill("white")  # Очистка экрана
    surface.blit(bg, (0, 0))  # Отрисовка фона

    # Получаем текущее время
    t = datetime.now()
    minute_angle = t.minute * 6
    second_angle = t.second * 6

    # Отрисовка стрелок
    blithand(surface, minute_hand, clock_center, minute_angle+50)
    blithand(surface, sec_hand, clock_center, second_angle)

    # Отображение времени
    time_render = font.render(f"{t:%H:%M:%S}", True, pygame.Color("black"), pygame.Color("white"))
    surface.blit(time_render, (20, 20))

    pygame.display.flip()
    clock.tick(20)
