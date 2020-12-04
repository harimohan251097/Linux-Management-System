#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")


form = cgi.FieldStorage()

paasname = form.getvalue("paasname")

s ="""FROM centos:latest
CMD {}
""".format(paasname)

fh = open('mydockerfile/Dockerfile', 'w')

fh.write(s)

fh.close()


cmd = "sudo docker build mydockerfile/ -t vimal-mypaas-python:v1"


output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("platform created")
else:
	print("error")













