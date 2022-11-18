#x = (9, 8, 7)
x = (9, 8, 7, 6, 5, 4, 3)
y = []

for i in range(len(x)):
    y.append(x[i] + 3)
print(x)
print(y)

t = list(x)
t[0] = 10
x = tuple(t)
print(x)

h = (1,2,3)
h += (4,5)
print(h)
#z, c, b = x
#print(z + c + b)

#y = tuple('stroka')
#print(y)
#print(type(x))

r = 5
u = 7
r, u = (u, r)

#print(x[1:2])
