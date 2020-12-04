#!/usr/bin/python36


import subprocess as sp
import os
import cgi

print("content-type: text/html\n")

#print("\t\t\t\tNFS SERVER SETUP")
#print("\t\t\t\t----------------")
a=cgi.FieldStorage()
sys=a.getvalue('sys')

if sys=="local":

	
	dir1=a.getvalue('dir1')
	sip=a.getvalue('sip')
	cip=a.getvalue('cip')
	cname=a.getvalue('cname')
	cpass=a.getvalue('cpass')
	dir2=a.getvalue('dir2')


	sw=sp.getoutput("rpm -q nfs-utils")
	#print("\nChecking softwares to be installed..")
	if "not" in sw:
		sp.getoutput("yum install nfs-utils")
		
	#dir1=input("enter directory to share: ")
	#sip=input("enter server ip: ")
	#cip=input("enter client ip: ")
	#cname=input("enter client name: ")
	#cpass=input("enter client password: ")
	sp.getoutput("sudo mkdir {}".format(dir1))
	sp.getoutput("sudo echo '{} {}(rw,no_root_squash)' > /etc/exports".format(dir1,cip))
	sp.getoutput("sudo systemctl restart nfs")
	sp.getoutput("sudo systemctl enable nfs")
	sp.getoutput("sudo iptables -F")
	d=sp.getoutput("sudo exportfs -v")
	sp.getoutput("sudo setsebool -P use_nfs_home_dirs=1 &")
	print(d)
	#dir2=input("Enter directory for client's machine: ")
	my_sp= sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} sudo mkdir /mnt{}".format(cpass,cname,cip,dir2))
	print(my_sp)
	sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} sudo mount {}:{} /mnt{}".format(cpass,cname,cip,sip,dir1,dir2))
	print("chal rha hai")
	
	
elif sys=="remote":
	#sip=input("enter server ip: ")
	#sname=input("enter server name: ")
	#spass=input("enter server password: ")
	sys=a.getvalue('sys')
	dir1=a.getvalue('dir1')
	cip=a.getvalue('sip')
	sip=a.getvalue('cip')
	sname=a.getvalue('cname')
	spass=a.getvalue('cpass')
	dir2=a.getvalue('dir2')
	

	
	sw=sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} rpm -q nfs-utils".format(spass,sname,sip))

	if "not" in sw:
		sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} yum install nfs-utils".format(spass,sname,sip))
	
	sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} sudo mkdir -p /mnt{}".format(spass,sname,sip,dir1))
	print("okay")
	sp.getoutput("sudo echo '/mnt{} {}(rw,no_root_squash)' > /code/a".format(dir1,cip))
	print("okay")
	sp.getoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /code/a root@{}:/etc/exports &".format(spass,sip))

	sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} systemctl restart nfs".format(spass,sname,sip))

	sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} systemctl enable nfs".format(spass,sname,sip))

	sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} iptables -F".format(spass,sname,sip))

	d=sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} exportfs -v &".format(spass,sname,sip))

	sp.getoutput("sudo sshpass -p {} ssh -o StrictHsotkeyChecking=no -l {} {} setsebool -P use_nfs_home_dirs=1 &".format(spass,sname,sip))

	print(d)
	#dir2=input("Enter directory for client's machine: ")
	sp.getoutput("sudo mkdir -p /mnt{}".format(dir2))
	c=sp.getstatusoutput("sudo mount {}:/mnt{} /mnt{}".format(sip,dir1,dir2))
	print(c)
	print("chal rha hai")
	#sp.getoutput("sudo rm ~/Desktop/a")
	
