age = 20
name = 'Timofei'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Возраст {} -- {} лет.'.format(name, age))  # можно и не писать цифры
print('Почему {0} забавляется с этим Python?'.format(name))
print('Почему {} забавляется с этим Python?'.format(name))  # можно и не писать цифры


# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))
# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^22}'.format('hello'))
# по ключевым словам:
print('{name} написал {book}'.format(name='Timofei', book='NIHUYA'))

