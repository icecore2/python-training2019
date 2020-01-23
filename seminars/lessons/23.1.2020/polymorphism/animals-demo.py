# PDF - page 16

class Dog:
    def __init__(self,str):
        self.name = str

    def hello(self):
        print("hau hau")


class Cat:
    def __init__(self,str):
        self.name = str

    def hello(self):
        print("miau miau")


class Cow:
    def __init__(self,str):
        self.name = str

    def hello(self):
        print("moo moo")


animals = [Cow("Metilda"), Dog("Doberman"), Cat("Mitzi"), Cow("Shula")]
for animal in animals:
    print("Animal noise:"), animal.hello()
    print("Name:", animal.name)
