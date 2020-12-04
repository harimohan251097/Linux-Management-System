#!/usr/bin/python2

import commands as sp
import cgi


print("content-type: text/html")


form = cgi.FieldStorage()
x = form.getvalue('x')


cmd="sudo docker start {}".format(x)

output=sp.getstatusoutput(cmd)

if output[0]  == 0:
	print('location: docker_manage.py')
	print("")
else:
	print("")
	print("error")
