#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp

cmd="sudo rpm -q docker-ce"

output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("already installed")
else:
	print("not installed")


