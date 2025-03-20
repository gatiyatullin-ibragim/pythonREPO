import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
res = WIDTH, HEIGHT = 400, 600
speed = 10
clock = pygame.time.Clock()

display = pygame.display.set_mode(res)
pygame.display.set_caption('racer')

try:
    bg = pygame.image.load("doroga.jpg").convert()
except pygame.error:
    print("Ошибка: изображение 'doroga.jpg' не найдено!")
    sys.exit()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


font = pygame.font.SysFont('Verdana', 30)

C = Coin()
P1 = Player()
E1 = Enemy()

cnt = 0  

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.move()
    E1.move()
    C.move()

    display.blit(bg, (0, 0))

    if P1.rect.colliderect(C.rect):
        cnt += 1 
        C.reset_position()

    if P1.rect.colliderect(E1.rect):
        print("Game Over")
        pygame.quit()
        sys.exit()

    P1.draw(display)
    E1.draw(display)
    C.draw(display)

    counter = font.render(str(cnt), True, (255, 255, 255))
    display.blit(counter, (WIDTH - 50, 10))

    pygame.display.update()
    clock.tick(FPS)
