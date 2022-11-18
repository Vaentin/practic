#m = [['perviy', '2'], [2], 1, 3,]
#
#m[0] = 9
#m[0] = m[0] + 2
#print([m])
#print(len(m))
#
#n = list(range(10))
#
#for i in n:
#    print(i)

x = [9, 8, 7, 6, 5]
x.append(4) 
x.insert(1, 7)
print(x.count(7))
x.sort()
x.reverse()
y = x.pop(0) #удаляет по индексу

print(y)
x.remove(7) #удаляет конкретный елемент
x.clear()
x.extend(['a', "s"]) #добовляет в конец элементы списка
h = x.copy()
print(x)
print(h)