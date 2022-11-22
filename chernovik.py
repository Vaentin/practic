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

