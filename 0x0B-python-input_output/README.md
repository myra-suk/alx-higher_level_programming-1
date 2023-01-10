# Python - Input/Output

In this project I learnt and tested Input/Output Concepts in Python Programming

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

## Tasks
* **0. Read file**
	* [0-read_file.py](./0-read_file.py): Reads a text file and prints it to stdout
	* Uses the with statement to perform the above operation
