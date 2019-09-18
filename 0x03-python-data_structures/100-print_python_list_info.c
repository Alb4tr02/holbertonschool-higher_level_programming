#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		int idx = 0;
		PyListObject *l = (PyListObject *)p;
		int size = Py_SIZE(l);
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %lu\n", l->allocated);
		while (idx < size)
		{
			printf("Element %d: ", idx);
			printf("%s\n", Py_TYPE(PyList_GetItem(p,idx))->tp_name);
			idx++;
		}
	}
}
