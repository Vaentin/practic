def sum_numbers_from_range(start, finish):
    # Технически можно менять start
    # Но входные аргументы нужно оставлять в исходном значении
    # Это сделает код проще для анализа
    i = start
    sum = 0  # Инициализация суммы
    while i <= finish:  # Двигаемся до конца диапазона
        sum = sum + i   # Считаем сумму для каждого числа
        i = i + 1       # Переходим к следующему числу в диапазоне
    # Возвращаем получившийся результат
    return sum

print(sum_numbers_from_range(5, 7))


# 1 цикл

i = 5
sum = 0
# step 1
while 5 <= 7
sum = 0 + 5
i = 5 + 1

# result step 1
sum = 5
i = 6

# step 2 
while 6 <= 7
sum = 5 + 6
i = 6 + 1

# result step 2
sum = 11
i = 7

# step 3 
while 7 <= 7
sum = 11 + 7
i = 7 + 1

# result step 2
sum = 18
i = 8

# step 4 
while 8 <= 7

return sum (18)
