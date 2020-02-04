# id=13540

# Develop a simple script that includes the definition of the average function.
# The average function should receive the marks of all students packed in a dict object and
# then calculate their average and return it.
# Calling the average function should look as in the following code snippet:
# result = average(david=82, avi=90, ronen=78, galit=92)


# The average function
def average(david, avi, ronen, galit):
    studentsMarks = {david, avi, ronen, galit}
    result = 0
    for averageScore in studentsMarks:
        result = result + averageScore
        print("Result inside the loop:", result)
    return result / len(studentsMarks)


# The function call with default values of variables
result = average(david=82, avi=90, ronen=78, galit=92)

print("Returned result of average:", result)
