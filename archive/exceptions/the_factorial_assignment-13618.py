# http://lifemichael.com/moodle/mod/assign/view.php?id=13618

# Define the FactorialException class. It should extend Exception. Define the factorial function. Whenever the
# factorial function receives a number for which it is not possible to calculate factorial (number smaller than 0) an
# exception should be thrown. It should be of the FactorialException type.
# Check your definition for the factorial function by calling it passing over a negative number.


# Empty class that considered as "type" of exception
class FactorialException(Exception): pass


def factorial(num):
    if num < 0:
        raise FactorialException
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result


try:
    temp = factorial(4)
    print(temp)

    temp = factorial(-3)
    print(temp)


except:
    print("Basa")
