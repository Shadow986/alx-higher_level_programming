#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list pointer.
 *
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	long int i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: A PyObject bytes pointer.
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	long int i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02hhx%s", string[i], i < 9 && i < size ? " " : "\n");
	}
}

