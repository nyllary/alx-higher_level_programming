#include "Python.h"


/**
 * print_python_list_info - prints some basic infomation
 * about python list
 * @p: a pointer to the list to be printed
 * must be compiled with:
 * "gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname, 
 * PyList -o libPyList.so -fPIC -I/usr/include/python3.4 
 * 100-print_python_list_info.c"
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
