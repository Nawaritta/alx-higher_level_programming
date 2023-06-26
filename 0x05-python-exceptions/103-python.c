#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n  [*] Size of the Python List = %ld\n", size);
	printf("  [*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("  Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[*] Python bytes info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n  [.] Size: %ld\n", size);
	printf("  [.] Trying string: %s\n", str);

	if (size > 10)
		size = 10;

	printf("  [.] first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic information about a Python float object.
 * @p: Pointer to the Python float object.
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("[.] float object info\n  [.] value: %f\n", value);
}
