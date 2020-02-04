# id=14005
# You should develop a short program that creates a list of tuples.
# Each tuple should represent a specific student.
# Each tuple should hold the 'firstname', 'lastname', 'id' and 'average' (of the specific student that tuple represents).
# You should create a comprehension list of the averages of all students.
MINIMUM_SCORE = 80
students_list = [(123123, "Dima", "Banny", 29),
                 (123124, "John", "Travolta", 89),
                 (123125, "Dima", "Bilan", 99),
                 (123126, "Avner", "Levi", 99)]

new_average_list = []  # Empty list

new_average_list += [average_scores[3] for average_scores in students_list if average_scores[3] >= MINIMUM_SCORE]
# print(new_average_list)
result = 0

for n in new_average_list:  # Variable 'n' holds the 'item' when loop performed
    result += n / len(new_average_list)

print("Scores from students:", new_average_list)
print("Average scores result:", int(result))
