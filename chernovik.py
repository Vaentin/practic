from random import randint


def choice_from_range(text, start, finish):
    index = randint(start, finish)
    choice = text[index]
    print(choice)


text = "abcdefghij"
choice_from_range(text, 6, 8)