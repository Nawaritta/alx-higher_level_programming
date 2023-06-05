# 0x00. Python - Hello, World

## Tasks

### 0. Run Python file

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

    - File: 0-run


### 1. Run inline

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

    - File: 1-run_inline

### 2. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

      - File: 2-print.py


### 3. Print integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

	 - File: 3-print_number.py


### 4. Print float

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

	 - File: 4-print_float.py


### 5. Print string

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

	 - File: 5-print_string.py


### 6. Play with strings

Complete this source code to print Welcome to Holberton School!

	 - File: 6-concat.py


### 7. Copy - Cut - Paste

Complete this source code

	 - File: 7-edges.py


### 8. Create a new sentence

Complete this source code to print object-oriented programming with Python, followed by a new line.

	 - File: 8-concat_edges.py


### 9. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

      - File: 9-easter_egg.py


### 10. Linked list cycle

Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free
carrie@ubuntu:~/0x00$ cat lists.h

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

    - File: 10-check_cycle.c, lists.h

### 11. Hello, write

Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

      - File: 100-write.py


### 12. Compile

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

    - File: 101-compile


### 13. ByteCode -> Python #1

Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
	      6 LOAD_FAST                1 (b)
              9 BINARY_POWER
	      10 BINARY_ADD
	      11 RETURN_VALUE

	      Tip: Python bytecode
	      - File: 102-magic_calculation.py
