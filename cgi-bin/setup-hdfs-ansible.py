#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")

fh = open('hosts', 'w')

form = cgi.FormContent()

for i in form.keys():
	if 'm' in i:
		fh.write("[master]\n")
		fh.write(form[i][0] + "\n")
	else:	
		fh.write("[slave]\n")
		fh.write(form[i][0] + "\n")

fh.close()



#sp.getoutput("sudo ansible-playbook  nm.yml -i hosts")


