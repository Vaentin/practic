x = 5

if x == 0:
	x = 1
	print ('x был равен нулю')

elif type(x) == type(1) or type(x) == type(1.5):
	print ('x допустимое значение')

else:
	print('В x недопустимый тип данных')
	x = 1
 
 
print (100/x)
