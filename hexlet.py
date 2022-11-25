two = 2 
words = "times"
print(f'{two} {words}')

value = -42
value = abs(value)
print(value)

company1 = "Apple"
company2 = "Samsung"

# BEGIN (write your solution here)
print(len(f'{company1}{company2}'))
#####################################
num1 = 10
num2 = -13
print(abs(num1 * num2))


number = 10.1234
print(hex(round(number)))  #round округлить, hex 16тиричное число

from random import randint
print(randint(1, 10))
########################################################

first_name = '  Grigor   \n '
print(first_name.strip())

########################################################
#С помощью слайсов, получите часть предложения, записанного в переменную text, c 5 по 16 символы включительно. Полученную подстроку обработайте методом .strip() и выведите на экран длину итоговой подстроки. Выполните эти операции подряд в цепочке без создания промежуточных переменных.

text = 'When \t\n you play a \t\n game of thrones you win or you die.'

print(len(text[5:17].strip()))

########################################################
def show():
    text = "Hi!"
    print(text)
show()

def greeting_with_return_and_printing():
    print('Я появлюсь в консоли')
    return 'Hello, Hexlet!'

m = greeting_with_return_and_printing()
#Ore
m = greeting_with_return_and_printing
m()

# BEGIN (write your solution here)
def say_hurray_three_times():
    return 'hurray! hurray! hurray!'


result = say_hurray_three_times()
print(result)  # => 'hurray! hurray! hurray!'

# END

text = 'hexlet'
index = 3
def truncate(text, index):
    return(text[:index] + '...')
    
truncate(text, index)


def truncate(text, index):
    return(text[:index] + '...')
    
truncate('hexlet',3)

#lesson 24 ##########################

def get_hidden_card(card_number, default_stars=4):
    return("*" * default_stars + card_number[-4:])
    
print(get_hidden_card('2034399002125581', 5))
print(get_hidden_card('2034399002125581'))

#lesson 25 ##########################

text = 'python'

def trim_and_repeat(text, offset=0, repetitions=1):
    return(text[offset:] * repetitions)

print(trim_and_repeat(text, repetitions=3))

#lesson 26#################################
def get_age_difference(first_year, second_year):
    return("The age difference is " + str(abs(second_year - first_year)))


actual = get_age_difference(2020, 2010)
print(actual) 

#variant II################################
def get_age_difference(first_year, second_year):
    difference = abs(second_year - first_year)
    print(f"The age difference is {difference}") 


actual = get_age_difference(2020, 2010)

#проверка в тексте заглавных букв
def has_upper_case(text):
    return text != text.lower()



m = has_upper_case('')  # False
# has_upper_case('python')  # False
# has_upper_case('pyThon')  # True
print(m)

#lesson 28#################################
def is_leap_year(year):
    method_1 = year % 400 == 0
    method_2 = year % 4 == 0 
    method_3 = year / 100 == 0
    return method_1 or method_2 and not method_3

test = is_leap_year(2018)
print(test)

#lesson 29 Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается строка yes, иначе no

# def string_or_not(string):
#         result = type(string) == str and 'yes' or 'on'
#         return(result)

def string_or_not(string):
    result = isinstance(string, str)
    return(result and 'yes' or 'no')

#lesson 30

def normalize_url(site):
    adress = 'https://'
    if adress == site[:8]:
        return site
    # elif adress[:4] == site[:4]:#ошибка с сайтом httpsecurity
    elif 'http://' == site[:7]:
        return adress + site[7:]
    else:
        return adress + site

#lesson 31 Test
a = 4
a -= 8 - a
print(a)

a = 4 - (8 - 4)
a = a - (8 - a)

def print_numbers(last_number):
  
    while 1 <= last_number:
      print(last_number)
      last_number -= 1
    print('finished!')

print_numbers(4)

#lesson 32
# Реализуйте функцию join_numbers_from_range(), 
# которая объединяет все числа из диапазона в 
# строку и возвращает получившуюся строку:

def join_numbers_from_range(start,finish):
    result = ''
    i = start
    while i <= finish:
      result = result + str(i)
      i += 1
    return result

print(join_numbers_from_range(5, 10))

#lesson 33
#Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины.
#Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа:
#мое решение полная хрень где не работает while можно его закоментить
def my_substr(string, index_string):  
  sub_string = ''
  while len(sub_string) < index_string:
    sub_string = string[:index_string]

    return sub_string 
#Ответ
def my_substr(string, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string

string = 'If I look back I am lost'
print(my_substr(string, 1))  # => 'I'
print(my_substr(string, 7))  # => 'If I lo'

