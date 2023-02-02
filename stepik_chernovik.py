s = input().lower()
s = s.replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')
s ='.'.join(s)
print('.'+ s)