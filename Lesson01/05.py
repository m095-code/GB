# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


profit = float(input(' Введите выручку компании '))
cost = float(input(' Введите издержку компании '))
if profit > cost:

    finance = profit - cost  # прибыль
    rent_profit = finance / profit  # рентабельность выручки
    print(f'Компания работает в Прибыль Рентабельность выручики составляет {rent_profit}%')
    people = int(input(' Введите Количество сотрудников '))
    finance_in_people = finance / people
    print(f'Прибыль на 1 сотрудника составляет {finance_in_people}')
else:
    print('Бизнес убыточен')
