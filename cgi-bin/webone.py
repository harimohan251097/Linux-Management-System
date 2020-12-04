#!/usr/bin/python36
import os
import subprocess

print("content-type: text/html\n")
print("<form action='thanks.py'")

print("<h1 >List Running services in Server</h1><br/><h3>")

print("""	<br><br> cilck to start httpd services
<input type='submit' /><br/><br/><br/>""")
a=subprocess.getoutput("systemctl status httpd")
print("<br/>")
print(a)


