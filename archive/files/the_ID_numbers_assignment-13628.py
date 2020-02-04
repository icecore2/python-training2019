# id=13628
# TODO: files - assignment not finished.
# Create a file that includes ID numbers. Each row includes a specific ID number.
# ID numbers might repeat themselves.
# Write a short program that reads the ID numbers from the file and prints them to the screen.
# Your short program should use the Set collection in order to avoid printing the same ID number more than once.

from os import path as path

file_location = path.dirname(__file__)

ids = ['2412414142',
       '2324214222',
       '6896959699',
       '6574653437',
       '2324214222',
       '6856587578',
       '4846746768',
       ]

def fileCreations(studentIds):
    f = open(file_location + 'studentsIDs.txt', 'w')
    f.writelines(studentIds)
    print(idNumbers)
    f.close()

def fileToRead():
    f = open(file_location + 'studentsIDs.txt', 'r')
    for linesToRead in f.readlines():
        studentIdsSet = linesToRead
        studentIds = set(studentIdsSet)
        print(studentIds)
    f.close()

fileCreations(ids)

fileToRead()