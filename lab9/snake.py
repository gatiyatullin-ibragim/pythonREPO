import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 720, 480
CELL_SIZE = 10
FPS = 15  # Начальная скорость
FRUIT_LIFETIME = 100  # Через сколько кадров фрукт исчезает

# Цвета
WHITE = pygame.Color('white')
GREEN = pygame.Color('green')
RED = pygame.Color('red')
BLACK = pygame.Color('black')

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def spawn_fruit():
    return [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]

def show_text(text, x, y):
    font = pygame.font.SysFont('Arial', 20)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Функция для перезапуска игры
def reset():
    return [[100, 50], [90, 50], [80, 50]], 'RIGHT', 'RIGHT', spawn_fruit(), 0, 1, FPS, FRUIT_LIFETIME

# Основной игровой цикл
while True:
    snake, direction, next_direction, fruit, score, level, speed, fruit_timer = reset()

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    next_direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    next_direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    next_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    next_direction = 'RIGHT'

        # Двигаем змейку
        direction = next_direction
        head = snake[0][:]
        if direction == 'UP':
            head[1] -= CELL_SIZE
        elif direction == 'DOWN':
            head[1] += CELL_SIZE
        elif direction == 'LEFT':
            head[0] -= CELL_SIZE
        elif direction == 'RIGHT':
            head[0] += CELL_SIZE

        # Проверка столкновения с границами или телом
        if head in snake or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            break  # Завершаем цикл игры

        # Проверка поедания фрукта
        eat_fruit = head == fruit
        if eat_fruit:
            score += random.randint(1,10)
            fruit = spawn_fruit()
            fruit_timer = FRUIT_LIFETIME  # Сбрасываем таймер
            if score % 5 == 0:  # Каждые 5 очков увеличиваем уровень
                level += 1
                speed += 1
        else:
            snake.pop()  # Если фрукт не съеден, убираем хвост

        # Логика исчезновения еды
        fruit_timer -= 1
        if fruit_timer <= 0:
            fruit = spawn_fruit()
            fruit_timer = FRUIT_LIFETIME  # Сброс таймера
            snake.pop()  # Удаляем хвост при исчезновении еды

        snake.insert(0, head)  # Добавляем новую голову змейки

        # Отрисовка
        screen.fill(WHITE)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(fruit[0], fruit[1], CELL_SIZE, CELL_SIZE))

        show_text(f'Score: {score}', 10, 10)
        show_text(f'Level: {level}', WIDTH - 100, 10)

        pygame.display.update()
        clock.tick(speed)

    # Экран поражения перед перезапуском
    screen.fill(BLACK)
    font = pygame.font.SysFont('Arial', 40)
    text_surface = font.render(f'Game Over! Score: {score}', True, RED)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)
