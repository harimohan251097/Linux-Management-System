#!/usr/bin/python2

import commands as sp
import cgi


print("content-type: text/html")


form = cgi.FieldStorage()
ip = form.getvalue('ip')
node = form.getvalue('node')

cmd=" sshpass -p 123456  ssh -l root {}  hadoop-daemon.sh start {}".format(ip,node)

output=sp.getstatusoutput(cmd)

if output[0]  == 0:
        print('location: hdfs_formed1.py')
        print("")
else:
        print("")
        print("error")

