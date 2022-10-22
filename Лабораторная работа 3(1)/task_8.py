money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0

while money_capital >= 0:

    money_capital += (salary - spend)
    spend *= (1 + increase)
    month += 1
    if money_capital < 0:
        month -= 1  # Т.к. если значение меньше ноля, значит на этот месяц уже не хватает денег

print(month)
