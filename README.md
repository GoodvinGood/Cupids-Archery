# Cupid's Archery

Cupid's Archery - это увлекательная игра, в которой вы должны стрелять из лука по сердечкам, как настоящий Купидон. Ваша задача - набирать очки и переходить на новые уровни, пока не достигнете победы.

## Установка

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 или выше).
2. Установите Pygame, если он еще не установлен:
    ```bash
    pip install pygame
    ```
3. Склонируйте репозиторий игры на ваш компьютер:
    ```bash
    git clone https://github.com/ваш_профиль/Cupids-Archery.git
    ```
4. Перейдите в директорию с игрой:
    ```bash
    cd Cupids-Archery
    ```

## Запуск игры

Для запуска игры выполните следующую команду:
```bash
python main.py
Как играть
При каждом попадании в сердечко вам начисляется 1 очко.
При промахе из счета вычитается 2 очка.
Игра начинается с первого уровня.
Каждые 15 очков вы переходите на новый уровень.
На каждом уровне сердечко перемещается с разной скоростью:
Уровень 1: сердечко перемещается каждые 2.5 секунды.
Уровень 2: сердечко перемещается каждые 2.1 секунды.
Уровень 3: сердечко перемещается каждые 1.7 секунды.
Уровень 4: сердечко перемещается каждые 1.45 секунды.
Уровень 5: сердечко перемещается каждые 1.25 секунды.
Если вы достигли 5 уровня и набрали 15 очков, вы победили.
Если ваш счет опускается ниже -3 очков, игра заканчивается.
Звуковые эффекты
В игре присутствуют следующие звуковые эффекты:

Звук выстрела при нажатии на кнопку мыши.
Звук попадания при попадании в сердечко.
Звук промаха при промахе.
Звук перехода на новый уровень.
Звук победы.
Звук поражения.
Зависимости
Python 3.6+
Pygame
