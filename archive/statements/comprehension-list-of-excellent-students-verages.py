# id=14005
"""
You should develop a short program that creates a list of tuples.
Each tuple should represent a specific student.
Each tuple should hold the 'firstname', 'lastname', 'id' and 'average' (of the specific student that tuple represents).
You should create a comprehension list of the averages of all excellent students.
An excellent student is a student with an average higher than 89.
"""

MINIMUMSCORE = 89

studentstupel = [(1234, "firstname", "lastname", 70),
                 (1235, "firstname2", "lastname2", 80),
                 (1236, "firstname3", "lastname3", 90),
                 (1237, "firstname4", "lastname4", 100)]
#a_list = [1, ‘4’, 9, ‘a’, 0, 4]
#squared_ints = [ e**2 for e in a_list if type(e) == types.IntType ]

averages = [excellent for excellent in studentstupel if excellent[3] >= MINIMUMSCORE ]
for scores in averages:
    thescores = scores[3]
    print(thescores)
# id, firstname, lastname, scores = averages
