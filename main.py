import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Задаем размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Задаем название окна
pygame.display.set_caption("Cupid's Archery")

# Задаем иконку окна (замените на путь к вашему изображению иконки)
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Загружаем изображение сердечка (замените на путь к вашему изображению сердечка)
heart_image = pygame.image.load("img/heart.png")
heart_width, heart_height = 100, 87

# Устанавливаем фон
BACKGROUND_COLOR = (255, 228, 196)  # Нежный кремовый цвет

# Создаем переменные для счета
score_hits = 0
score_misses = 0
last_move_time = time.time()

# Устанавливаем начальные координаты сердечка
heart_x = random.randint(0, SCREEN_WIDTH - heart_width)
heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)


# Функция для отображения сердечка
def draw_heart(x, y):
    screen.blit(heart_image, (x, y))


# Функция для отображения счета
font = pygame.font.SysFont(None, 36)


def draw_score(hits, misses):
    score_text = f"Hits: {hits}    Misses: {misses}"
    text = font.render(score_text, True, (0, 0, 0))
    screen.blit(text, (10, 10))


# Основной игровой цикл
running = True
while running:
    # Заливка экрана кремовым цветом
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if heart_x < mouse_x < heart_x + heart_width and heart_y < mouse_y < heart_y + heart_height:
                score_hits += 1
                heart_x = random.randint(0, SCREEN_WIDTH - heart_width)
                heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)
            else:
                score_misses += 1

    # Перемещение сердечка каждые 1.5 секунды
    current_time = time.time()
    if current_time - last_move_time > 5.5:
        heart_x = random.randint(0, SCREEN_WIDTH - heart_width)
        heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)
        last_move_time = current_time

    # Отображение сердечка
    draw_heart(heart_x, heart_y)

    # Отображение счета
    draw_score(score_hits, score_misses)

    # Обновление экрана
    pygame.display.update()

pygame.quit()
