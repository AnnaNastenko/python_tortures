#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)  # garden
meadow_set = set(meadow)  # meadow
print("Множество цветов, произрастающих в саду", garden_set, end='\n\n')
print("Множество цветов, произрастающих на лугу", meadow_set, end='\n\n')
# выведите на консоль все виды цветов
# TODO здесь ваш код
all_flowers = garden_set.union(meadow_set)  # все
# all_flowers = garden_set | meadow_set
print("Общее множество", all_flowers, end='\n\n')
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
intersection = garden_set.intersection(meadow_set)  # пересечение
# intersection = garden_set & meadow_set
print("Пересечение", intersection, end='\n\n')
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
garden_diff = garden_set.difference(meadow_set)
# garden_diff = garden_set - meadow_set
print("Растут в саду, но не растут на лугу", garden_diff, end='\n\n')
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
meadow_diff = meadow_set.difference(garden_set)
# meadow_diff = meadow_set - garden_set
print("Растут на лугу, но не растут в саду", meadow_diff, end='\n\n')