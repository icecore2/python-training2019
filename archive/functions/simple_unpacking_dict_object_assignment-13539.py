# http://lifemichael.com/moodle/mod/assign/view.php?id=13539

# Develop a simple script that includes the definition of the average function.
# The average function has four parameters: math, physics, chemistry, and history.
# The average function should receive the marks in these four subjects and return their average.
# You should include the required code for calculating David's average.
# David's marks (90 in math, 92 in physics, 80 in chemistry and 70 in history)
# should be passed over packed in a dict object.

# The name we are looking for
studentName = 'david'

# All students grades
studentsScores = {
    'david': ({'math': 90, 'physics': 92, 'chemistry': 80, 'history': 70}),
    'dima': ({'math': 62, 'physics': 93, 'chemistry': 79, 'history': 79}),
    'dana': ({'math': 50, 'physics': 90, 'chemistry': 99, 'history': 63}),
    'daniel': ({'math': 66, 'physics': 90, 'chemistry': 99, 'history': 63}),
}


def average(math, physics, chemistry, history):
    averageScore = math + physics + chemistry + history
    print(averageScore / 4)


# Unpacking 'studentsScores'
math, physics, chemistry, history = studentsScores[studentName].items()

# The function that calculates the average
average(math[1], physics[1], chemistry[1], history[1])
