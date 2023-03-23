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

