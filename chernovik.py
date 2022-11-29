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


# text = 'If I look forward I win'
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win



