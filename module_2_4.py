numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]    #

primes = []    # Список простых чисел
not_primes = []    # Список не простых чисел

is_prime = True    # Флаг простого числа

for i in numbers:
    if i == 1:    # 1 не является простым, а также и не простым, поэтому пропускаем
        continue

    elif i == 2:    # 2 является простым числом, поэтому сразу загоняем в список простых чисел
        primes.append(i)
        continue

    for j in range(2, i):    # Во втором цикле определяем простое число, перебирая возможные делители

        if i % j == 0:    # При появлении первого делителя, отмечаем флаг простого числа и останавливаем цикл
            is_prime = False
            break

        else: is_prime = True    # Если j не является делителем, то отмечаем флаг простого числа и продолжаем поиск

    if is_prime:    # В зависимости от флага распределяем числа по спискам
        primes.append(i)
    else:
        not_primes.append(i)

print('Исходный список: ', numbers)
print('Простые числа: ', primes)
print('Не простые числа: ',not_primes)