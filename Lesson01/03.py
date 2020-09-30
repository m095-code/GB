# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input(' Введите число '))
n_str = str(n)
n1 = n_str + n_str
n2 = n_str + n_str + n_str
result = n + int(n1) + int(n2)
# print(n , '+', n1, '+', n2, '=', result)
print(f'{n} + {n1} + {n2} = {result}')
