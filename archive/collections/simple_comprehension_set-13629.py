# http://lifemichael.com/moodle/mod/assign/view.php?id=13629

# Develop a simple program that creates the following comprehension sets based on following ones:
# {1,2,3,4}      ====>   {10,20,30,40}
# {'a','b','c'}  ====>   {'aaa','bbb','ccc'}
# {100,200,300}  ====>   {1,2,3}

def numberSet():
    # numberSet = {1,2,3,4}  ====> <class 'set'>
    number_set = {1, 2, 3, 4}  # <class 'set'>
    comprehension_set = sorted({n * 10 for n in number_set})
    print("numberSet: ", comprehension_set)


def lettersSet():
    letter_set = {'a', 'b', 'c'}
    comprehension_set = {n * 3 for n in letter_set}
    print("lettersSet:", comprehension_set)


def bigNumberSet():
    number_set = {100, 200, 300}
    comprehension_set = sorted({int(n / 100) for n in number_set})
    print("bigNumberSet:", comprehension_set)


numberSet()

lettersSet()

bigNumberSet()
