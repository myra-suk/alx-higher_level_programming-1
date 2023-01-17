# Python - Almost a circle

In this project I learnt about:
* Import
* Exceptions
* Class
* Private Attribute
* Getter/setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/write file
* args and kwargs
* Serialization/ Deserialization
* Java Script Object Notation

## Tests:heavy_check_mark:
* This set of tests were used to validate the code [main-tests](./main-tests) 
* Unittest folder: [./tests](./tests/test_models)

## Learning Objectives
```
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
```

| Files | Prototypes |
| --- | --- |
| `base.py`| `def __init__(self, id=None):`|
| `rectangle.py`| |
| `square.py` | |
| `test_base.py` | |
| `test_square.py` | |
| `test_rectangle.py` | |

### Tasks
* **1. Base class**
	* [base.py](./models/base.py): Write a first Class Base
	```
	Class Base:
	* private class attribute __nb_objects = 0
	* class constructor: def __init__(self, id=None)::
        	* if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
        	* otherwise, increment __nb_objects and assign the new value to the public instance attribute id
	```
* **2. First Rectangle**
	* [rectangle.py](./models/rectangle.py): Write a class Rectangle that inherits from Base:
	```
	Class Rectangle:
	1) Private instance attributes, each with its own public getter and setter:
	* __width -> width
	* __height -> height
	* __x -> x
	* __y -> y

	2) Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
 	```



