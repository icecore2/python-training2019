# http://lifemichael.com/moodle/mod/assign/view.php?id=13539
# Develop a simple script that includes the definition of the average function.
# The average function has four parameters: math, physics, chemistry, and history.
# The average function should receive the marks in these four subjects and return their average.
# You should include the required code for calculating David's average.
# David's marks (90 in math, 92 in physics, 80 in chemistry and 70 in history)
# should be passed over packed in a dict object.

marks_dict = {"david": {'math': 90, 'physics': 92, 'chemistry': 80, 'history': 70},
              "dima": {'math': 90, 'physics': 92, 'chemistry': 80, 'history': 70},
              "haim": {'math': 90, 'physics': 92, 'chemistry': 80, 'history': 70},
              "gani": {'math': 90, 'physics': 92, 'chemistry': 80, 'history': 70},
              }
print(marks_dict['david'])
math, physics, chemistry, history = marks_dict['david'].values()

def average(math, physics, chemistry, history):
    average = (math + physics + chemistry + history) / 4
    print(average)
    return average()

pix = b'slfskflksflkg'
print(type(pix))
print(pix)