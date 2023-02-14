a, b = int(input()), int(input())
s = input() 
if s == "/" and b ==0:
    print("На ноль делить нельзя!")
elif  s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
elif s == "/":
    print(a / b)
else:
    print("Неверная операция")
    