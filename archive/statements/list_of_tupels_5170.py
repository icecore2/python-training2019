# http://lifemichael.com/moodle/mod/assign/view.php?id=5169
# The following code should print out the details of all
# books the list holds their details as tuples. You should complete the missing code.
books = [
    (123123, "core php", 122, 39.9),
    (234432, "core java", 242, 49.9),
    (893123, "mongo in 8 days!", 128, 19.9),
    (923123, "scala now", 522, 34.9)
]

for (id, name, pages, price) in books:
    print(id, name, pages, price)
