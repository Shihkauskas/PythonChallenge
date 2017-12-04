# -*- coding:utf -8 -*-

try:
    number = int(input('Введите число: '))
    if number % 3 == 0:
        print(True)
    else:
        print(False)
except:
    print('Некорректный ввод')
