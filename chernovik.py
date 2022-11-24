
# Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины.
# Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа:


def my_substr(string, index_string):
  
  sub_string = ''
  while len(sub_string) < index_string:
    sub_string = string[:index_string]

  
    return sub_string 


  
  


string = 'If I look back I am lost'
print(my_substr(string, 1))  # => 'I'
print(my_substr(string, 7))  # => 'If I lo'
