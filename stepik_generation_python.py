# if else
password1, password2 = input(), input()

if password1 == password2:
    print('Пароль принят')
else:
    print("Пароль не принят")

#"сумма первой и последней цифр равна разности второй и третьей цифр.
num = int(input())
if (num // 1000 + num % 10) == (num % 1000 // 100 - num % 100 // 10):
    print("ДА")
else:
    print("НЕТ")
#"арефметическая прогрессия
a, b, c = int(input()), int(input()), int(input())
 
if (b - a) + b == c:
    print("YES")
else:
    print("NO")
#"вывод наименьшего числа
a, b = int(input()), int(input())
 
if a < b:
    print(a)
else:
    print(b)

#"из 4 чисел самое маленькое
a, b, c, d = int(input()), int(input()), int(input()), int(input())
min1 = 0
if a < b:
    min1 = a
else:
    min1 = b
if c < d:
    min2 = c
else:
    min2 = d
if min1 < min2:
    print(min1)
else:
    print(min2)

#
a = 7
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b       #для отвлечения внимания?
else:
    b = 5
p = (a + b) * (a + b)       #первое условие 7>2 и 7<17 сработало поэтому b=3
print(p)                    #результат 100

#Красивое число, должно быть 4-х значным и делится на 7 или на 17 
x = int(input())
if (1000 <= x <= 9999) and (x % 7 == 0 or x % 17 == 0):
    print("YES")    
else:
    print("NO")

# Невырожденный треугольник 
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
# Треугольник
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a != b != c and a != c != b: # a != b != c != a
    print("Разносторонний")
else:
    print("Равнобедренный")


# Высокосный год. Кратен 4 не кратен 100 или кратен 400
y = int(input()) 
if  y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("YES")
else:
    print("NO")

# Ход короля 
a, b, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a2 == a - 1 and b2 == b + 1) or (a2 == a and b2 == b +1) or (a2 == a + 1 and b2 == b +1) or (a2 == a - 1 and b2 == b) or (a2 == a and b2 == b) or (a2 == a + 1 and b2 == b) or (a2 == a - 1 and b2 == b - 1) or (a == a2 and b2 == b - 1) or (a2 == a + 1 and b2 == b -1) :
        print("YES")
else:
    print("NO")
# Лучшее решение
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')

# elif Вложенный оператор
#Если n быстрее k нужно вывести «NO», если k быстрее n нужно вывести «YES», если их скорости равны нужно вывести "Don't know".
n, k = int(input()), int(input())
if n > k:
    print("NO")
elif n < k:
    print("YES")
else:
    print("Don't know")

# Среднее число

a, b, c = int(input()), int(input()), int(input())
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)

# количество дней в месце
a = int(input())
if  a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12 :
    print("31")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")
else:
    print("28")
# 2 вариант
a = int(input())
if  a == 2:
    print("28")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")
else:
    print("31")

#Самописный калькулятор
a, b = int(input()), int(input())
s = input() 
if s == "/" and b == 0:
    print("На ноль делить нельзя!")
elif s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
elif s == "/":
    print(a / b)
else:
    print("Неверная операция")

# цветовой микшер
color_1, color_2 = input(), input()
red = "красный"
blue = "синий"
yeallow = "желтый"
orange = "оранжевый"
green = "зеленый"
violet = "фиолетовый"

if color_1 == color_2 == red:
    print(red)
elif color_1 == color_2 == blue:
    print(blue)
elif color_1 == color_2 == yeallow:
    print(yeallow)
elif color_1 == blue and color_2 == red or color_1 == red and color_2 == blue:
    print(violet)
elif color_1 == red and color_2 == yeallow or color_1 == yeallow and color_2 == red:
    print(orange)
elif color_1 == yeallow and color_2 == blue or color_1 == blue and color_2 == yeallow:
    print(green)
else:
    print("ошибка цвета")

# Рулетка
n = int(input())
green = "зеленый"
red = "красный"
black = "черный"

if n == 0:
    print(green)
elif 1 <= n <= 10:
    if  n % 2 == 0:
        print(black)
    else:
        print(red)
elif 11 <= n <= 18:
    if  n % 2 == 0:
        print(red)
    else:
        print(black)
elif 19 <= n <= 28:
    if  n % 2 == 0:
        print(black)
    else:
        print(red)
elif 29 <= n <= 36:
    if  n % 2 == 0:
        print(red)
    else:
        print(black)
else:
    print("ошибка ввода")

# 2 вариант рулетки
a = int(input())
if 0<=a<37:
  if (0<a<11 or 18<a<29) and a%2 or (10<a<19 or 28<a<37) and a%2==0:
    print('красный')
  elif a == 0:
    print('зеленый')
  else:
    print('черный')
else:
  print('ошибка ввода')

# Пересечение отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if  b1 < a2 or b2 < a1:
    print("пустое множество")
elif b1 == a2:
    print(b1)
elif a1 == b2:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1,)
elif a2 <= a1 < b2 < b1:
    print(a1, b2,)
elif a1 < a2 <b2 <= b1:
    print(a2, b2,)
else:
    print(a1, b1,)
# !!!!  ЭКЗАМЕН  !!!!

# 1 Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».
a = int(input())
if a % 100 == 0:
    print("YES")
else:
    print("NO")
# 2 Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + x2 + y1 + y2) % 2 == 0:
    print("YES")
else:
    print("NO")
# 3 Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
num = int(input())
if num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
elif num == 10:
    print("X")
else:
    print("ошибка")
# Более интересное решение
n = int(input())
if not 0 < n < 11:
    print('ошибка')
elif n < 4:
    print(n*'I')
elif n == 4:
    print('IV')
elif n < 9:
    print('V' + (n-5)*'I')
elif n < 11:
    print((10-n)*'I' + 'X')
# 4 
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».
num = int(input())
if num % 2 != 0:
    print("YES")
else:
    if 2 <= num <= 5:
        print("NO")
    elif 6 <= num <= 20:
        print("YES")
    else:
        print("NO")
   
# 5 Ход Слона
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a - b) == (c - d) or (a + b) == (c + d):
    print('YES')
else:
    print('NO')
# 6 Ход ГРЕБАННОГО Коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if ((x1 - x2 == 1 or x2 - x1 == 1) and (y1 - y2 == 2 or y2 - y1 == 2)):
    print("YES")
elif ((x1 - x2 == 2 or x2 - x1 == 2) and (y1- y2 == 1 or y2 - y1 == 1)):                                            
    print("YES")
else:
    print("NO")
# Решение с квадратом
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
    print("YES")
else:
    print("NO")
# Ход ферзя
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2) or (x1 - x2)**2 == (y1 -y2)**2:
    print("YES")
else:
    print("NO")

# Первое десятичное число
print(int(float(input()) * 10) % 10)
# Десятичные
print(float(input())% 1)
# Второе решение
a=float(input())
print(a-int(a))

#Самое короткое и длииное название города
town1, town2, town3 = input(), input(), input()
minl = min(len(town1), len(town2), len(town3))
maxl = max(len(town1), len(town2), len(town3))
if minl == len(town1):
    print(town1)
elif minl == len(town2):
    print(town2)
else:
    print(town3)
if maxl == len(town1):
    print(town1)
elif maxl == len(town2):
    print(town2)
else:
    print(town3)

#    Оператор in  #
s = input()
if "синий" in s:
    print("YES")
else:
    print("NO")

# суббота ИЛИ воскресенье в строке
s = input()
if "суббота" in s:
    print("YES")
elif "воскресенье" in s:
    print("YES")
else:
    print("NO")
# Лучше решение
s = input()
if 'суббота' in s or 'воскресенье' in s:
    print('YES')
else:
    print('NO')

# Модуль math # import math или from math import *

from math import sqrt #корень
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(p)

from math import pi
R = float(input())
S = pi * R ** 2
C = 2 * pi * R
print(S, C, sep = "\n")

# Пол и потолок
import math
x = float(input())
print(math.ceil(x) + math.floor(x))
# Правильный многоугольник
from math import tan, pi
n, a = float(input()), float(input())
S = (n * (a**2)) / (4 * tan(pi / n))
print(S)

""""""""""""""""""""""""""""""""""""""""""""""""""
# ЦИКЛ for

"""for название_переменной_цикла in range(количество повторений):
    блок кода"""

for i in range(10):
    print("Python is awesome!")