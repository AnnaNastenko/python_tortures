#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
# Итоговое значение


# TODO здесь в переменные внести расстояния между городами
# HINT чтобы корректно прошел 4ый тест, в задаче не следует использовать round!

m = sites['Moscow']
l = sites['London']
p = sites['Paris']

# Moscow_to_destination
# moscow_london = london_moscow = round(((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** .5, 2)
# moscow_paris = paris_moscow = round(((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** .5, 2)
moscow_london = london_moscow = ((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** .5
moscow_paris = paris_moscow = ((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** .5

# London to_destination
# london_to_moscow - ready!
# london_paris = paris_london = round(((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** .5, 2)
london_paris = paris_london = ((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** .5

# Moscow_to_destination - ready!

# TODO здесь заполнение словаря
distances = {
    'Moscow': {'London': moscow_london,
               'Paris': moscow_paris
               },
    'London': {
        'Moscow': london_moscow,
        'Paris': london_paris
    },
    'Paris': {
        'Moscow': paris_moscow,
        'London': paris_london
    }
}

pprint(distances)