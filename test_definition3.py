def name(h, g=5, *args, k):  #*a переводит в кортеж
    print(h)
    print(g)
    print(args)
    print(k)
    
name(1,2,3, k=10)

print('Вторая часть')

def exclusive_item(*args):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    return new_list

z = [9,8,7]
x = [8,8,9,7,6,5]
c = [1,2,3,4,5,6,7,7]

t = exclusive_item()
print(t)

