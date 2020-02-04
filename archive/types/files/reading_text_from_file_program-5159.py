# id=5159

# Develop a simple program that receives from the user the name of a textual file, reads its content and prints it to
# the screen.

import os.path

path = os.path

file_location = path.dirname(__file__)

f = open(file_location + "\\file_test2.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)
else:
    print("File issue.")
print(f.read())
f.close()
