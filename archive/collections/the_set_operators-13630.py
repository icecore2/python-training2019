# http://lifemichael.com/moodle/mod/assign/view.php?id=13630
# Additional link: https://data-flair.training/blogs/python-operator/

# Given the following two sets:
# one = {'a','b','c','d','e','f','g','h'}
# two = {'a','d','g'}
#
# Calculate the value of each one of the following expressions:
# 'a' in one
# one – two (Difference)
# one | two (Union)
# one & two (Intersection)
# one ^ two (Difference)
# set('bcd') < one (Subset of another set)
# set('abcde') > one (Superset of another set)

# Global sets
one = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
two = {'a', 'd', 'g'}


# Assignment Operator
def minusSet(): return print("minusSet:", one - two)


def unionSet(): return print("orSet:", one | two)


def andSet(): return print("andSet:", one & two)


def xorSet(): return print("xorSet:", one ^ two)


def setRemove(): return print("setRemove:", set('bcd') < one)


def setAdd(): return print("setAdd:", set('abcde') > one)


print("Set 'one' is: {}".format(one))
print("Set 'two' is: {}".format(two))

minusSet()  # difference between two sets
unionSet()  # union of two sets
andSet()  # intersection between two sets
xorSet()  # Difference between two sets
setRemove()  # subset of another set
setAdd()  # superset of another set
