# http://lifemichael.com/moodle/mod/assign/view.php?id=14043

# You should develop a simple application that prints out the current exchange rates of all currencies Bank Israel
# can provide us with their exchange rates.
# You can find all currencies' exchange rates at https://www.boi.org.il/currency.xml it is recommended
# to download the "currency.xml" file manually and save it in your project.

from xml.dom import minidom as minidom
from os import path

file_location = path.dirname(__file__)  # This is the working file location

workingFile = minidom.parse(file_location + "/currency.xml")  # File to work on

document = workingFile.getElementsByTagName('CURRENCIES')
document.getElementsByTagName('CURRENCY')
mapping = {}

print(document)
