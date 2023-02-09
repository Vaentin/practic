# if else
password1, password2 = input(), input()

if password1 == password2:
    print('Пароль принят')
else:
    print("Пароль не принят")

#сумма первой и последней цифр равна разности второй и третьей цифр.
num = int(input())
if (num // 1000 + num % 10) == (num % 1000 // 100 - num % 100 // 10):
    print("ДА")
else:
    print("НЕТ")
