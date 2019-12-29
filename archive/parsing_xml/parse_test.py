from xml.dom import minidom
from os import path

file_location = path.dirname(__file__)  # This is the working file location

file = minidom.parse(file_location + "/currency.xml")  # File to work on

mapping = {}


def failedTry():
    for nodeCurrencies in file.getElementsByTagName("CURRENCIES"):
        currency = nodeCurrencies.getElementsByTagName("CURRENCY")
        for nodeStats in currency:
            nodeResult = nodeStats.firstChild
            currencyData = nodeResult.data
            mapping[currency] = currencyData

    print(mapping)

# failedTry()
