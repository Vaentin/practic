# Реализуйте функцию join_numbers_from_range(), 
# которая объединяет все числа из диапазона в 
# строку и возвращает получившуюся строку:

def join_numbers_from_range(num_start, num_finish):
  i = 0
  result = ""

  while i <= num_finish:

    result += i
    
