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



# Ввод данных в строку
n, a, b = map(int,input().split()) 
S = (n * (a * b)) * 2
print(S)




#Однажды, посетив магазин канцелярских товаров,
#Вася купил X карандашей, Y ручек и Z фломастеров.
#Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера.
#Также известно, что стоимость карандаша составляет 3 рубля.
#Требуется определить общую стоимость покупки.
X, Y, Z = map(int,input().split())
print(X * 3 + Y * 5 + Z * 12)

#################################
separ = str(input())
print(1, 2, 3, 4, 5, sep = separ)
#################################
print(str(input()), end = ' - Сказала она!')
#################################
n = input()
nn = str(n) + str(n)
nnn = str(n) + str(n)+ str(n)
result = n + int(nn) + int(nnn)
print(result)

# Программе поступает на вход одно целое положительное число,
# ваша задача вывести его последнюю цифру
print(int(input()) % 10)

# Дано целое положительное число,
# аша задача вывести разряд сотен этого числа
print((int(input()) % 1000) // 100)

# Дано целое положительное трехзначное число,
# ваша задача найти сумму разрядов этого числа
n = int(input())
print((n // 100) + (n % 100) // 10 + n % 10)

#  У Олега в банке есть n евро.
#  Он хочет снять всю сумму наличными. Номиналы еврокупюр равны 1, 5, 10, 20, 100.
#  Какое минимальное число купюр должен получить Олег после того, как снимет все деньги?
#  На вход программе поступает одно положительные целое число n.

n = 13
a = n // 100
b = n % 100 // 20
c = n % 100 % 20 // 10
d = n % 100 % 20 % 10 // 5
e = n % 100 % 20 % 10 % 5
print(a, b, c, d, e )

# Более простое решение
n = int(input())
n1 = n // 100 # купюры по 100
n2 = n % 100 // 20 # купюры по 20, после выдачи купюр по 100
n3 = n % 20 // 10 # купюры по 10, после выдачи купюр по 20
n4 = n % 10 // 5 # купюры по 5, после выдачи купюр по 10
n5 = n % 5 // 1 # купюры по 1, после выдачи купюр по 5
print(n1 + n2 +n3 + n4 + n5) # скалдываем кол-во купюр


# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутка

n = int(input())
nday = n % 1440
nhours = nday // 60
nminuts = nday % 60
print(nhours, nminuts)

#Другое решение
n = int(input())
print(n // 60 % 24, n % 60)

#Дано целое число n. Выведите следующее за ним четное число
n = int(input())
print(n + 2 - (n % 2))


# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне от 0 до 23,
# потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
n = int(input())
nhours =  (n//3600)%24
n = n%3600
nminuts = n//60
seconds = n % 60
print(nhours,':', nminuts//10, nminuts%10, ':', seconds//10, seconds%10, sep='')

# 
print(int(input()) > 0) #Выод положительного числа
print(int(input()) % 2 == 0) # Четное число
print(int(input()) % 6 == 0) # кратно 6
print(int(input()) %9 != 0) # не делится на 9
print(int(input()) %10 == 2) # Последняя цифра 2

# На вход два числа в строку, оба должны делиться на 7
a, b = map(int,input().split())
print(a % 7 == 0 and b % 7 == 0)

# Программа должна вывести True,
# если введенное значение принадлежит интервалу
# от 5 не включительно до 19 включительно
# в противном случае - False.
print(5 < int(input()) <= 19)

# Программа должна вывести True,
# если хотя бы одно слово равно слову "awesome".
a, b = input(), input()
print(a == 'awesome' or  b == 'awesome')

# Более интересное решение 
a, b, c = input(), input(), 'awesome'
print(a == c or b == c)

# Необходимо вывести True,
# если данные стороны образуют равнобедренный треугольник

a, b, c = map(int,input().split())
print(a == b or b == c or c == a)

# Программа должна вывести True,
# если данное число является двузначным
print(len(input())!= 2)

# Более верное ршение
print(9 < int(input()) < 100)

# Необходимо вывести True, 
# если данные стороны образуют прямоугольный треугольник
a, b, c = map(int,input().split())
g = max(a, b, c)
k1 = min(a, b, c)
k2 = (a+b+c)-g-k1

print(g**2 == k1**2 + k2**2)

#Входные данные
# Программе на вход поступает натуральное число N (N ≤ 109) – длина перевязи в миллиметрах.

# Выходные данные
# Выведите на экран минимальное количество луидоров, которые Портос должен отдать за работу.
import math
print(math.ceil((int(input()))/10))

# После вечеринки компания из N человек хочет добраться домой с помощью такси. Максимальное количество человек,
# которое может уместиться в машину равно 4. Сколько машин придется вызвать ребятам, чтобы все могли уехать?

# Программа получает на вход положительное целое число N - количество человек в компании.
import math
print(math.ceil((int(input()))/4))

#Выведите на экран одно целое число – минимальное количество банок краски, 
# необходимых для покраски стен в офисе. Одной банки хватает на 16 м**2
from math import ceil 
L, W, H = map(int,input().split())
print(ceil((L*H + W*H)*2 /16))

# СТРОКИ

a = 'Я стану крутым программистом!'
print(a,a,a, sep = '\n')
#или
print("""Я стану крутым программистом!
Я стану крутым программистом!
Я стану крутым программистом!""")
#777 букв W
print("W"*777)

# Принять две строчки и напечатать так же
print(input(),input(), sep = '\n')
# Поменять местами строчки
a, b, c = input(),input(),input()
print(c, b, a, sep = '\n')

#Программа принимает на вход три символа через пробел в одну строку.
#Необходимо вывести код каждого символа при помощи функции ord в определенном формате.
a, b, c = map(str,input().split())
print("Simvol code ", a, " is ", ord(a),'.', sep = '')
print("Simvol code ", b, " is ", ord(b),'.', sep = '')
print("Simvol code ", c, " is ", ord(c),'.', sep = '')

#более верное решение используя конкатенацию (+)
a,s,d=map(str,input().split())
print('Simvol code',a,'is',str(ord(a))+'.')
print('Simvol code',s,'is',str(ord(s))+'.')
print('Simvol code',d,'is',str(ord(d))+'.')

# ******** Методы строк ********
print(input().upper())     # все заглавные
print(input().lower())     # все строчные
print(input().swapcase())  # все заглавные буквы преобразованы в строчные, строчные – в заглавные
print(input().find('a'))   # индекс первой а
print(input().rfind('a'))  # индекс первой а с конца
print(input().replace(' ',',')) #пробел на запятую
print(input().replace('w','').replace('z','')) # w и z на ничто) удалили из строки

#сравни строки независимо от регистра
s = input()
word = input()
print(s.upper() == word.upper())

#первые последние 3 буквы заглавные в середине маленькие
word = input()
print(word.upper()[:3] + word.lower()[3:-3] + word.upper()[-3:])

#удаляет все гласные буквы,
#перед каждой согласной буквой ставит символ ".",
#все прописные согласные буквы заменяет на строчные.
s = input().lower()
s = s.replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')
s ='.'.join(s)
print('.'+ s)

# Сколько слов в строке (.split(sep=по умол пробел, maxsplit=-1))
print(len(input().split()))

# Напишите программу, которая проверяет, 
# чтобы введенная фраза s одновременно начиналась со строки prefix и заканчивалась строкой postfix
s = input()
prefix = input()
postfix = input()
print(s.startswith(prefix) and s.endswith(postfix))

# Добавляет строку из одного знаечения 
print(input().ljust(15, '-'))  #справа input----
print(input().rjust(10, '!'))  #слева !!!!input
print(input().center(15, '_')) #по бокам __center__
print(input().zfill(10))       #нули 0000input

# Убрать символы
print(input().strip("-_!?"))   #убрать(изьять) все из символов -_!?
print(input().lstrip("-_!?"))  #убрать слева
print(input().rstrip("-_!?"))  #убрать справа

# Переведите цифры в кодировку RGB
R, G, B = int(input()),int(input()),int(input())
R = hex(R).lstrip('0x').zfill(2).upper()
G = hex(G).lstrip('0x').zfill(2).upper()
B = hex(B).lstrip('0x').zfill(2).upper()
print('#' + R + G + B)

# Экранирование 
print("  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/''*''\_\n(/_)^(_\)")
#или
print(r"""  /~~~\
 //^ ^\\
(/(_*_)\)
_/''*''\_
(/_)^(_\)""")

#Формат строк
print("Что Вы сказали? {word}? Какое интересное слово".format(word=input()))
print("Здравствуйте,{1} {0}!".format(input(),input()))
#
number=int(input())
n1 = number - 1
n2 = number + 1
print("""Для числа {number} предыдущим будет число {numb1}.
Для числа {number} следующим будет число {numb2}.""".format(number=number, numb1=n1, numb2=n2))
# F-строки
print(f"Мое имя {input()}!")

name = input()
age = input()
print(f"Hello {name.upper()}. You are {age} years old.")
#или
print(f"Hello {input().upper()}. You are {input()} years old.")

print(f"{input()}, вам исполнится 77 лет в {int(input())+77}")

'''Секунды в минуты'''
sec = int(input())
print(f"{sec} сек - это {sec//60} мин. {sec%60} сек.")
#
widh, height = map(int,input().split())
print(f"""Разрешение экрана: {widh} x {height}.
Общее количество пикселей = {widh*height}.""")
# 
price, many = float(input()), int(input())
print(f"""Current dollar rate is {price}. You want to buy {many} dollars
You must pay {price*many}""")
# F - Строки
"""Вывод переменных"""
x, y = int(input()), int(input())
print(f"Точка({x = }, {y = })") #Точка(x = 5, y = 9)
"""Символы после запятой"""
number_pi = 3.141592653589793
print(f'{number_pi:.6f}') #3.141592
print(f"{float(input()):.2f}") #input 1.1111111 print 1.11
print(f"{int(input()):010d}")  #iput 1 print 000000001
"""Выравнивание"""

number = 12345.6789             #
print(f"Число {number = }")     #Число number = 12345.6789
print(f"|{number:=<25}|")       #|12345.6789===============|
print(f"|{number:=>25}|")       #|===============12345.6789|
print(f"|{number:=^25}|")       #|=======12345.6789========|
print('-'*25)                   #-------------------------
text = "Python 3.10"
print(f"Строка {text = }")      #Строка text = 'Python 3.10'
print(f"|{text:-<25}|")         #|Python 3.10--------------|
print(f"|{text:!>25}|")         #|!!!!!!!!!!!!!!Python 3.10|
print(f"|{text:?^25}|")         #|???????Python 3.10???????|
#
number = int(input())
print(f"{number:-^15}")


