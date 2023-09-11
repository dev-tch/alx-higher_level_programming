#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - print some basic info about python list
* @p: object
* Return: void
*/
void print_python_list_info(PyObject *p)
{
	long int len = PyList_Size(p);
	int j = 0;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (j = 0; j < len; j++)
		printf("Element %i: %s\n", j, Py_TYPE(obj->ob_item[j])->tp_name);
}
