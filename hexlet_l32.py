
# def join_numbers_from_range(start,finish):
#     result = ''
#     i = start
#     while i <= finish:
#       result = result + str(i)
#       i += 1
#     return result

# print(join_numbers_from_range(5, 10))

def join_numbers_from_range(start, stop):
    result = ''
    # index = start
    while start <= stop:
      result += str(start)
      start += 1
    return result

print(join_numbers_from_range(1, 1)) # '1'
print(join_numbers_from_range(2, 3))  # '23'
print(join_numbers_from_range(5, 10))  # '5678910'

