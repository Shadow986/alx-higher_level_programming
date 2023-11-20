#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list pointer
 *
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: PyObject bytes pointer
 *
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	PyBytesObject *bytes;
	char *str;

	printf("[*] Python bytes\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	str = bytes->ob_sval;
	size = Py_SIZE(p);

	printf("  Size of the Python Bytes = %ld\n", size);
	printf("  Trying string: %s\n", str);
	printf("  First %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02hhx%s", str[i], i + 1 < size + 1 && i + 1 < 10 ? " " : "\n");
}

/**
 * print_python_float - Prints basic info about Python floats.
 * @p: PyObject float pointer
 *
 * Return: Nothing.
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[*] Python float\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
