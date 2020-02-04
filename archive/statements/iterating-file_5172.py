# id=5172
# The file names.txt includes persons names. You should
# complete the missing code of the following program in order to print out each one of the names in a separated line.
# The names are already in separated lines inside names.txt.

import os

file_location = os.path.dirname(__file__)

ob = open(file_location + '\\text_files\\names.txt')

line_number = None
for line_number, the_text in enumerate(ob):
    print("{}:{}".format(line_number, the_text))
