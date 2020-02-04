# id=13975

# You should develop a short program that creates a list that includes the following numbers:  12, 15 and 18.
# Your code should calculate the average of all numbers the list includes, and print it to the screen.

list_of_numbers = (10, 20)
index = 0
average_list = 0

for i in list_of_numbers:
    print(list_of_numbers[index])

    average_list += list_of_numbers[index]
    index += 1

print((int)(average_list / len(list_of_numbers)))
