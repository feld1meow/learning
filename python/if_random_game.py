# Программа игра. Компьютер загадывает случайное целое число от 1 до 4
# пользователь пытается его угадать
# Программа запрашивает число ТОЛЬКО один раз

import random

value = random.randint(1, 4)
user_value = int(input('Я загадал случайное целое число от 1 до 4. Попробуйте угадать. У вас только один шанс:'))
if user_value == value:
    print('На этот раз вам повезло...')
elif user_value > value:
    print('Ваше число больше загаданного')
else:
    print('Ваше число меньше загаданного')