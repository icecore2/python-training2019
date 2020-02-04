# id=5170
"""
The following code should print out the details of all books the dict holds their details. You should complete the missing code.
 books = {
   123123: (123123  ,  "core php",122,39.9),
   234432: (234432  ,  "core java",242,49.9),
   893123: (893123  ,  "mongo in 8 days!",128,19.9),
   923123: (923123  ,  "scala now",522,34.9)
}

for ____ in books:
   (__,____,_____,____) = books[isbn]
   print(id,name,pages,price)
"""
books = {
    123123: (123123, "core php", 122, 39.9),
    234432: (234432, "core java", 242, 49.9),
    893123: (893123, "mongo in 8 days!", 128, 19.9),
    923123: (923123, "scala now", 522, 34.9)
}

for isbn in books:
    (id, name, pages, price) = books[isbn]

    print("Id:", id, "Name:", name, "Pages:", pages, "Price:", price)
    # print(id,name,pages,price)
    # print("Id:", id),   print("Name:", name),   print("Pages:", pages),   print("Price:", price)
