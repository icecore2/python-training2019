# id=5155

# The following program should receive an input from the user.
# The input should be a number. The program prints the number binary representation.
# You should complete the missing code.
# number = input("please enter a number:")
# result = ____________
# print("the binary representation is %s" % result)

def digits(number):
    result = number
    if not result.isdigit():
        print("Please insert a number only!")
    else:
        result = int(number)
        # print("the binary representation is")
        print("Type of is: {0}".format(type(result)))
        print("Binary: {0:b} (Base 2)".format(result))
        print("Decimal: {0:d} (Base 10)".format(result))
        print("Octa: {0:o} (Base 8)".format(result))
        print("Hex: {0:x} (Base 16)".format(result))
        print("===============================")


number = input("Note: Only numbers allowed.\nPlease enter a number:")
digits(number)

# print("the binary representation is %s" % result)
