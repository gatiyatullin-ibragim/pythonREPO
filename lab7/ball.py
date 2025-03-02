import pygame
import random

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движение круга")

# Цвета
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Параметры круга
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_radius = 50
speed = 20
circle_color = blue  # Начальный цвет круга

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))




running = True
while running:
    pygame.time.delay(30)

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление клавишами
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and circle_y - circle_radius > 0:
        circle_y -= speed
        hit_y = False
    if keys[pygame.K_DOWN] and circle_y + circle_radius < HEIGHT:
        circle_y += speed
        hit_y = False
    if keys[pygame.K_LEFT] and circle_x - circle_radius > 0:
        circle_x -= speed
        hit_x = False
    if keys[pygame.K_RIGHT] and circle_x + circle_radius < WIDTH:
        circle_x += speed
        hit_x = False

    # Проверка на столкновение с границами
    if (circle_x - circle_radius <= 0 or circle_x + circle_radius >= WIDTH) and not hit_x:
        circle_color = random_color()
        hit_x = True
    if (circle_y - circle_radius <= 0 or circle_y + circle_radius >= HEIGHT) and not hit_y:
        circle_color = random_color()
        hit_y = True

    # Отрисовка экрана
    screen.fill(green)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    pygame.display.flip()

pygame.quit()
