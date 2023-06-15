#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints basic info about Python lists and bytes objects
 *
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;

	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	for (; i < size + 1 && i < 10; i++)
		printf(" %02hhx", string[i]);
	printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer to a Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
