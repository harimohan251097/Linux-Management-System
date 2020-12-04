#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")


form  = cgi.FieldStorage()

imgname = form.getvalue("imagename")
dname = form.getvalue("dockername")
gui = form.getvalue("gui")

if gui == "gui_no":
	cmd="sudo docker run -dit --name {} {}".format(dname, imgname)
else:
	cmd="sudo docker run -dit --name {} -e DISPLAY=:0 -v  /tmp/.X11-unix:/tmp/.X11-unix  --ipc=host {}".format(dname, imgname)


output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("location: docker.py")
	print("")
else:
	print("")
	print("error")
