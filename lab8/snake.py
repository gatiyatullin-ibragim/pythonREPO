import pygame
import time
import random
import sys

pygame.init()

RES = WIDTH, HEIGHT = 720, 480
bg = pygame.display.set_mode(RES)
pygame.display.set_caption("Snake")
FPS = pygame.time.Clock()
bg.fill(pygame.Color('white'))

snake_speed = 15
snake_pos = [100, 50]

snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_pos = [random.randrange(1, (WIDTH // 10)) * 10,
             random.randrange(1, (HEIGHT // 10)) * 10]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    score_rect = score_surface.get_rect(topleft=(10, 10))
    bg.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Score: {score}', True, 'red')
    game_over_rect = game_over_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    bg.fill('black')
    bg.blit(game_over_surface, game_over_rect)
    pygame.display.update()

    time.sleep(2)
    pygame.quit()
    sys.exit()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                     random.randrange(1, (HEIGHT // 10)) * 10]
    fruit_spawn = True

    bg.fill(pygame.Color('white'))

    for pos in snake_body:
        pygame.draw.rect(bg, pygame.Color('green'), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(bg, pygame.Color('red'), pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, 'black', 'Arial', 20)

    pygame.display.update()
    FPS.tick(snake_speed)
