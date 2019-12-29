# http://lifemichael.com/moodle/mod/assign/view.php?id=5192

# Use the Python console in order to evaluate the value of each one of the following expressions.
# Before you start, make sure you create the following two sets:
#   a = [1,2,3]
#   b = [5,6,7]
#   c = [1,2,3,4,5,6,7,8,9]
# The expressions you should check their values are:
# a * 2
# b * 3
# 71/5
# 71//5
# 2 ** 3
# 4 ** 2
# a[1]
# b[2]
# a[0]
# c[2:7]

a = [1, 2, 3]
b = [5, 6, 7]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("a: ", a)
print("b: ",b)
print("c: ", c)

print("a * 2:", a * 2)
print("b * 3:", b * 3)
print("71 / 5:", 71 / 5)
print("71 // 5:", 71 // 5)  # Floor division
print("2 ** 3:", 2 ** 3)
print("4 ** 2:", 4 ** 2)
print("Index a[1]:", a[1])  # Index 2
print("Index b[2]:", b[2])  # Index 3
print("Index a[0]:", a[0])  # Index 0
print("Index c[2:7]:", c[2:7])  # Not includes the index 7 (c[7] == 8)
