#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
zoo.extend(birds)
print("Добавляем птичек ", zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
del zoo[3]
print('Убираем слона ', zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
lion_cage = zoo.index('lion') + 1 # Номер клетки со львом, в человекопонятном формате
lark_cage = zoo.index('lark') + 1 # Номер клетки со жаворонком, в человекопонятном формате
print("Номер клетки льва: ", lion_cage)
print("Номер клетки жаворонка: ", lark_cage)

print(zoo)