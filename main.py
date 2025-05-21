import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Игровой объект
square = pygame.Rect(300, 200, 40, 40)
speed = 5

# Главный цикл игры
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: square.x -= speed
    if keys[pygame.K_RIGHT]: square.x += speed
    if keys[pygame.K_UP]: square.y -= speed
    if keys[pygame.K_DOWN]: square.y += speed

    pygame.draw.rect(screen, BLUE, square)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
