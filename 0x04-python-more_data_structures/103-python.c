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

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

		for (; i < size + 1 && i < 10; i++)
			printf(" %02hhx", string[i]);
		printf("\n");
	}
}
