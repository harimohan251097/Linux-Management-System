#!/usr/bin/python36
import os
import subprocess

print("content-type: text/html\n")
print("<form action='thanks.py'")

print("<h1 >List Install software in Server</h1><br/><h3>")
print("""Enter Software Name for Uninstall

<input name='namenode' />""")
print("""	<br><br> cilck to submit
<input type='submit' /><br/><br/><br/>""")
a=subprocess.getoutput("yum list installed")
a=a.split("\n")
print("<br/>")
for i in a:
	print(i+"<br>")


