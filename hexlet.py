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
#мое решение полная (хрень где не работает while можно его закоментить)
def my_substr(string, index_string):  
  sub_string = ''
  while len(sub_string) < index_string:
    sub_string = string[:index_string]

    return sub_string 
#попытка 2
def my_substr(string, index_string):
  sub_string = ''
  index = 0
  while index < index_string:
    sub_string += string[index]
    index += 1
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


#lesson 34
# Реализуйте функцию is_contains_char(),
# которая проверяет, содержит ли строка указанную букву.
# Регистр букв не важен. Функция принимает два параметра:

def is_contains_char(text, letter):
  index = 0
  words = text.lower()
  char = letter.lower()
  while index < len(text):
    if words[index] == char:
      return True
    index += 1   
  return False

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False
# Ответ:
def is_contains_char(string, char):
    index = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            return True
        index += 1
    return False


#lesson 35

# Реализуйте функцию filter_string().
# Она принимает на вход строку и символ и возвращает новую строку, 
# в которой удалён переданный символ во всех его позициях.
# Если строка не содержит указанный символ, то она возвращается без изменений.


def filter_string(text, char):
    result = ''
    for current_char in text:
      if current_char.upper() != char.upper():
       result += current_char
    return result.strip()

text = '  If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win
print(filter_string(text, ''))

# Ответ
def filter_string(text, char):
    result = ''
    lowered_char = char.lower()
    for current_char in text:
        if current_char.lower() != lowered_char:
            result += current_char
    return result.strip()

#lesson36

# Реализуйте функцию is_palindrome(), которая принимает на вход слово,
# определяет является ли оно палиндромом и возвращает логическое значение.


def is_palindrome(text):
    result = ''
    for char in text:
      result = char + result
      
    if result == text:
        return True
    return False
print(is_palindrome('ass9sa'))

# Ответ
def is_palindrome(string):
    pointer1 = 0
    pointer2 = len(string) - 1
    while pointer2 - pointer1 > 0:
        if string[pointer1] != string[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True


# Alternative solution
#  def is_palindrome(string):
#      return string == string[::-1]

#lesson37
# Реализуйте функцию count_vowels(), которая принимает строку,
# считает и возвращает количество гласных букв в ней.
# Для проверки, является ли буква гласной,
# импортируйте и используйте функцию is_vowel() из модуля symbols.py.

from symbols import is_vowel


def count_vowels(text):
    result = 0
    for char in text:
        if is_vowel(char):
            result += 1
    return result

# Директория src в файловом дереве содержит модуль kit.py. Изучите его.

# Реализуйте функцию print_kit() и вызовите в ней все функции,
# которые определены в модуле kit.py.
# Предварительно импортируйте их.

import kit
def print_kit():
    print(kit.show_language())
    print(kit.say_hello())
    print(kit.say_bye())

# Реализуйте функцию choice_from_range(),
# которая принимает строку-набор и выбирает случайный символ по индексу из ограниченного диапазона.

from random import randint

def choice_from_range(text, start, finish):
    index = randint(start, finish)
    choice = text[index]
    return(choice)

#Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений)
#и возвращает пару, значения которой расположены строго в порядке возрастания.

# обратите внимание на скобки у аргумента функции
# sort_pair((5, 1)) == (1, 5)
# sort_pair((2, 2)) == (2, 2)
# sort_pair((7, 8)) == (7, 8)

def sort_pair (cortej):
    sort = tuple((sorted(cortej)))
    return(sort)