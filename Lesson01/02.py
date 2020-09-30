# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


sec = int(input('Введите число в секундах : '))
minute = 0
hour = 0
while sec >= 60:
    minute = sec // 60
    sec = sec % 60
    while minute >= 60:
        hour = minute // 60
        minute = minute % 60

print(int(hour), ':', int(minute), ':', int(sec))
print(f'{hour:>02}:{minute:>02}:{sec:>02}')
