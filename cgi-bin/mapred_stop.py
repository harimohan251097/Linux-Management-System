#!/usr/bin/python2

import commands as sp
import cgi


print("content-type: text/html")


form = cgi.FieldStorage()
ip = form.getvalue('ip')
tracker = form.getvalue('tracker')
cmd="hadoop-daemon.sh stop {}".format(tracker)

output=sp.getstatusoutput(cmd) 
if '0' in output:
        print('location: mapred_formed1.py')
        print("")
else:
        print("")
        print("error")

