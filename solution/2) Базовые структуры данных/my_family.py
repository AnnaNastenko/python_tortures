#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Andrew',
             'Hanna',
             'Tiry']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 189],
    [my_family[1], 156],
    [my_family[2], 55]
]

# TODO:

# Запишите в переменную father_height рост отца и выведите на консоль рост отца в формате
#   Рост отца - ХХ см
father_height = my_family_height[0][1]  # Рост отца
print('Рост отца -', my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
family_height = my_family_height[0][1] + my_family_height[1][1] + \
                my_family_height[2][1]  # Рост моей семьи
print('Общий рост моей семьи', family_height, 'см')
