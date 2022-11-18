import random
name = "Tirion"
print("Hello, " + name + "!")
i = 0
while i < 5:
    number_1 = random.randint(0, 10)
    number_2 = random.randint(1, 10)
    op = random.choice(["+", "-", "*", "/"])
    exp = str(number_2) + op + str(number_2)

    print(f"What is result {exp}?")
    #print(eval(exp))
    answer = float(input())
    if answer == eval(exp):
        print("Correct")
    else:
        print("Incorect. Correct amswer is " + str(eval(exp)))
    i = i + 1