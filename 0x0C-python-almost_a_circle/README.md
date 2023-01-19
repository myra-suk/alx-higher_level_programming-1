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
* **1. Base class.py**
	* [base.py](./models/base.py):
	* Write a first class ``base``
	* Update the class Base by adding the class method ``def save_to_file(cls, list_objs):`` that writes the JSON string representation of list_objs to a file:
	* Update the class ``Base`` by adding the static method ``def from_json_string(json_string):`` that returns the list of the JSON string representation json_string:
	* Update the class ``Base`` by adding the class method ``def create(cls, **dictionary):`` that returns an instance with all attributes already set:
	* Update the class ``Base`` by adding the class method ``def load_from_file(cls):`` that returns a list of instances:
	* Update the class ``Base`` by adding the class methods ``def save_to_file_csv(cls, list_objs):`` and ``def load_from_file_csv(cls):`` that serializes and deserializes in CSV:


 	
* **Rectangle.py**
	* [rectangle.py](./models/base.py):
	* Write a class ``Rectangle`` that inherits from Base
	* Update the Class ``Rectangle``by adding all setter methods and instantiation
	* Update the class by adding the public method ``def area(self):`` that returns the area of the Rectangle instance
	* Update the class ``Rectangle`` by adding the public method ``def display(self):`` that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
	* Update the class ``Rectangle`` by overriding the __str__ method so that it returns ``[Rectangle] (<id>) <x>/<y> - <width>/<height>``
	* Update the class ``Rectangle`` by improving the public method ``def display(self):`` to print in stdout the ``Rectangle`` instance with the character # by taking care of x and y
	* Update the class ``Rectangle`` by adding the public method ``def update(self, *args):`` that assigns an argument to each attribute:
	* Update the class ``Rectangle`` by updating the public method ``def update(self, *args):`` by changing the prototype to update ``(self, *args, **kwargs)``  that assigns a key/value argument to attributes:
	* Update the class ``Rectangle`` by adding the public method ``def to_dictionary(self):`` that returns the dictionary representation of a ``Rectangle:``

* **Square.py**
	* [square.py](./models/square.py)
	* Write a class ``Square`` that inherits from the class ``Rectangle``
	* Update the class ``Square`` by adding the public getter and setter ``size``
	* Update the class ``Square`` by adding the public method ``def update(self, *args, **kwargs)`` that assigns attributes:
	* Update the class ``Square`` by adding the public method ``def to_dictionary(self):`` that returns the dictionary representation of a ``Square``
