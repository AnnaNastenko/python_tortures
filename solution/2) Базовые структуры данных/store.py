#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб', end='\n\n')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# TODO здесь ваш код
# Столы
tc = store[goods['Стол']]
tables_qty = tc[0]['quantity'] + tc[1]['quantity']
tables_cost = tc[0]['quantity'] * tc[0]['price'] + tc[1]['quantity'] * tc[1]['price']
print('Стол -', tables_qty, 'шт, стоимость', tables_cost, 'руб', end='\n\n')

# Диваны
sf = store[goods['Диван']]
sofas_qty = sf[0]['quantity'] + sf[1]['quantity']
sofas_cost = sf[0]['quantity'] * sf[0]['price'] + sf[1]['quantity'] * sf[1]['price']
print('Диван -', sofas_qty, 'шт, стоимость', sofas_cost, 'руб', end='\n\n')

# Стулья
ch = store[goods['Стул']]
chairs_qty = ch[0]['quantity'] + ch[1]['quantity'] + ch[2]['quantity']
chairs_cost = ch[0]['quantity'] * ch[0]['price'] + \
               ch[1]['quantity'] * ch[1]['price'] + \
               ch[2]['quantity'] * ch[2]['price']
print('Стул -', chairs_qty, 'шт, стоимость', chairs_cost, 'руб', end='\n\n')







