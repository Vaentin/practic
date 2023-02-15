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