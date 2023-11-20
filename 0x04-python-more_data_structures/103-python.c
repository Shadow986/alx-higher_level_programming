#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - A function that gives data of the PyBytesObject
 * @obj: the PyObject
 */
void print_python_bytes(PyObject *obj)
{
	Py_ssize_t size = 0, obj_size = 0;
	char *string = NULL;
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	if (PyBytes_AsStringAndSize(obj, &string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (obj_size < size + 1 && obj_size < 10)
		{
			printf(" %02hhx", string[obj_size]);
			obj_size++;
		}
		printf("\n");
	}
}
/**
 * print_python_list - A function that gives data of the PyListObject
 * @obj: the PyObject
 */
void print_python_list(PyObject *obj)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int obj_size = 0;
	if (PyList_CheckExact(obj))
	{
		size = PyList_Size(obj);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)obj)->allocated);
		while (obj_size < size)
		{
			item = PyList_GET_ITEM(obj, obj_size);
			printf("Element %d: %s\n", obj_size, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			obj_size++;
		}
	}
}
