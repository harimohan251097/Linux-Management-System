#!/usr/bin/python36

print("content-type: text/html\n")
print("<form action='thanks.py'")
f=open("/var/www/html/iplist.txt","r")
print("<h1 >List Of IP Added in Server</h1><br/><h3>")
b=f.read()
f.close()
c=b.split("\n")
for i in c:
	print(i)
	print("<br/>")

print("""Enter ip for deletion

<input name='namenode' />""")

print("""	<br><br> cilck to submit
<input type='submit' />
""")

