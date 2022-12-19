#Параметры sep и end
print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')
###########################
razdelitel = input()
string_1 = input()
string_2 = input()
string_3 = input()

print(string_1, string_2, string_3, sep = razdelitel)

###########################

num = int(input())
hour = num // 60
min = num % 60
print(num, 'мин - это', hour, 'час', min, 'минут.')

###########################
num =int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
###########################
num =int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10

print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

# Входные данные

# Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.

# Выходные данные

# Выведите число секунд между этими моментами времени.

#Решение нуба
start_hours, start_minuts, start_seconds = int(input()), int(input()), int(input())
start_hours_in_sec = start_hours * 3600
start_minuts_in_sec = start_minuts * 60
start_result = start_hours_in_sec + start_minuts_in_sec + start_seconds

finish_hours, finish_minuts, finish_seconds = int(input()), int(input()), int(input())
finish_hours_in_sec = finish_hours * 3600
finish_minuts_in_sec = finish_minuts * 60
finish_result = finish_hours_in_sec + finish_minuts_in_sec + finish_seconds
print(finish_result - start_result)

# Нормальное решение
time1 = int(input()) * 3600 + int(input()) * 60 + int(input())
time2 = int(input()) * 3600 + int(input()) * 60 + int(input())
print(time2 - time1)

# Входные данные

# Во входных данных записаны три целых числа a, b и c, каждое в отдельной строке (1 ≤ a, b, c ≤ 10).

# Выходные данные

# Выведите максимальное значение выражения, которое можно получить.
a, b, c = int(input()), int(input()), int(input())
s1 = a + b + c
s2 = a * b * c
s3 = a + b * c
s4 = (a + b) * c
s5 = a * b + c
s6 = a * (b + c)
print(max(s1, s2, s3, s4, s5, s6))