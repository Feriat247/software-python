money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0

while money_capital >= 0:
    money_capital += salary - spend
    spend *= (1 + increase)
    month += 1
    if money_capital <= 0:
        print(f"Финансовая подушка закончится на {month} месяце и будет равной: {money_capital:.2f}")
        month -= 1



print("Количество месяцев, которое можно протянуть без долгов:", month)
