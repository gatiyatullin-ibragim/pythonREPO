import pygame

def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PAINT")
    clock = pygame.time.Clock()

    # Настройки рисования
    drawing = False
    mode = "line"
    color = (0, 0, 0)
    radius = 5
    start_pos = None
    end_pos = None  # Инициализируем

    # Палитра цветов
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Смена режима
                if event.key == pygame.K_1:
                    mode = "line"
                elif event.key == pygame.K_2:
                    mode = "rect"
                elif event.key == pygame.K_3:
                    mode = "circle"
                elif event.key == pygame.K_4:
                    mode = "right triangle"
                elif event.key == pygame.K_5:
                    mode = "square"
                elif event.key == pygame.K_6:
                    mode = "equilateral triangle"
                elif event.key == pygame.K_7:
                    mode = "rhombus"
                elif event.key == pygame.K_e:
                    mode = "eraser"
                    color = 'white'

                # Смена цвета
                elif event.key == pygame.K_r:
                    color = 'red'
                elif event.key == pygame.K_g:
                    color = 'green'
                elif event.key == pygame.K_b:
                    color = 'blue'
                elif event.key == pygame.K_y:
                    color = 'yellow'
                elif event.key == pygame.K_k:
                    color = 'black'

                # Изменение толщины
                elif event.key == pygame.K_PLUS:
                    radius = min(50, radius + 1)
                elif event.key == pygame.K_MINUS:
                    radius = max(1, radius - 1)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка
                    drawing = True
                    start_pos = event.pos
                    if mode == "line":
                        last_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    end_pos = event.pos

                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])

                    center_x = (start_pos[0] + end_pos[0]) // 2
                    center_y = (start_pos[1] + end_pos[1]) // 2

                    if mode == "rect":
                        pygame.draw.rect(screen, color, (*start_pos, width, height), radius)

                    elif mode == "circle":
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        radius_circle = int((dx**2 + dy**2)**0.5)
                        pygame.draw.circle(screen, color, start_pos, radius_circle, radius)

                    elif mode == "right triangle":
                        points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
                        pygame.draw.polygon(screen, color, points, radius)

                    elif mode == "square":
                        side = min(width, height)
                        pygame.draw.rect(screen, color, (*start_pos, side, side), radius)

                    elif mode == "equilateral triangle":
                        h = (3**0.5 / 2) * width
                        p1 = (start_pos[0], start_pos[1] - h // 2)
                        p2 = (start_pos[0] - width // 2, start_pos[1] + h // 2)
                        p3 = (start_pos[0] + width // 2, start_pos[1] + h // 2)
                        pygame.draw.polygon(screen, color, [p1, p2, p3], radius)

                    elif mode == "rhombus":
                        up = (center_x, center_y - height // 2)
                        right = (center_x + width // 2, center_y)
                        down = (center_x, center_y + height // 2)
                        left = (center_x - width // 2, center_y)
                        pygame.draw.polygon(screen, color, [up, right, down, left], radius)

            elif event.type == pygame.MOUSEMOTION:
                if drawing and mode == "line":
                    current_pos = event.pos
                    pygame.draw.line(screen, color, last_pos, current_pos, radius)
                    last_pos = current_pos

        #Отрисовка палитры
        y_palette = 550
        pygame.draw.rect(screen, 'black', (10, y_palette, 30, 30))
        pygame.draw.rect(screen, 'red', (50, y_palette, 30, 30))
        pygame.draw.rect(screen, 'green', (90, y_palette, 30, 30))
        pygame.draw.rect(screen, 'blue', (130, y_palette, 30, 30))
        pygame.draw.rect(screen, 'yellow', (170, y_palette, 30, 30))

        #Подпись режима
        font = pygame.font.SysFont(None, 24)
        mode_text = font.render(f"Mode: {mode}", True, (0, 0, 0))
        screen.blit(mode_text, (650, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
