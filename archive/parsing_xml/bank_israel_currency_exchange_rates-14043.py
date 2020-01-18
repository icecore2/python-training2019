# http://lifemichael.com/moodle/mod/assign/view.php?id=14043
"""Lesson example:
for nodeBook in document.getElementsByTagName("book"):
    isbn = nodeBook.getAttribute("isbn")
    titles = nodeBook.getElementsByTagName("title")
    for nodeTitle in titles:
        nodeText = nodeTitle.firstChild
        title = nodeText.data
        mapping[isbn] = title

print(mapping)
"""
# You should develop a simple application that prints out the current exchange rates of all currencies Bank Israel
# can provide us with their exchange rates.
# You can find all currencies' exchange rates at https://www.boi.org.il/currency.xml it is recommended
# to download the "currency.xml" file manually and save it in your project.

from xml.dom import minidom as minidom
from os import path

file_location = path.dirname(__file__)  # This is the working file location

document = minidom.parse(file_location + "/currency.xml")  # File to work on
# currencies = document.getElementsByTagName('CURRENCIES')

mapping = {}


def homeWorkFunc():  # Not working
    print(document)
    for currency in document.getElementsByTagName("CURRENCIES"):
        tempMapping = currency.getElementsByTagName("CURRENCY")
        for nodeName in tempMapping:
            currencyName = currency.getElementsByTagName("NAME")
            currencyRate = currency.getElementsByTagName("RATE")
            nodeText = nodeName.firstChild
            print("nodeText.data: ", nodeText.data)
            print("currencyRate: ", currencyRate.firstChild)
            print("currencyName: ", currencyName.firstChild)

            currName = nodeText.data
            mapping[nodeName] = nodeText
        # currencyName = currency.getElementsByTagName("CURRENCY")
        # currencyRate = currency.getElementsByTagName("RATE")

        #     nodeText = nodeTitle.firstChild
        #     title = nodeText.data
        #     mapping[isbn] = title
    print(mapping)


# homeWorkFunc()

def classSolution():
    '''This solution used with:
    * map
    * zip
    * lambda
    '''
    codes1 = document.getElementsByTagName("CURRENCYCODE")  # Finding by element the Tag name
    rates1 = document.getElementsByTagName("RATE")  # Finding by element the Tag name
    codes2 = map(lambda ob: ob.firstChild.data, codes1)  # Mapping the firstChild from 'codes1' to 'codes2'
    rates2 = map(lambda ob: ob.firstChild.data, rates1)  # Mapping the 'firstChild' from 'rates1' to 'rates2'

    tuples = zip(codes2, rates2)  # Zipping the values of 'codes2' and 'rates2' to 'tupels' variable

    # Create a loop for display all the rates in 'tupels' variable.
    for tpl in tuples:
        print(tpl)


classSolution()
