#!/usr/bin/python36

#import cgi

import subprocess

print("content-type: text/html")
print("")
print("<form action='deleteip.py'>")

d=""
a=cgi.FieldStorage()
ip=a.getvalue('ip')

f=open("/var/www/html/iplist.txt","r")
b=f.read()
f.close()
ip="192.168.56.102"
f=open("/var/www/html/iplist.txt","w")
c=b.split("\n")
for i in c:
	if i==ip:
		continue
	d=d+i+"\n"
f.write(d)
f.close()
Print("operation complete/n ip deleted from server/n/n press enter for Refresh ip list")
print("<input type='submit' value='submit' /></form>")


