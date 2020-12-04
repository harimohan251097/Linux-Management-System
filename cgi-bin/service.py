#!/usr/bin/python36
import os
import subprocess

print("content-type: text/html\n")
print("<form action='thanks.py'")

print("<h1 >List Running services in Server</h1><br/><h3>")
a=subprocess.getoutput("systemctl list-units --type=service")
a=a.split("\n")
print("<br/>")
for i in a:
	print(i+"<br>")


