# id=5158

# Develop a simple program that receives from the user a short text and a filename the user wants the program to
# create and write the text into it.

from os import path as path

# file_location = path.absolute(__file__)
file_location = path.dirname(__file__)

# This method is creating a file and writed something inside.
#     Params:
#          file_location = at location of 'file_location'

fileExtention = ".txt"
fileName = "file_test"
fileContent = "the text"
linesToWrite = 12
numberOfFiles = 2


def fileWriter(filename, text, times):
    onlylocation = file_location
    # This line can be written in another way: f = open(file_location + "/" + filename, "w+")
    f = open(onlylocation + ("/{0}{1}".format(filename, fileExtention)), "w+")
    for i in range(times):
        f.write(f"This is line {i + 1} - {text}\n")
    f.close()
    return print(f"The file:{f.name} written successfully.")


# TODO: Fix the bug with number of file to create.
try:
    # fileWriter(fileName, fileContent, linesToWrite)
    fileWriter(fileName, fileContent, linesToWrite)
    if numberOfFiles > 1:
        for n in range(numberOfFiles):
            fileWriter(fileName + "-" + str(n), fileContent + str(n), linesToWrite)
except:
    print("Unable to write the file.")
    IndexError.with_traceback(fileWriter(fileName + numberOfFiles, fileContent + numberOfFiles, linesToWrite))


def filenames(filename):
    result_filename = filename
    print(result_filename)
    return result_filename


printfilename = ("Location of files: " + file_location)
print(printfilename)
