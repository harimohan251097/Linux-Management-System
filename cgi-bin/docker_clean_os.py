#!/usr/bin/python2

import commands as sp


print("content-type: text/html")

cmd = "sudo docker rm -f $(sudo docker ps -a -q )"

output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("location: docker.py")
	print("")
else:
	print("")
	print("not cleaned: error")
