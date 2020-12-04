#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
nm = form.getvalue("nm")
ns = form.getvalue("ns")

sj = 1
mj = 1

print("<form action='setup-hdfs-ansible.py'>")

while mj <= int(nm):
	print("MN {0} : <input name='mip{0}' /><br />".format(mj))
	mj+=1


while sj <=  int(ns): 
	print("DN {0} : <input name='sip{0}' /><br />".format(sj))
	sj+=1

print("""
<input type='submit' />
</form>
""")










