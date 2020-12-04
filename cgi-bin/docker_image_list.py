#!/usr/bin/python2

import commands as sp


cmd="docker images"
output = sp.getoutput(cmd)
imagelist = output.split("\n")
for i in imagelist[1:]:
	print(i.split()[0] + ":" +  i.split()[1])
