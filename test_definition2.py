
# def count_list(par):  #parametr
#     count = 0
#     for i in par:
#         count += 1
#     return count


# j = [9, 8, 7, 6]

# print(count_list(j)) #argument

# h = ['a', 'a', 'h']

# print(count_list(h))

# k = [9, 8, 7, 5, 7, 5]

# print(count_list(k))

# print(count_list("strochka"))

######################################################

# def count_list(par, count = 0):  #parametr
    
#     for i in par:
#         count += 1
#     return count
# f = [9, 7, 6, 5, 2, 2]
# print(count_list(f))

# print(count_list(f, -1))

#######################################################
def count_list(par, par2 = False, count = 0):  #parametr
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ

    else:        
        for i in par:
            count += 1
        return count
f = [9, 7, 6, 5, 2, 2]

#Можно передать параметры в функцию
#print(count_list(f))

print(count_list(f, count=-1)) 

print(count_list(f, -1))

print(count_list(f, True, -1))

#Можно распаковать на переменные

h, p = count_list(f, True)
print(h)
print(p)
