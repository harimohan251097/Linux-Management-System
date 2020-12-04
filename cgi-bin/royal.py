#!/usr/bin/python36

import subprocess
import os
import cgi
print("content-type: text/html\n")

b=cgi.FieldStorage()
mysystem=b.getvalue('sys')
if mysystem=="remote":
	rip=b.getvalue('ip')
	hname=b.getvalue('host')
	rpasswd=b.getvalue('pass')


if mysystem=="local":

		

		ch=b.getvalue('inp')

		if int(ch)==1:
			x=subprocess.getoutput("date")
			print(x)
		elif int(ch)==2:
			x=subprocess.getoutput("cal")
			print(x)
		elif int(ch)==3:
			uname=input("Enter ur file name: ")	
			x=subprocess.getoutput("useradd {}".format(uname))
			p;rint(x)
		elif int(ch)==4:
			fname=input("Enter ur file name: ")
			x=subprocess.getoutput("touch {}".format(fname))
			print(x)
		elif int(ch)==5:
			os.system("yum install httpd")
			os.system("systemctl start httpd")
			wname=input("enter path of webpage to show to client: ")
			os.system("cp {} /var/www/html".format(wname))
			os.system("iptables -F")
		elif int(ch)==6:
			exit()

		else:
			print("not supported")

elif mysystem=="remote":
		

		ch=b.getvalue('inp')

		if int(ch)==1:
			x=subprocess.getoutput("sshpass -p {} ssh -l {} {} date".format(rpasswd,hname,rip))
			print(x)
		elif int(ch)==2:
			x=subprocess.getoutput("sshpass -p {} ssh -l {} {} cal".format(rpasswd,hname,rip))
			print(x)
		elif int(ch)==3:
			tname=input("Enter ur user name: ")	
			os.system("sshpass -p {} ssh -l {} {} useradd {}".format(rpasswd,hname,rip,tname))
			os.system("sshpass -p {} ssh -l root {} passwd {}".format(rpasswd,rip,tname))		
		elif int(ch)==4:
			fname=input("Enter ur file name: ")
			x=subprocess.getoutput("sshpass -p {} ssh -l {} {} touch {}".format(rpasswd,hname,rip,fname))
			print(x)
				
		elif int(ch)==5:
			exit()
		else:
			print("not supported")
