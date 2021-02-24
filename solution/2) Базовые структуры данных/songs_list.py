#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],  # 0
    ['Sweetest Perfection', 4.43],  # 1
    ['Personal Jesus', 4.56],  # 2
    ['Halo', 4.9],  # 3
    ['Waiting for the Night', 6.07],  # 4
    ['Enjoy the Silence', 4.20],  # 5
    ['Policy of Truth', 4.76],  # 6
    ['Blue Dress', 4.29],  # 7
    ['Clean', 5.83],  # 8
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код
sum1 = violator_songs_list[3][1] + \
       violator_songs_list[5][1] + \
       violator_songs_list[8][1]  # Halo', 'Enjoy the Silence' и 'Clean', точность до двух знаков после запятой
print('Три песни звучат', round(sum1, 1), 'минут', end='\n\n')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
sum2 = violator_songs_dict['Halo'] + \
       violator_songs_dict['Policy of Truth'] + \
       violator_songs_dict['Blue Dress']  # 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
print('Три песни звучат', sum2, 'минут', end='\n\n')