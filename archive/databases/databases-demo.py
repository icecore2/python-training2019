import pymysql.cursors
# connect with the database
connection = pymysql.connect(host='localhost',user='haim',password='michael',db='haim',charset='utf8',port=8889,cursorclass=pymysql.cursors.DictCursor)
try:
with connection.cursor() as cursor:
# creating a new record
    sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"cursor.execute(sql, ('haimm', '12345'))