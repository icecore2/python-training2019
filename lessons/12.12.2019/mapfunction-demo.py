number1 = [2, 3, 5, 1, 66, 7, 4]


def f(price):
    return price / 3.5


number2 = map(f, number1)

print(number2)
print(type(number2))
