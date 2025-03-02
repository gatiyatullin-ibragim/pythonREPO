import pygame
import sys
import os
from datetime import datetime
import math

# Константы экрана
RES = WIDTH, HEIGHT = 600, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 210
radius_list = {'sec' : RADIUS - 10, 'min' : RADIUS - 55, 'hour' : RADIUS - 100, 'digit' : RADIUS - 30}

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# Углы для часов и минут
clock12 = dict(zip(range(12), range(0, 360, 30)))
clock60 = dict(zip(range(60), range(0, 360, 6)))

# Загрузка изображений
bg = pygame.image.load("mickey-mouse-seeklogo.png")
hour_hand = pygame.image.load("прямая рука.png")


# Масштабирование
bg = pygame.transform.scale(bg, (RADIUS * 2, RADIUS * 2))
hour_hand = pygame.transform.scale(hour_hand, (160, 130))   # Часовая стрелка
minute_hand = pygame.transform.scale(hour_hand, (160, 210)) # Минутная стрелка
second_hand = pygame.transform.scale(hour_hand, (160, 200)) # Секундная стрелка

# Шрифт для времени
font = pygame.font.SysFont('Verdana', 30)


def get_clock_pos(clock_dict, clock_hand, key):
    """Возвращает позицию часовой стрелки"""
    
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi /2)
    return x,y
    


def blit_hand(surf, image, center, angle, pivot):
    """Поворачивает стрелку и центрирует её относительно `center`"""
    rotated_image = pygame.transform.rotate(image, -angle)
    pivot_offset = pygame.math.Vector2(pivot).rotate(angle)
    rotated_rect = rotated_image.get_rect(center=(center[0] + pivot_offset.x, center[1] + pivot_offset.y))
    surf.blit(rotated_image, rotated_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    surface.fill(pygame.Color('white'))

    # Центр часов
    clock_center = (H_WIDTH, H_HEIGHT)

    # Время
    t = datetime.now()
    hour_angle = (t.hour % 12) * 30 + t.minute * 0.5  # 30° на час + 0.5° за каждую минуту
    minute_angle = t.minute * 6  # 6° за каждую минуту
    second_angle = t.second * 6  # 6° за каждую секунду
    
    
    pygame.draw.circle(surface, pygame.Color('white'), (H_WIDTH, H_HEIGHT), RADIUS)
    
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('black'), get_clock_pos(clock60, digit, 'digit'), radius)
        
        
        if digit % 15 == 0:
            text_surf = font.render(str(digit // 5 if digit else 12), True, pygame.Color('white'))
            text_rect = font.render(str(digit // 5 if digit else 12), True, pygame.Color('white'))
            text_rect = text_surf.get_rect(center=get_clock_pos(clock60, digit, 'digit'))
            surface.blit(text_surf, text_rect)

    # Отрисовка циферблата
    pygame.draw.circle(surface, pygame.Color('black'), clock_center, RADIUS, 6)
    pygame.draw.circle(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), 12)
    
    # Отрисовка циферблата с изображением Микки Мауса
    surface.blit(bg, (H_WIDTH - RADIUS, H_HEIGHT - RADIUS))  
    pygame.draw.circle(surface, pygame.Color('black'), clock_center, RADIUS, 6)  # Граница круга
    pygame.draw.circle(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), 12)  # Центральный узел

    
    # Рисуем стрелки
    blit_hand(surface, hour_hand, clock_center, hour_angle, (0, -65))  # Pivot point for hour hand
    blit_hand(surface, minute_hand, clock_center, minute_angle, (0, -80))  # Pivot point for minute hand
    blit_hand(surface, second_hand, clock_center, second_angle, (0, -105))  # Pivot point for second hand

    # Отрисовка цифрового времени
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('black'), pygame.Color('white'))
    surface.blit(time_render, (0, 0))

    pygame.display.flip()
    clock.tick(20)
