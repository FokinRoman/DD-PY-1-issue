salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
money = 0

while months != 0:

    money += spend
    spend = spend * (1 + increase)
    months -= 1

money -= salary * 10

need_money = round(money)  # количество денег, чтобы прожить 10 месяцев

print(round(need_money))
