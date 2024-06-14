import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Задаем размеры экрана и игрового поля
INFO_WIDTH = 200  # Ширина дополнительной зоны для опций и информации
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_WIDTH = SCREEN_WIDTH + INFO_WIDTH

screen = pygame.display.set_mode((WINDOW_WIDTH, SCREEN_HEIGHT))

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

# Загрузка звуков
shoot_sound = pygame.mixer.Sound('sounds/shoot_sound.wav')  # замените на путь к вашему файлу звука выстрела
hit_sound = pygame.mixer.Sound('sounds/hit_sound.wav')  # замените на путь к вашему файлу звука попадания
miss_sound = pygame.mixer.Sound('sounds/miss_sound.wav')  # замените на путь к вашему файлу звука промаха
level_up_sound = pygame.mixer.Sound(
    'sounds/level_up.wav')  # замените на путь к вашему файлу звука перехода на новый уровень
win_sound = pygame.mixer.Sound('sounds/win.wav')  # замените на путь к вашему файлу звука победы
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')  # замените на путь к вашему файлу звука поражения

# Создаем переменные для счета и уровней
score = 0
level = 1
last_move_time = time.time()

# Интервалы перемещения сердечка для каждого уровня
move_intervals = [2.5, 2.1, 1.7, 1.45, 1.25]

# Устанавливаем начальные координаты сердечка
heart_x = random.randint(INFO_WIDTH, SCREEN_WIDTH + INFO_WIDTH - heart_width)
heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)


# Функция для отображения сердечка
def draw_heart(x, y):
    screen.blit(heart_image, (x, y))


# Функция для отображения счета и уровня
font = pygame.font.SysFont(None, 36)


def draw_info(score, level):
    score_text = f"Счет: {score}"
    text = font.render(score_text, True, (0, 0, 0))
    screen.blit(text, (10, 10))
    level_text = f"Уровень: {level}"
    text = font.render(level_text, True, (0, 0, 0))
    screen.blit(text, (10, 50))


# Функция для отображения сообщения
def show_message(message):
    font_large = pygame.font.SysFont(None, 72)
    text = font_large.render(message, True, (255, 0, 0))
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)


# Основной игровой цикл
running = True
while running:
    # Заливка экрана кремовым цветом
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, INFO_WIDTH, SCREEN_HEIGHT))  # Зона для информации

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot_sound.play()  # воспроизведение звука выстрела
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if heart_x < mouse_x < heart_x + heart_width and heart_y < mouse_y < heart_y + heart_height:
                hit_sound.play()  # воспроизведение звука попадания
                score += 1
                heart_x = random.randint(INFO_WIDTH, SCREEN_WIDTH + INFO_WIDTH - heart_width)
                heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)
            else:
                miss_sound.play()  # воспроизведение звука промаха
                score -= 2

    # Проверка условий победы и поражения
    if score >= 15 * level:
        if level == 5:
            win_sound.play()  # звук победы
            show_message("Ты выиграл!")
            running = False
        else:
            level += 1
            level_up_sound.play()  # звук перехода на новый уровень
            show_message(f"Уровень {level}")
    elif score < -3:
        game_over_sound.play()  # звук поражения
        show_message("Конец игры")
        running = False

    # Перемещение сердечка в зависимости от уровня
    current_time = time.time()
    if current_time - last_move_time > move_intervals[level - 1]:
        heart_x = random.randint(INFO_WIDTH, SCREEN_WIDTH + INFO_WIDTH - heart_width)
        heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)
        last_move_time = current_time

    # Отображение сердечка
    draw_heart(heart_x, heart_y)

    # Отображение информации
    draw_info(score, level)

    # Обновление экрана
    pygame.display.update()

pygame.quit()
