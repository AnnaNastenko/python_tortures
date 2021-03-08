#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['me', 'Andrew', 'Tiri']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
# ['имя', рост],
['me', 156],
['Andrew', 192],
['Tiri', 45]
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
father_height = my_family_height[1]
print('Andrew height is: ', father_height[1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
family_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('My family height is: ', family_height)


## Комментарии ##
# lines 11-16 выровнять лист при помощи pycharm - чтобы он не подчеркивал и было красиво