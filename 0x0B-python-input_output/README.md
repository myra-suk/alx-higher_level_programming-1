# Python - Input/Output

In this project I learnt and tested Input/Output Concepts in Python Programming

## Tests:heavy_check_mark

[tests](./tests): A set of tests that verified the code

## Learning Objectives

* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

### Example
```
vagrant@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

vagrant@ubuntu:~/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!
vagrant@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!

```
| Files | Prototypes |
| --- | --- |
| `0-read_file.py` | `def read_file(filename="")` |
| `1-write_file.py` | `def write_file(filename="", text="")` |
| `2-append_write.py` | `def append_write(filename="", text="")` |
| `3-to_json_string.py` | `def to_json_string(my_obj)` |
| `4-from_json_string.py` | `def from_json_string(my_str)` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename)` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename)` |
| `7-add_item.py` |  |
| `8-class_to_json.py` | `def class_to_json(obj)` |
| `9-student.py` | `def to_json(self)` |
| `10-student.py` | `def to_json(self, attrs=None)` |
| `11-student.py` | `def to_json(self, attrs=None)` |
| `12-pascal_triangle.py` | `def pascal_triangle(n)` |

## Tasks
* **0. Read file**
	* [0-read_file.py](./0-read_file.py): Reads a text file and prints it to stdout
	* Uses the with statement to perform the above operation
* **1. Write to a file**
	* [1-write_file.py](./1-write_file.py): Writes a string to a text file and returns the number of characters written
* **2. Append to a file**
	* [2-append_write.py](./2-append_write.py): Appends a string at the end of a text file and returns the characters appended.
* **3. To JSON string**
	* [3-to_json_string.py](./3-to_json_string.py): Returns the JSON representation an object(string)
* **4. From JSON string to Object**
	* [4-from_json_string.py](./4-from_json_string.py): Returns an object represented by a JSON string
* **5. Save Object to a file**
	* [5-save_to_json_file.py](./5-save_to_json_file.py): Writes an object to a text file using a JSON representation
* **6. Create object from a JSON file**
	* [6-load_from_json_file.py](./6-load_from_json_file.py): Creates anobject from a JSON file.
* **7. Load, add, save**
	* [7-add_item.py](./7-add_item.py): Adds all arguments to a python list and saves them to a file
* **8. Class to JSON**
	* [8-class_to_json.py](./8-class_to_json.py): Returns a dictionary description with a simple data structure for JSON serialization of an object.
* **9. Student to JSON**
	* [9-student.py](./9-student.py): Defines a class Student.
* **10. Student to JSON with filter**
	* [10-student.py](./10-student.py): Defines a class student based on 9-student.py
* **11. Student to disk and reload**
	* [11-student.py](./11-student.py): Defines a class student based on 10-student.py
* **12. Pascal's Triangle**
	* [12-pascal_triangle.py](./12-pascal_triangle.py): Returns a list of integers representing Pascals Triangle
