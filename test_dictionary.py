# d1 = {'a': 7, 'b':9}
# d2 = dict([[1,2],[3,4],[5,6]])
# d3 = dict.fromkeys([1,2,3,4,5], 'value')

# #d1.clear #очищает словарь
# d5 = d1.copy() #копия словаря
# print(d5)
# print(d1.items()) #возращает список из кортежей
# print(d1.keys()) #возращает ключи в словаре в виде списка
# print(d1.values()) #возращает значение в словаре
# d1.update(d2) #позваляет добавить значения из другого словаря
# print(d1)

# if 'c' in d1:
#     d1['c']

# y = d1.get('c')
# print(y)

price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

# # for i in price:
# #     print(i)

# for i in price:
#     price[i] = price[i] * 0.85

# new_price = {}
# for i in price:
#     new_price[i] =  round(price[i] * 0.85, 2)
for i in price.items():
    print(i)

for key, value in price.items():
    print(key)
    print(value)

# print(price)
# print(new_price)

