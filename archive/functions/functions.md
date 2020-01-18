#### Attributes

The variables of the object. **Example:**

```python
def sum(a,b):
    c = a + b
    return c
sum.version = 101
sum.author = "haim michael"
sum.priority = 3
print(sum.author)
```

output: `haim michael`

#### Variables Scope

This trick caller also `LEGB Rule`

| Letter | Meaning   | Keyword  |
|:-------|:----------|:---------|
| L      | local     |          |
| E      | enclosing | nonlocal |
| G      | global    | global   |
| B      | built-in  |          |
**Example:**

```python
number = 4  # global

def a():
    number = 3  # enclosing
    def b():
        number = 2  # local
        print(number)
    b()
a()
```

#### Arguments

* References passed to the function
* Assigning new references **Example:**

```python
def doSomething(firstParameter, secondParameter):
    # do something

firstParameter= 0
secondParameter= 1

doSomething(firstParameter, secondParameter)
```

#### Sequence Returned Value

* Define a function that returns a tuple, or any other sequence type.

**Example:**

```python
def f(a,b):
    numA = 2 * a
    numB = 2 * b
    return [numA,numB]
x = f(3,5)
print(x)
```

#### The `func(*name)` Syntax

* function will be capable of unpacking the passed argument into
  discrete separated parameters

**Example:**

```python
def f(x1,y1,x2,y2):
    return (y2-y1)*(y2-y1)+(x2-x1)*(x2-x1)
ob = [0,0,4,3]
num = f(*ob)
print(num)
```
