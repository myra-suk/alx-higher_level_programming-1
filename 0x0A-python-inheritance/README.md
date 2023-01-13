# 0x0A. Python - Inheritance

In this Project I learnt and tested my understanding of Single and Multiple Inheritance concept in Python OOP Programming

## Tests:heavy_check_mark:

* [tests](./tests): Test files for the project

## Learning Objectives
```
* Why Python programming is awesome
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use isinstance, issubclass, type and super built-in functions
```

Function Prototypes:
| File | Prototype |
|--- | --- |
| `0-lookup.py` | `def lookup(obj)` |
| `1-my_list.py` | `def print_sorted(self)` |
| `2-is_same_class.py` | `def is_same_class(obj, a_class)` |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class)` |
| `4-inherits_from.py` | `def inherits_from(obj, a_class)` |
| `5-base_geometry.py` | `class BaseGeometry()` |
| `6-base_geometry.py` | `def area(self)` |
| `7-base_geometry.py` | `def integer_validator(self, name, value)` |
| `8-rectangle.py` | `def __init__(self, width, height)` |
| `9-rectangle.py` | `def __init__(self, width, height)` |
| `10-square.py` | `def __init__(self, size)` |
| `11-square.py` | `def __init__(self, size)` |


## Tasks
* **0. Lookup**
	* [0-lookup.py](./0-lookup.py): Returns the list of attributes and mmethods of an object
	* Returns  a list object
* **1. My list**
	* [1-my_list.py](./1-my_list.py): A class myList that inherits from a list
	* Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
* **2. Exact same object**
	* [2-is_same_class.py](./2-is_same_class.py): Returns True if the object is exactly an instance of the specified class ; otherwise False.
* **3. Same class or inherit from**
	* [3-is_kind_of_class.py](./3-is_kind_of_class.py): Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
* **4. Only sub class of**
	* [4-inherits_from.py](./4-inherits_from.py): Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
* **5. Geometry module**
	* [5-base_geometry.py](./5-base_geometry.py): Creates an empty class BaseGeometry
* **6. Improve Geometry**
	* [6-base_geometry.py](./6-base_geometry.py): Write a class BaseGeometry (based on 5-base_geometry.py).
* **7. Integer validator**
	* [7-base_geometry.py](./7-base_geometry.py): Write a class BaseGeometry (based on 6-base_geometry.py).
* **8. Rectangle**
	* [8-rectangle.py](./8-rectangle.py): Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
* **9. Full rectangle**
	* [9-rectangle.py](./9-rectangle.py): Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
* **10. Square #1**
	* [10-square.py](./10-square.py): Write a class Square that inherits from Rectangle (9-rectangle.py):
* **11. Square #2**
	* [11-square.py](./11-square.py): Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
* **12. My integer**
	* [100-my_int.py](./100-my_int.py): Write a class MyInt that inherits from int
