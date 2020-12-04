#!/usr/bin/python36

import cgi
import subprocess as sp
import os

print("content-type: text/html\n")
print("ho")
a=cgi.FieldStorage()
system=a.getvalue('sys')
inp=a.getvalue('inp')
print(inp)
type1=a.getvalue('type1')
size1=a.getvalue('size1')
ftype=a.getvalue('ftype')
num=a.getvalue('num')
mount=a.getvalue('mount')


