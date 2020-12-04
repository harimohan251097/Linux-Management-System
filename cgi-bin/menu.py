#!/usr/bin/python36
import cgi
import subprocess

print("content-type: text/html")
print("")

a=cgi.FieldStorage()
b=a.getvalue('u')

ch=subprocess.getoutput("sudo useradd {}".format(b))

print("user {} created successfully".format(b))

