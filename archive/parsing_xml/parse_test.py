
from xml.dom import minidom
from os import path

file_location = path.dirname(__file__)  # This is the working file location

file = minidom.parse(file_location + "/currency.xml")  # File to work on

mapping = {}

'''
def failedTry():
    for nodeCurrencies in file.getElementsByTagName("CURRENCIES"):
        currency = nodeCurrencies.getElementsByTagName("CURRENCY")
        print(currency)
        # for nodeStats in currency:
        #     nodeResult = nodeStats.firstChild
        #     currencyData = nodeResult.data
        #     mapping[currency] = currencyData

    print(mapping)

failedTry()
'''

def failedTry():
    currency = file.getElementsByTagName("CURRENCY")
    rate = file.getElementsByTagName("RATE")
    for nodeCurrencies in file.getElementsByTagName("CURRENCIES"):
        # currency = nodeCurrencies.getElementsByTagName("CURRENCY")

        print(currency)
        # for nodeStats in currency:
        #     nodeResult = nodeStats.firstChild
        #     currencyData = nodeResult.data
        #     mapping[currency] = currencyData

    print(mapping)

failedTry()