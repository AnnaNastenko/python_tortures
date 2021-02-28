# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

# TODO здесь ваш код

days_in_each_month = {1: [31, 'January'],
                      2: [28, 'February'],
                      3: [31, 'March'],
                      4: [30, 'April'],
                      5: [31, 'May'],
                      6: [30, 'June'],
                      7: [31, 'Jule'],
                      8: [31, 'August'],
                      9: [30, 'September'],
                      10: [31, 'October'],
                      11: [30, 'November'],
                      12: [31, 'December']
                      }

print(f'''Вы ввели {month} "{days_in_each_month[month][1]}, в нем"''', end=' ')


if month in days_in_each_month:
    dm = days_in_each_month[month][0]
    print(dm)
else:
    print('Введен некорректный номер месяца')