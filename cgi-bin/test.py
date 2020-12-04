#!/usr/bin/python36 

import PyV8

print("content-type: text/html \n")	


class Global(PyV8.JSClass):
	pass

with PyV8.JSContext(Global()) as ctxt:
	te=ctxt.eval("temp=prompt('enter remote ip address:'t)")

print(x)
