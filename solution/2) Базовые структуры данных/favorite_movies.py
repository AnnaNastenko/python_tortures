#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
first = my_favorite_movies[:10]  # первый
print(first)

last = my_favorite_movies[-15:]  # последний
print(last)

second = my_favorite_movies[12:25]  # второй
print(second)

penult = my_favorite_movies[-22:-17]  # второй с конца
print(penult)