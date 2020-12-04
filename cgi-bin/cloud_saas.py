#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")

st = sp.getoutput("sudo ansible-playbook /ws/cloud_saas.yml ")
print(st)
 

