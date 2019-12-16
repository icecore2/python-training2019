# http://lifemichael.com/moodle/mod/assign/view.php?id=5188
# The module file can be copied to local "venv" directory: 'venv' > 'Lib' > 'site-packages' > 'math_utils_lesson'
# for testing this exception messages.

# Check if the module is from library or folder as backup.
try:
    from math_utils_lesson.math_utils_from_statement import multiplyof, sumof, differenceof

    print("Imported from venv/Lib folder.\n----------")
except ImportError:
    print("Imported from folder.")
    from archive.modules.module.math_utils_from_statement import multiplyof, sumof, differenceof

differenceOfNumbers = differenceof(4, 4)
print("differenceOfNumbers:", differenceOfNumbers)

multiplyOfNumbers = multiplyof(2, 2)
print("multiplyOfNumbers:", multiplyOfNumbers)

sumOfNumbers = sumof(2, 2)
print("sumOfNumbers:", sumOfNumbers)
