import pygame  # Импортируем модуль pygame для создания игры
import random  # Импортируем модуль random для генерации случайных чисел
import time  # Импортируем модуль time для работы со временем

# Инициализация Pygame
pygame.init()

# Задаем размеры экрана и игрового поля
INFO_WIDTH = 200  # Ширина дополнительной зоны для опций и информации
SCREEN_WIDTH = 800  # Ширина игрового поля
SCREEN_HEIGHT = 600  # Высота игрового поля
WINDOW_WIDTH = SCREEN_WIDTH + INFO_WIDTH  # Общая ширина окна с учетом зоны информации

# Создаем окно игры с заданными размерами
screen = pygame.display.set_mode((WINDOW_WIDTH, SCREEN_HEIGHT))

# Устанавливаем заголовок окна
pygame.display.set_caption("Cupid's Archery")

# Устанавливаем иконку окна (замените на путь к вашему изображению иконки)
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Загружаем изображение сердечка (замените на путь к вашему изображению сердечка)
heart_image = pygame.image.load("img/heart.png")
heart_width, heart_height = 100, 87  # Размеры сердечка

# Устанавливаем фон
BACKGROUND_COLOR = (255, 228, 196)  # Нежный кремовый цвет

# Загрузка звуков
shoot_sound = pygame.mixer.Sound('sounds/shoot_sound.wav')  # Звук выстрела (замените на путь к вашему файлу звука)
hit_sound = pygame.mixer.Sound('sounds/hit_sound.wav')  # Звук попадания (замените на путь к вашему файлу звука)
miss_sound = pygame.mixer.Sound('sounds/miss_sound.wav')  # Звук промаха (замените на путь к вашему файлу звука)
level_up_sound = pygame.mixer.Sound(
    'sounds/level_up.wav')  # Звук перехода на новый уровень (замените на путь к вашему файлу звука)
win_sound = pygame.mixer.Sound('sounds/win.wav')  # Звук победы (замените на путь к вашему файлу звука)
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')  # Звук поражения (замените на путь к вашему файлу звука)

# Создаем переменные для счета и уровней
score = 0  # Начальный счет
level = 1  # Начальный уровень
last_move_time = time.time()  # Время последнего перемещения сердечка

# Интервалы перемещения сердечка для каждого уровня
move_intervals = [2.5, 2.1, 1.7, 1.45, 1.25]

# Устанавливаем начальные координаты сердечка в случайном месте на игровом поле
heart_x = random.randint(INFO_WIDTH, SCREEN_WIDTH + INFO_WIDTH - heart_width)
heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)


# Функция для отображения сердечка на экране
def draw_heart(x, y):
    screen.blit(heart_image, (x, y))


# Функция для отображения счета и уровня
font = pygame.font.SysFont(None, 36)  # Шрифт для отображения текста


def draw_info(score, level):
    # Отображаем счет
    score_text = f"Счет: {score}"
    text = font.render(score_text, True, (0, 0, 0))
    screen.blit(text, (10, 10))
    # Отображаем уровень
    level_text = f"Уровень: {level}"
    text = font.render(level_text, True, (0, 0, 0))
    screen.blit(text, (10, 50))


# Функция для отображения сообщения
def show_message(message):
    font_large = pygame.font.SysFont(None, 72)  # Крупный шрифт для сообщения
    text = font_large.render(message, True, (255, 0, 0))  # Красный текст
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text, text_rect)  # Отображаем текст в центре экрана
    pygame.display.update()  # Обновляем экран
    pygame.time.delay(2000)  # Задержка на 2 секунды


# Основной игровой цикл
running = True
while running:
    # Заливка экрана кремовым цветом
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, INFO_WIDTH, SCREEN_HEIGHT))  # Зона для информации

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка, если пользователь закрыл окно
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка, если нажата кнопка мыши
            shoot_sound.play()  # Воспроизведение звука выстрела
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем координаты мыши
            if heart_x < mouse_x < heart_x + heart_width and heart_y < mouse_y < heart_y + heart_height:
                hit_sound.play()  # Воспроизведение звука попадания
                score += 1  # Увеличиваем счет
                # Перемещаем сердечко в случайное место
                heart_x = random.randint(INFO_WIDTH, SCREEN_WIDTH + INFO_WIDTH - heart_width)
                heart_y = random.randint(0, SCREEN_HEIGHT - heart_height)
            else:
                miss_sound.play()  # Воспроизведение звука промаха
                score -= 2  # Уменьшаем счет

    # Проверка условий победы и поражения
    if score >= 15 * level:
        if level == 5:  # Проверка, достигнут ли последний уровень
            win_sound.play()  # Звук победы
            show_message("Ты выиграл!")  # Отображение сообщения о победе
            running = False  # Остановка игры
        else:
            level += 1  # Переход на следующий уровень
            level_up_sound.play()  # Звук перехода на новый уровень
            show_message(f"Уровень {level}")  # Отображение текущего уровня
    elif score < -3:
        game_over_sound.play()  # Звук поражения
        show_message("Конец игры")  # Отображение сообщения о поражении
        running = False  # Остановка игры

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
