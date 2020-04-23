from abc import ABC, abstractmethod, abstractclassmethod

from pymongo import MongoClient

client = MongoClient()
db = client.webstore
products = db.products

'''
Getting a Collection - https://www.mongodb.org/display/DOCS/Collections


    def __init__(self, product):
        product_name = "Polo T shirt"

    product_creationdate = "01.01.2020"
    product_price = 59.99

    def init(self, product_name, product_creationdate, product_price):
        self.product_name = product_name
        self.product_creationdate = product_creationdate
        self.product_price = product_price
'''


@abstractclassmethod
class AbstractDBDAO(ABC):

    @abstractmethod
    def insertOne(self):
        return

    @abstractmethod
    def deleteOne(self):
        return

    @abstractmethod
    def updateOne(self):
        return

    @abstractmethod
    def replaceOne(self):
        return

    @abstractmethod
    def addProduct(self):
        return


class Product:
    def __init__(self, productID, productName, productPrice):
        self.productID = productID
        self.productName = productName
        self.productPrice = productPrice


class MongoDBDAO(AbstractDBDAO):

    def productInsert(self, product):

# product = Product({"id": 123, "name": 'carpeta', "price": 99})
# result = products.find_one({"id": 123})
#
# print(result)
# print(type(result))


# products.insert_one({"id":123,"name":'carpeta',"price":99})
# result = products.find_one({"id":123})
# print(result)
# print(type(result))

MongoDBDAO.insertOne()
