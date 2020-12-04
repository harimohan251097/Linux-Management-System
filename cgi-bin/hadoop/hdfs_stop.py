#!/usr/bin/python2

import commands as sp
import cgi


print("content-type: text/html")


form = cgi.FieldStorage()
ip = form.getvalue('ip')
node = form.getvalue('node')
cmd="hadoop-daemon.sh stop {}".format(node)

output=sp.getstatusoutput(cmd) 
if '0' in output:
        print('location: hdfs_formed1.py')
        print("")
else:
        print("")
        print("error")

