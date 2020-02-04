# id=5160

# Create a list that holds Fraction objects that represent ½, ¾, ⅝ and ⅞. Create a copy for that list by calling the
# copy() function. Change the first fraction in the new list and print the first list to the screen. You should
# expect to see the original list.

import fractions

fraction = fractions.Fraction

list_of_fraction = [fraction(1, 2), fraction(3, 4), fraction(5, 8), fraction(7, 8)]


def copy(fractions_copy_list):
    new_fraction_list = fractions_copy_list.copy()  # Copy of old list
    new_fraction_list[0] = fraction(1, 3)  # Change value at index 0
    return new_fraction_list


fraction_copy = copy(list_of_fraction)

print("Original fraction list:")
print(list_of_fraction)

print("Copy fraction list:")
print(fraction_copy)
