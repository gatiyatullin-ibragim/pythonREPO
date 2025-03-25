import pygame

def main():
    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PAINT")
    clock = pygame.time.Clock()

    # Настройки рисования
    drawing = False          # Флаг рисования
    mode = "line"            # Режим: 'line', 'rect', 'circle', 'eraser'
    color = (0, 0, 0)        # Цвет по умолчанию (чёрный)
    radius = 5               # Толщина кисти
    start_pos = None         # Начальная позиция для фигур

    # Палитра цветов
    colors = {
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "white": (255, 255, 255)  # Для ластика
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- Обработка клавиш ---
            elif event.type == pygame.KEYDOWN:
                # Смена режима
                if event.key == pygame.K_1:
                    mode = "line"
                elif event.key == pygame.K_2:
                    mode = "rect"
                elif event.key == pygame.K_3:
                    mode = "circle"
                elif event.key == pygame.K_e:
                    mode = "eraser"
                    color = colors["white"]

                # Смена цвета
                elif event.key == pygame.K_r:
                    color = colors["red"]
                elif event.key == pygame.K_g:
                    color = colors["green"]
                elif event.key == pygame.K_b:
                    color = colors["blue"]
                elif event.key == pygame.K_y:
                    color = colors["yellow"]
                elif event.key == pygame.K_k:
                    color = colors["black"]

                # Изменение толщины
                elif event.key == pygame.K_PLUS:
                    radius = min(50, radius + 1)
                elif event.key == pygame.K_MINUS:
                    radius = max(1, radius - 1)

            # --- Обработка мыши ---
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

                    # Рисуем фигуры
                    if mode == "rect":
                        width = end_pos[0] - start_pos[0]
                        height = end_pos[1] - start_pos[1]
                        pygame.draw.rect(screen, color, (start_pos, (width, height)), radius)
                    elif mode == "circle":
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        radius_circle = int((dx**2 + dy**2)**0.5)
                        pygame.draw.circle(screen, color, start_pos, radius_circle, radius)

            elif event.type == pygame.MOUSEMOTION:
                if drawing and mode == "line":
                    current_pos = event.pos
                    pygame.draw.line(screen, color, last_pos, current_pos, radius)
                    last_pos = current_pos

        # --- Отрисовка палитры ---
        y_palette = 550
        pygame.draw.rect(screen, colors["black"], (10, y_palette, 30, 30))
        pygame.draw.rect(screen, colors["red"], (50, y_palette, 30, 30))
        pygame.draw.rect(screen, colors["green"], (90, y_palette, 30, 30))
        pygame.draw.rect(screen, colors["blue"], (130, y_palette, 30, 30))
        pygame.draw.rect(screen, colors["yellow"], (170, y_palette, 30, 30))

        # --- Подпись режима ---
        font = pygame.font.SysFont(None, 24)
        mode_text = font.render(f"Mode: {mode}", True, (0, 0, 0))
        screen.blit(mode_text, (650, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()