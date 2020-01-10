class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

class Mark:
    def __init__(self, subject, mark):
        self.subject = subject
        self.mark = mark


students = dict()

with open("dara.csv", "r"):
    line = input.readlines()
    for line in lines:
        texts = line.split(",")
        if text[0] in students:
            students[texts[0]].marks.append(Mark(texts[3], texts[2]))