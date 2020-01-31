# Object Oriented Programming in Python
## Date: Thursday, January 23th 2020

### Topics
#### Introduction
* Magic functions
* type of `class`.    

# Example Class
```Python
    class TestClass:
        pass
    print(type(TestClass))  # Print: class 'type'
    # Example Number
    print(type(1))  # Print: class 'int'
```
* Inhetitance
    * super()
        * super() with Single Inheritance
```Python
class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')
d1 = Dog()
```

    * __init__
        * It is known as a constructor in object oriented concepts

```Python
class testClass:
        def __init__(self, w, h):
            self.width = w
            self.height = h
        def area(self):
            return self.width * self.height
```

* Links:
    * [Understanding self and __init__ method in python Class](https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/)
    *
* Polymorphysm

### Lesson assignments
* [Rectangle](/seminars/lessons/23.1.2020/rectangle/rectangle.py)
* [Parallel lines](/seminars/lessons/23.1.2020/parallel_lines)
* [Student - person](/seminars/object_oriented)

### Notes
* first parameter is `self` inside the `def` when function is in the class.
* `__init__` variables must to be dynamic
* class name `Person(Inherited)`
* `super()` - usage of the inherited class, example:

`super().__init__(var1, var2)`
  * the `super()` is imported to use because it's a must to split and
stay organised which is inherited or not.
*
