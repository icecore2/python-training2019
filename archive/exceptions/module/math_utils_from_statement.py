# http://lifemichael.com/moodle/mod/assign/view.php?id=5188
# Define the utils module with the following functions: sumof, multiplyof and differenceof.
# Each one of these three functions is capable of receiving two arguments and return the calculation of their
# sum, multiplication or difference.
# Define a separated module where you will use the utils' functions. Use the 'from' statement in that other module.

# Functions

def multiplyof(firstNumber, secondNumber):
    result = firstNumber * secondNumber
    return result


def differenceof(firstNumber, secondNumber):
    if firstNumber < secondNumber:
        print("(First number is bigger)")
        result = secondNumber - firstNumber
    else:
        print("(Second number is bigger)")
        result = firstNumber - secondNumber
    return result


def sumof(firstNumber, secondNumber):
    result = firstNumber + secondNumber
    return result
