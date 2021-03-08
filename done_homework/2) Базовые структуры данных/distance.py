#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
#TODO здесь в переменные внести расстояния между городами
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = round((((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5), 2)
moscow_paris = round((((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5), 2)
london_moscow = round((((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5), 2)
london_paris = round((((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5), 2)
paris_moscow = round((((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5), 2)
paris_london = round((((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5), 2)

# TODO здесь заполнение словаря
distances = {
    'Moscow': {'London': moscow_london, # расстояние
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


## Комментарии ##

# Решено технически граммотно, но есть логическое противоречие принципу DRY (don't repeat yourself):
# line 21 нет необходимости считать расстояние london_moscow, достаточно написать london_moscow = moscow_london
# Аналогично для 23-24
#
# lines 29 - 30 проблема с выравниванием словаря, так же коммент(#) должен стоять за два пробела от python кода (это может исправить pycharm)


