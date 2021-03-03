# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month_qty = 10

# TODO здесь ваш код
one_month_coast = expenses - educational_grant
month_left = 9
count = 0
total_summ = 0
while count <= month_left:
    one_month_coast = one_month_coast * 1.03
    total_summ += one_month_coast
    count += 1
total_summ += expenses - educational_grant

print('Студенту надо попросить', round(total_summ, 2), 'рублей')
