salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0
month = months  # сохраняю значение переменной в другой
while months != 0:

    need_money += spend
    spend = spend * (1 + increase)
    months -= 1

need_money -= salary * month  # количество денег, чтобы прожить 10 месяцев
print(round(need_money))
