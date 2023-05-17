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
# Повторяй за мной 2
name = input()
for i in range(10):
    print(i, name)

#Квадрат числа
n = int(input()) + 1 
for i in range(n):
    print("Квадрат числа " + str(i) + " равен " + str(i**2))
#лучше
n = int(input())
for i in range(n + 1):
    print("Квадрат числа ", i, " равен ", i**2)
#Звездный треугольник
n = int(input())
for i in range(n):
    print("*" * (n - i))

# Популяция
# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, (m * (p / 100 + 1) ** i))

# Range
m, n = int(input()), int(input()),
for i in range(m, n + 1):
    print(i)

#Последовательность чисел
m, n = int(input()), int(input()),

if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
else:
    print(m)
    
#!!!!!!!!!!!Последовательность чисел!!!!!!!!!!
# Даны два целых числа m и n (m>n).
# Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
# Не используя if
m, n = int(input()), int(input()),
for i in range(m % 2 + m - 1, n - 1, -2):
    print(i)

# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.

m, n = int(input()), int(input()),
for i in range(m,n+1):
    if i % 10 == 9 or i % 17 == 0 or i % 15 == 0:
        print(i)
#Таблица умножения
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#На вход программе подаются два целых числа a и b (a≤b). 
#Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых ОКАНЧИВАЕТСЯ на 4 4 или 9
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if (i ** 3) % 10 == 9 or (i ** 3) % 10 == 4:
        counter = counter + 1
print(counter)

# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
num = int(input())
count = 0
sum = 0
for i in range(0, num):
   count = int(input())
   sum = sum + count
print(sum)
#или
s = 0
for i in range(int(input())):
  s += int(input())
print(s)

#Асимптотическое приближение
from math import log
n= int(input())
num = 0
for i in range(1, n):
    num =  num + (1 / ( i  +  1))
   
print((1 + num) - log(n))

# На вход программе подается натуральное число n.
# Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно)
# квадрат которых оканчивается на 2,5 или 8.
n= int(input())
count = 0
for i in range(1, n + 1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10  == 8:
        count += i
print(count)

#Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

result = 1
for i in range(10):
    num = int(input())
    if num != 0:
        result *= num
print(result)

#Сумма всех делителей
n = int(input())
result = 0
for i in range(1, n + 1):
    if (n / i) % 1 == 0.0:
        result += i
print(result)

#Знакочередующаяся сумма
n = int(input())
count = (((-1)**(n+1))*(2*n+1)+1)/4
print(int(count))
#              !  Наибольшие числа  !
n = int(input())
num = 0
count = 0
count2 = 0
for i in range(n):
    num = int(input())         #5            4                3
    if num > count:            #5 > 0        4 > 5 False      3 > 5 False
        count2 = count         #count2 = 0   
        count = num            #count = 5
    elif num > count2 < count: #             4 > 0 < 5 True   3 > 4 < 5 False
        count2 = num           #             count2 = 4
print(count)
print(count2)

# Напишите программу,
# которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
count = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        count += 1
if count == 10:
    print('YES')
else:
    print('NO')

#Более интересное
flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)

#  !!! WHILE !!!
# Концом последовательности является слово «КОНЕЦ» 
text = input()
while text != 'КОНЕЦ':
    print(text)  
    text = input()
#Концом последовательности является слово «КОНЕЦ» или «конец»
text = input()
stop1 = 'КОНЕЦ' 
stop2 = 'конец'
while text != stop1 and text != stop2:
    print(text)  
    text = input()
#Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). 
#Напишите программу, которая выводит общее количество членов данной последовательности.
text = input()
count = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    count += 1
    text = input()
print(count) 
# Концом последовательности является любое число не делящееся на 7
# А еще 0 надо тоже выводить
number = int(input())
while number % 7 == 0:
    print(number)
    number = int(input())

#Концом последовательности является любое отрицательное число.
#Напишите программу, которая выводит сумму всех членов данной последовательности.
number = int(input())
total = 0
while number >= 0:
    total += number
    number = int(input())       
print(total)

#Количество пятерок
number = 0
five = 0
while 0 <= number <= 5:    
    number = int(input())
    if number == 5:
        five += 1
print(five)

#В мире ведьмака существуют монеты с номиналами 1,5,10,25.
#Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
n = int(input())
monet = 0
while n >= 25:
    monet += 1
    n = n - 25
while n >= 10:
    monet += 1
    n = n - 10
while n >= 5:
    monet += 1
    n = n - 5
while n >= 1:
    monet += 1
    n = n - 1
print(monet)

#Дано натуральное число.
#Напишите программу, которая выводит его цифры в столбик в обратном порядке.
num = int(input())
while num > 0:
    reslut = num % 10
    num = num // 10
    print(reslut)
#Второй вариант
num = int(input()) 
while num != 0:
    print(num % 10)    
    num = num // 10

#Обратный порядок
num = int(input())
result = 1
while num > 0:
    result = num % 10
    num //= 10
    print(result, end = "")
#Более понятно
num = int(input())
newnum = 0

while num != 0:
    last_digit = num % 10
    newnum = newnum*10 +last_digit
    num = num // 10 

print(newnum)

#  Максимальная и Минимальная ЦИФРА в ЧИСЛЕ
num = int(input())
n = 0
n_max = 0
n_min = 9
while num > 0:
    n = num % 10
    num //= 10
    if n > n_max:
         n_max = n
    if n < n_min:
         n_min = n
print('Максимальная цифра равна', n_max)
print('Минимальная цифра равна', n_min)

# Все вместе
sum_n = 0     # сумму его цифр;
total_n = 0   # количество цифр в нем;
total_nn = 1  # произведение его цифр;
arph_n = 0    # среднее арифметическое его цифр;
first_n = 0   # его первую цифру;
sum_f_l_n = 0 # сумму его первой и последней цифры.
n = 0         # цифра
num = int(input())
last_n = num % 10

while num > 0:
    n = num % 10
    total_n += 1
    sum_n += n
    total_nn *= n
    num //= 10
    
    if num > 0:
        first_n = num
arph_n = sum_n / total_n
sum_f_l_n = first_n + last_n
print(sum_n) 
print(total_n) 
print(total_nn) 
print(arph_n)    
print(first_n)
print(sum_f_l_n)

#Вторая цифра числа
num = int(input())
while num > 9:
    second_num = num % 10
    num //= 10
print(second_num)

# Дано натуральное число.
# Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
num1 = num
flag = True
n1 = 0
n2 = 0
while num != 0:
    n2 = num % 10
    
    while num1 > 0:
        n1 = num1
        num1 //= 10
    num //= 10
    if n1 != n2:
        flag = False

if flag == True:
    print('YES')
else:
    print('NO')

# Второй вариант (Берем последнюю и сравниваем с предпоследней и так до первой)
n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)    

# ! Упорядоченные цифры !
num = int(input())
result = 'YES'
while num != 0:
    last_num = num % 10
    prelast = num % 100 // 10
    if last_num > prelast and prelast != 0:
        result = 'NO'
    num //= 10
print(result)

# Наименьший делитель
n = int(input())

for i in range(2, n+1):
    if n % i == 0:
        break 
print(i)

#числа от 1 до n включительно за исключением:
#чисел от 5 до 9 включительно;
#чисел от 17 до 37 включительно;
#чисел от 78 до 87 включительно.
n = int(input())

n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
#Вариант 2
n = int(input())
for i in range(1, n + 1):
    if i in range(5, 10):
        continue  
    if i in range(17, 38):
        continue        
    if i in range(78, 88):
        continue
    print(i)
# Первая ЦИФРА
n = int(input())
while n > 9:
    n //= 10
print(n)

#Программа должна вывести таблицу размером n × 3 состоящую из данного числа
n = int(input())
for _ in range(n): 
    for i in range(3):
        print(n, end = ' ')
    print()
#Напишите программу, которая печатает таблицу размером n × 5,
#где в i-ой строке указано число i (числа отделены одним пробелом).
n = int(input())
for i in range(1, n + 1): 
    for _ in range(5):
        print(i, end = ' ')
    print()
#Таблица сложения
n = int(input())
for i in range(1, n + 1):
    for j in range(1,10):
        print(i, '+', j, '=',  i + j)
    print()

#равнобедренный звездный треугольник с основанием, равным n в соответствии с примером
n = int(input())
for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n // 2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
"""
3

*
**
*
"""
#Цифровая пирамида
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end = '')
    print()
#Решите уравнение в натуральных числах 28n + 30k + 31m = 365.
# n <= 13 (365/28) Если k и n равны 0
# k <= 12 (365/30)
# m <= 11 (365/31)
for n in range(1, 13):
    for k in range(1, 12):
        for m in range(1, 11):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)
#Имеется 100 рублей.
#Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка 10 рублей, 
# за корову – 5 рублей, 
# за теленка – 0.5 рубля 
# и надо купить 100 голов скота?
for b in range(100):
    for k in range(100):
        for t in range(100):
            if (10 * b + 5 * k + 0.5 * t == 100) and (b + k + t == 100):
                print(b, k, t) 
#Пирамида из цифр
n = int(input())
count = 1
for i in range(1, n + 1):
    for j in range(i):
        print(count, end = ' ')
        count += 1
    print()

#Дано натуральное число n.
#Напишите программу, которая печатает численный треугольник с высотой равной n,
#в соответствии с примером:
# 1
# 121
# 12321
# 1234321
# 123454321
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = '')
    for k in range(j, 1, -1):
         print(k - 1, end = '')
    print()
# 7.9.3 
#Программа должна вывести два числа на одной строке, разделенных пробелом:
#число с максимальной суммой делителей и сумму его делителей.
# Мое решение
a, b = int(input()), int(input())
sum_sep = 0
max_sep = 0
for i in range (a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
        if total >=sum_sep and i >= max_sep:
            sum_sep = total
            max_sep = i
print(max_sep, sum_sep)
# Решение 2
a, b = int(input()), int(input())
counter = 0 # счетчик подсчета суммы делителей
number = 1 # число которое будем выводить 
summa = 0  # тут будет сумма делителей, которую надо будет вывести
for i in range(a, b + 1):  # проверяем каждое число в [a;b]
    counter = 0 # обнуляем счетчик для каждого i
    for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
        if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
            counter += j  # создаем сумму делителей
    if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
        summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
        number = i  # число у которого делителей оказалось больше, теперь равно number
print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей

#В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.
n = int(input())
for i in range(1, n + 1):
    plus = ''
    for j in range(1, i + 1):
        if i % j == 0:
            plus += '+'
    print(j, plus, sep = '')
# Результат n = 5
# 1+
# 2++
# 3++
# 4+++
# 5++

#Программа должна вывести цифровой корень введенного числа
#192: 1+9+2=12, 1+2=3
n = int(input())
sum_digit = 0
last_digit = 0

while n > 0:
    last_digit = n % 10
    n //= 10        
    sum_digit += last_digit
while sum_digit > 9:
    last_digit = sum_digit % 10
    sum_digit //= 10        
    sum_digit += last_digit
    
print(sum_digit)

#Сумма факториалов 
n = int(input())
factorial = 1
sum_factorial = 0
for i in range(1, n + 1):
    factorial *= i
    sum_factorial += factorial
print(sum_factorial)

#Программа должна вывести все простые числа от a до b включительно
a, b = int(input()), int(input())

for i in range(a, b + 1):
    count = 0
    for j in range(1, b + 1):        
        if i % j == 0:
            count +=1 
    if count == 2:
        print(i)
#!!!!! ЭКЗАМЕН ЦИКЛЫ !!!!!

# РЕВЬЮ КОДА

#На обработку поступает натуральное число.
#Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа или 0, если чётных цифр в записи нет.
#Программист торопился и написал программу неправильно.
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)

#На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**12
#Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной последовательности и максимальное делящееся нацело на 4 число.
#Если делящихся нацело на 4 чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
n = 8
count = 0
maximum = -10 ** 12 - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

#На обработку поступает последовательность из 4 целых чисел.
#Известно, что вводимые числа по абсолютной величине не превышают 10**8
#Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и максимальное нечётное число.
#Если нечётных чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
n = 4
count = 0
maximum = -10**8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
            
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

#Звездная рамка

#На вход программе подается натуральное число n.
#Напишите программу, которая печатает звездную рамку размерами n×19
n = int(input())
print('*' * 19)
for i in range(n - 2):
    print('*',' ' * 15,'*')
print('*' * 19)

# Все и сразу
n = int(input())
count_digit_3 = 0   # количество цифр 3 в нем;
count_last_digit = 0    # сколько раз в нем встречается последняя цифра;
last_digit = n % 10
total_even = 0    # количество четных цифр;
sum_5 = 0         # сумму его цифр, больших пяти;
mult_7 = 1
count_greater_than_7 = 0        # произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
sum_digit_0_5 = 0 # сколько раз в нем встречается цифры 0 и 5 (всего суммарно)

while n != 0:
    digit = n % 10
    
    if digit == 3:
        count_digit_3 += 1
    if digit == last_digit and n != 0:
        count_last_digit += 1
    if digit % 2 == 0:
        total_even += 1
    if digit > 5:
        sum_5 += digit
    if digit > 7:
        mult_7 *= digit
        count_greater_than_7 += 1
    if digit == 0 or digit == 5:
        sum_digit_0_5 += 1
    n //= 10
print(count_digit_3)
print(count_last_digit)
print(total_even)
print(sum_5)
if count_greater_than_7 == 0:
    print(1)
elif count_greater_than_7 == 1:
    print(mult_7)
else:
    print(mult_7)
print(sum_digit_0_5)

# 9 СТРОКОВЫЙ ТИП ДАННЫХ 
# На вход программе подается одна строка.
# Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик
s = input()
for i in range(0, len(s), 2):
    print(s[i])
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
s = input()
for i in range(len(s)):
    print(s[i])
# Напишите программу, которая считает сумму цифр данной строки.
n = input()
sum = 0
for c in n:
    sum += int(c)
print(sum)

# Цифра в строке 
s = input()
flag = True
for c in s:
    for i in range(10):
        if c == str(i):
            flag = False
if flag == True:
    print('Цифр нет')
else:
    print('Цифра')
# Второе решение 
s = input()
flag = False
for i in range(10):
    if str(i) in s:
        flag = True
        break
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')
# Сколько раз встречаются символы в строке
s = input()
total_plus = 0
total_star = 0

for c in s:
    if c == '+':
        total_plus += 1
    if c == '*':
        total_star += 1
print('Символ + встречается',total_plus, 'раз')
print('Символ * встречается',total_star, 'раз')

# Одинаковые соседи
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
s = input()
total = 0
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        total += 1
print(total)
# Второй вариант
s, count, = input(), 0
n = 0
for c in s:
    if c == n:
        count += 1
    n = c
print(count)

# Гласные и согласные
string = input().lower()
glasnie = 'ауоыиэяюёе'
soglasnie = 'бвгджзйклмнпрстфхцчшщ'
total_glasnie = 0
total_soglasnie = 0
for c in string:
    for g in glasnie:
        if c == g:
            total_glasnie += 1
    for s in soglasnie:
        if c == s:
            total_soglasnie += 1
print('Количество гласных букв равно', total_glasnie)
print('Количество согласных букв равно', total_soglasnie)

# Перевод десятичных сичел в двоичные
decimal = int(input())
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print(binary)
# Палиндром
s = input()
if s == s[::-1]:
    print('YES')
else:
    print('NO')
#
s = input()
print(len(s))   #общее количество символов в строке
print(s * 3)    #исходную строку повторенную 3 раза
print(s[0])     #первый символ строки
print(s[:3])    #первые три символа строки
print(s[-3:])   #последние три символа строки
print(s[::-1])  #строку в обратном порядке
print(s[1:-1])  #строку с удаленным первым и последним символом
print(s[2])      # третий символ этой строки;
print(s[-2])     # предпоследний символ этой строки;
print(s[:5])     # первые пять символов этой строки;
print(s[:-2])    # всю строку, кроме последних двух символов;
print(s[::2])    # все символы с четными индексами;
print(s[1::2])    # все символы с нечетными индексами;
print(s[::-1])    # все символы в обратном порядке;
print(s[-1::-2])    # все символы строки через один в обратном порядке, начиная с последнего.

# Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.
from math import ceil
s = input()
print(s[ceil(len(s)/2):] + s[:ceil(len(s)/2)])

# !!!  Методы строк  !!!
# Программа должна вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном случае.
s = input()
if s == s.title():
    print('YES')
else:
    print('NO')
# Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок
s = input().upper()
x = 'ХОРОШ'
if x in s:
    print('YES')
else:
    print('NO')

# Программа должна вывести количество буквенных символов в нижнем регистре.
# БЕЗ ЦИФР
s = input()
count = 0
for i in s:
    if i == i.lower() and i not in '1234567890':
        count += 1
print(count)

# Количество слов разделенных пробелом
print(input().count(' ') + 1)
# Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
n = int(input())
count = 0
for _ in range(n):
    s = input()
    if s.count('11') >= 3:
        count += 1
print(count)

# Количество цифр в строке
s = input()
count = 0
for i in s:
    if i in "0123456789":
        count += 1
print(count)
# Более интересный вариант с применением метода .count()
n = input()
count = 0
for i in range(10):
    count += n.count(str(i))
print(count)
# Программа должна вывести «YES» если введенная строка заканчивается подстрокой .com или .ru и «NO» в противном случае.
s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')
# Самый частотный символ
s = input()
simbol = ''
count = 0
for i in s:
   if s.count(i) >= count:
        simbol = i
        count = s.count(i)
print(simbol)

# На вход программе подается строка текста.
# Если в этой строке буква «f» встречается только один раз, выведите её индекс. 
# Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных символом пробела. 
# Если буква «f» в данной строке не встречается, следует вывести «NO».
s = input()
count_f = s.count('f')

if count_f == 1:
    print(s.find('f'))
elif count_f > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
# вариант 2
s= input()
if s.find('f') == -1:
    print('NO')
elif s.find('f') == s.rfind('f'):
    print(s.find('f'))
else:
    print(s.find('f'),s.rfind('f'))

# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])

# Метод format
s = 'In {0}, someone paid {1} {2} for two pizzas.'
year = 2010
price = '10k'
BTC = 'Bitcoin'
print(s.format(year, price, BTC))
# Вариант 2
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format('2010','10k','Bitcoin')
print(s)
# Метод f-строка
year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

# Функции ord() и chr()

# Символы в диапазоне
a, b = int(input()), int(input())
for c in range (a, b + 1):
    print(chr(c), end = ' ')
# Простой шифр
s = input()
for i in s:
    print(ord(i), end = ' ')
# !! Шифр Цезаря !!
n = int(input())
s = input()
for i in s:
    dec = ord(i) - n
    if dec < 97:
        dec += 26
    print(chr(dec), end = '')
# !!!! ЭКЗАМЕН  !!!!
# Напишите программу, которая удаляет из нее все символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ...
s = input()
new_s = ""

for i in range(len(s)):
    if i % 3 != 0:
        new_s += s[i]

print(new_s)

#Замена 1 на one
s = input()
print(s.replace('1', 'one'))

# Напишите программу, которая выводит индекс второго вхождения буквы «f». 
# Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
s = input()
count_f = s.count('f')

if count_f == 1:
    print(-1)
elif count_f > 1:
    print(s.find('f',s.find('f') + 1))
else:
    print(-2)

# ПЕРЕВОРОТ
# На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
# Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h»
s = input()
start = s[:s.find('h') + 1]
centr = s[s.find('h') + 1: s.rfind('h')] 
finish = s[s.rfind('h'):]
print(start + centr[::-1] + finish )
# Вариант 2
s=input()
a=int(s.find('h'))
b=int(s.rfind('h'))
print(s[:a]+s[b:a:-1]+s[b:])

# !! ***СПИСКИ*** !!
# Список чисел
n = int(input())
print(list(range(1, n + 1)))

# Напишите программу, которая выводит список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
n = int(input())
a = ''
for i in range(1, n + 1):
    a += (chr(96 + i))
print(list(a))

# Дополните приведенный код, так чтобы он вывел сумму минимального и максимального элементов списка numbers.
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

print(sum([max(numbers), min(numbers)]))
# Замена элемента списка
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[6] = 'Фиолетовый'
print(rainbow)

# Все сразу
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))                 # Вывел длину списка;
print(numbers[-1])                  # Вывел последний элемент списка;
print(numbers[:: -1])               # Вывел список в обратном порядке (вспоминаем срезы);
if 5 in numbers and 17 in numbers:  # Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
    print('YES')
else:
    print('NO')

del numbers[0]                      # Вывел список с удаленным первым и последним элементами.
del numbers[-1]                    
print(numbers)       
# Вариант 2
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
ans = 'YES' if [5, 7] in numbers else 'NO'
print(len(numbers), numbers[-1], numbers[::-1], ans, numbers[1:-1], sep='\n')
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.
n = int(input())
words = []
for i in range(n):
    words.append(input())
print(words)
# Напишите программу, выводящую следующий список:
#['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
lst = list()
for i in range(1, 27):
    lst.append(chr(i + 96) * i)
print(lst)
# Список кубов
n = int(input())
lst = list()
for i in range(n):
    lst.append(int(input())**3)
print(lst)
# Список делителей
n = int(input())
lst = list()
for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)
print(lst)
# ! Сумма двух !
# На вход программе подается натуральное число n≥2, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и3 и т.д.)
n = int(input())
lst = list()
count = 0
for _ in range(1, n + 1):
    lst.append(int(input()))
result = list()
for i in range (n - 1):
    result.append(lst[i] + lst[i + 1])
print(result)

# На вход программе подается натуральное число n, а затемv  целых чисел.
# Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
del lst[1::2]
print(lst)

# !! k-ая буква слова !!
# На вход программе подается натуральное число n и n строк, а затем число k. !!
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов
n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

k = int(input())
for i in lst:
    if len(i) >= k:
       print(i[k - 1], end = '' )

# На вход программе подается натуральное число n, а затем n строк. 
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.
lst = []
for _ in range(int(input())):
    lst.extend(input())
print(lst) 

# ! Вывод элементов списка!
# сума квадратов элементов списка numbers
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
lst = []
for i in numbers:
    lst.append(int(i) ** 2)
print(sum(lst))

#  Напишите программу, которая для каждого введенного числа x выводит значение функции f(x)=x**2 + 2x + 1, каждое на отдельной строке.
lst = []
for _ in range(int(input())):
    lst.append(int(input()))
print(*lst, sep='\n')
print()
for x in lst:
    f = 0
    f = (x**2) + (2 * x) + 1
    print(f)
# Результат
#Sample Input 1:
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
# 1
# 2
# 3
# 4
# 5

# 4
# 9
# 16
# 25
# 36

# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
lst = []
for _ in range(int(input())):
    lst.append(int(input()))
result_lst = []
for i in lst:
    if i != min(lst) and i != max(lst):
        result_lst.append(i)
print(*result_lst, sep = '\n')
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
lst = []
for _ in range(int(input())):
    lst.append(input())
result_lst = []
for i in lst:
    if i not in result_lst:
        result_lst.append(i)
print(*result_lst, sep = '/n')
# Google search
# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. 
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
lst = []
for _ in range(int(input())):
    lst.append(input())

result_search  = []
search = input().lower()
for i in lst:
    if search in i.lower():
        result_search.append(i)
print(*result_search, sep = '\n')

# !!!! Google search 2 !!!!
# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k строк — поисковые запросы. 
# Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
lst = []
for n in range(int(input())):
    lst.append(input())

lst_search = []
for k in range(int(input())):
    lst_search.append(input())

result_search  = []

for i in lst:
    flag = True
    for j in lst_search:
        if j.lower() not in i.lower():
            flag = False
            break
    if flag:
        print(i)

# Negatives, Zeros and Positives
lst = []
for n in range(int(input())):
    lst.append(int(input()))
m_digit, p_digit, z_digit = list(), list(), list()

for i in lst:
    if i < 0:
        m_digit.append(i)
    elif i > 0:
        p_digit.append(i)
    else:
        z_digit.append(i)
print(*m_digit, *z_digit, *p_digit, sep = '\n')

# Построчный вывод
print(*input().split(), sep = '\n')

# Инициалы
s = input().split()
for i in s:
    print((i[0]), end = '.')

# На вход программе подается одна строка с корректным именем файла в операционной системе Windows. 
# Напишите программу, которая разбирает строку на части, разделенные символом "\". 
# Каждую часть вывести в отдельной строке.
s = input().split('\\')
for i in s:
    print(i)
# Напишите программу, которая по заданным числам строит столбчатую диаграмму.
s = input().split()
for i in s:
    print('+' * int(i))
# Корректный ip-адрес
s = input().split('.')
flag = True
for i in s:
    if int(i) > 255:
       flag = False
       break
if flag:
    print('ДА')
else:
    print('НЕТ')
# Второй вариант
flag = 'ДА'
for c in input().split('.'):
    if int(c) > 255:
        flag = 'НЕТ'
print(flag)

# Добавь разделитель
s = input()
j = input()
print(j.join(s))
# Второй вариант
print(*list(input()), sep=input())

# ! Количество совпадающих пар !
# На вход программе подается строка текста, содержащая натуральные числа. 
# Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, 
# сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, 
# равные друг другу образуют одну пару, которую необходимо посчитать.
s = input().split()
count = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)
# Sample Input 1:
# 1 7 5 7 5
# Sample Output 1:
# 2

# МЕТОДЫ СПИСКОВ ЧАСТЬ 2
# list.append(x)Добавляет элемент в конец списка
# list.extend(L)Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x)Вставляет на i-ый элемент значение x
# list.remove(x)Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]])Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)Возвращает количество элементов со значением x
# list.sort([key=функция])Сортирует список на основе функции
# list.reverse()Разворачивает список
# list.copy()Поверхностная копия списка
# list.clear()Очищает список
numbers = [8, 9, 10, 11]

numbers[1] = 17                # Заменил второй элемент списка на 17;
numbers.extend([4, 5, 6])      # Добавил числа 4, 5 и 6 в конец списка;
numbers.pop(0)                 # Удалил первый элемент списка;
del numbers[0]                 
numbers *= 2                   # Удвоил список;
numbers.insert(3, 25)          # Вставил число 25 по индексу 3;
print(numbers)                 # Вывел список, с помощью функции print()

# Переставить min и max
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

item_min = min(numbers)
item_max = max(numbers)
index_min = numbers.index(item_min)
index_max = numbers.index(item_max)
numbers.pop(index_min)
numbers.insert(index_min, item_max)
numbers.pop(index_max)
numbers.insert(index_max, item_min)

print(*numbers)

# Количество артиклей в тексте
words = input().lower().split()
article = ['a', 'an', 'the']
article_count = 0
for i in article:
    article_count += words.count(i)

print('Общее количество артиклей:',article_count)
# Вариант 2
s = input().lower().split()
print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")

# !! Убрать комментарии из кода !!
code_str = int((input())[1:])

for i in range(code_str):
    string = input()
    if '#' in string:
        print(string[:(string.index('#'))].rstrip())
    else:
        print(string)
# Вариант 2 
n = int(input()[1:]) 
for _ in range(n):
    s = input().split('#') # Разделитель списка '#' один что то там #два что то тут -> [один что то там , два что то тут ]
    print(s[0].rstrip())   # Печатаем первый элемент списка [0] и удаляем пробелы справа -> один что то там

# Сортировка чисел
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
print(*s)
s.sort(reverse = True)
print(*s)

# Удаленный первый символ
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [k[1:] for k in keywords]
#список содержащий длины строк исходного списка.
lengths = [len(k) for k in keywords]
# список содержащий только слова длиной не менее пяти символов (включительно).
new_keywords = [k for k in keywords if len(k) >= 5]

# Палиндром от 100 до 1000
palindromes = [i for i in range(100, 1000) if i % 10 == i // 100] # Если первое и третье числа равны

# Список квадратов от 1 до n
n = [i ** 2 for i in range(1, (int(input())) + 1)]
print(*n, sep = "\n")

# Список кубов из строки текста
numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
n = [j ** 3 for j in numbers]

for _ in n:
    print(_, end = ' ')
# Вариант 2
n = [int(i) ** 3 for i in input().split()]
for i in n:
    print(i, end = ' ')
# Строка в столбик
print(*[i for i in input().split()], sep = "\n")
# или
[print(s) for s in input().split()]

# только цифры
print(*[n for n in input() if n in '0123456789'], sep = '')

# Напишите программу, использующую списочное выражение, которая выведет квадраты четных чисел, которые не оканчиваются на цифру 4.
print(*[int(n) ** 2 for n in input().split() if (int(n) ** 2) % 10 != 4 and (int(n) ** 2) % 2 == 0 ])

#  Алгоритм пузырьковой сортировки
a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)

for i in range(n - 1):
    is_sorted = True  
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            is_sorted = False 
    if is_sorted:
        break 

print(a)

#  Алгоритм сортировки выбором
a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)
for i in range(n):
        # Мы предполагаем, что первый элемент несортированного сегмента является наименьшим
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, n):
            if a[j] < a[lowest_value_index]:
                lowest_value_index = j
        # Поменять местами значения самого низкого несортированного элемента с первым несортированным
        a[i], a[lowest_value_index] = a[lowest_value_index], a[i]
# реализация алгоритма сортировки выбором

print(a)

#   **Экзамен списки**
# Список четных
print([i for i in range(2, int(input()) + 1) if i % 2 == 0])

# Сумма двух списков
L = input().split()
M = input().split()
lst = []
for i in range(len(L)):
    lst.append(int(L[i]) + int(M[i]))
print(*lst)
# Второй вариант
l, m = input().split(), input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))

# Сумма чисел
lst = input().split()
print("+".join(lst),sum([int(i) for i in lst]), sep ='=')

# !Валидный номер! 
# abc-def-hijk или
# 7-abc-def-hijk
number = input().split('-')
flag = True
if len(number[0]) == 1 and number[0] == '7': 
    number.remove('7')

if len(number[0]) != 3 or len(number[1]) != 3 or len(number[2]) != 4:
    flag = False    

for i in number: 
    for j in i:
        if j not in '0123456789':
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")

# Самый длинный
n = (input().split())
lst =[]
for i in n:
    lst.append(len(i))
print(max(lst))
# Вариант 2
print(max([len(a) for a in input().split()]))

# Молодежный жаргон
print(*[i[1:] + i[0] + "ки"for i in input().split()])

# !!!! Функции !!!!

# Звездный прямоугольник 14 x 10

def draw_box():
    print("**********")
    for i in range(12):
        print("*        *")
    print("**********")

draw_box()

# Звездный треуголник
def draw_triangle():
    for i in range(1, 11):
        print("*" * i)
draw_triangle()
# Звездный треуголник 2
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, (base // 2) + 1):
        print(fill * i)
    for i in range((base // 2) + 1, 0, -1):
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

# ФИО
# объявление функции
def print_fio(name, surname, patronymic):
    fio = surname[0] + name[0] + patronymic[0]
    print(fio.upper())

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

# Сумма цифр
# объявление функции
def print_digit_sum(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
# Вариант 2
def print_digit_sum(num):
    print(sum([int(i) for i in num]))
print_digit_sum(input())

# километры в мили
# объявление функции
def convert_to_miles(km):
    return km * 0.6214

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))

# дней в месяце
# объявление функции
def get_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
# считываем данные
num = int(input())
# вызываем функцию
print(get_days(num))

# Найти индексы всех символов в строке
# объявление функции
def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if target[i] == symbol:
            lst.append(i)
    return(lst)
# считываем данные
s = input()
char = input()
# вызываем функцию
print(find_all(s, char))

# Merge lists 1 Два списка
# объявление функции
def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1
# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))