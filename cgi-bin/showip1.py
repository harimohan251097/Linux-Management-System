#!/usr/bin/python36

print("content-type: text/html\n")
f=open("/var/www/html/iplist.txt","r")
print("<h1 >List Of IP Added in Server</h1>")
b=f.read()
f.close()
c=b.split("\n")
for i in c:
	print("<h3>"+i+"<h3>")
	#print("<br/>")


