#!/usr/bin/python36

import subprocess as sp
import os

print("content-type: text/html\n")

a=FieldStorage()
system=a.getvalue('sys')
inp=a.getvalue('inp')
type1=a.getvalue('type1')
size1=a.getvalue('size1')
ftype=a.getvalue('ftype')
num=a.getvalue('num')
mount=a.getvalue('mount')
print(type(inp))
#system=input("enter where u want to create partition:")

'''
if system=="local":
	
	
		print("""
		press 1:To create partition
		press 2:To view partition
		press 3:To exit 
		""")

		#inp=input("Enter ur choice: ")
		sp.getoutput("sudo partprobe /dev/sdb")
		if int(inp)==1:
		
			counting partition
			par=int(sp.getoutput("lsblk | grep sdb | wc -l"))-1
			print(par)
			
			creating partition
			if par<3:
				print("default(primary): ")
				type1=input("enter type of partition:")
				size=input("enter partion size(+1G or in sectors):")
				sp.getoutput("echo -e 'n\n{}\n\n\n{}\nw\n'| fdisk /dev/sdb".format(type1,size))
				sp.getoutput("echo 'n\n' | fdisk /dev/sdb > /root/Desktop/rm.txt")
				fp=open('/root/Desktop/rm.txt','r')
				line=[]
				for x in fp:
					line.append(x)
				print(line[7])		

			elif par==3:
				print("default(extended): ")
				type1=input("enter type of partition:")
				size=input("enter partion size(+1G or in sectors):")
		
				sp.getoutput("echo 'n\n{}\n\n{}\nw\n'| fdisk /dev/sdb".format(type1,size))	
				print("Partition {} of type extended is set\n".format(par+1))
				fp=open('/root/Desktop/rm.txt','r')
				line=[]
				for x in fp:
					line.append(x)
				print(line[7])		

			else:	
				print("All primary partitions are in use")
				print("Adding logical partition {}".format(par+1))
				size=input("enter partion size(+1G or in sectors):")
				sp.getoutput("echo 'n\n\n{}\nw\n'| fdisk /dev/sdb".format(size))
				print("Logocal partition {} of type Linux is set\n".format(par+1))
			updating drivers			
			sp.getoutput("partpobe /dev/sdb")
			
			print("Partiton created successfull!!")	

			formating partition
			form=input("specify format type: ")
			sp.getoutput("mkfs.{} /dev/sdb{}".format(form,par+1))

			mounting
			pnum=input("enter partition number to mount: ")

			if int(pnum)<=par+1:
				mp=input("enter mount point: ")
				sp.getoutput("mkdir /media/{}".format(mp))
				sp.getoutput("mount /dev/sdb{} /media/{}".format(pnum,mp))
			else:
				print("Partition does not exist!!")
						
			sp.getoutput("rm /root/Desktop/rm.txt")			

			
		elif int(inp)==2:
			x=sp.getoutput("echo 'p\n' | fdisk /dev/sdb")
			print(x)

		elif int(inp)==3:
			exit()
		
		input("Enter to continue...")
		os.system("clear")

elif system=="remote":
	rip=input("enter remote ip: ")
	rname=input("enter user name: ")
	rpass=input("enter password: ")
	while(True):
		print("""
		press 1:To create partition
		press 2:To view partition
		press 3:To exit 
		""")

		inp=input("Enter ur choice: ")

		if int(inp)==1:
		
			counting partition
			par=int(sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking -l {} {} lsblk | grep sdb | wc -l").format(rpass,rname,rip))-1

			print(par)

			creating partition
			if par<3:
				print("default(primary): ")
				type1=input("enter type of partition:")
				size=input("enter partion size(+1G or in sectors):")
				sp.getoutput("sshpass -p {} ssh -l {} {}'echo -e 'n\n{}\n\n\n{}\nw\n'| fdisk /dev/sdb'".format(rpass,rname,rip,type1,size))
			
			elif par==3:
				print("default(extended): ")
				type1=input("enter type of partition:")
				size=input("enter partion size(+1G or in sectors):")
		
				sp.getoutput("sshpass -p {} ssh -l {} {} 'echo 'n\n{}\n\n{}\nw\n'| fdisk /dev/sdb'".format(rpass,rname,rip,type1,size))	
			
			else:	
				print("All primary partitions are in use")
				print("Adding logical partition {}".format(par+1))
				size=input("enter partion size(+1G or in sectors):")
				sp.getoutput("sshpass -p {} ssh -l {} {} 'echo 'n\n\n{}\nw\n'| fdisk /dev/sdb'".format(rpass,rname,rip,size))

			updating drivers			
			sp.getoutput("sshpass -p {} ssh -l {} {} partpobe /dev/sdb".format(rpass,rname,rip))
			print("Partiton created successfull!!")	

			formating partition
			form=input("specify format type: ")
			sp.getoutput("sshpass -p {} ssh -l {} {} mkfs.{} /dev/sdb{}".format(rpass,rname,rip,form,par+1))

			mounting
			pnum=input("enter partition number to mount: ")

			if int(pnum)<=par+1:
				mp=input("enter mount point: ")
				sp.getoutput("sshpass -p {} ssh -l {} {} mkdir /media/{}".format(rpass,rname,rip,mp))
				sp.getoutput("sshpass -p {} ssh -l {} {} mount /dev/sdb{} /media/{}".format(rpass,rname,rip,pnum,mp))
			else:
				print("Partition does not exist!!")

		elif int(inp)==2:
			x=sp.getoutput("sshpass -p {} ssh -l {} {} 'echo '\''p\n'\'' | fdisk /dev/sdb'".format(rpass,rname,rip))
			print(x)

		elif int(inp)==3:
			exit()

else:
	print("local or remote was not entered!")
	exit()			
input("Enter to continue...")
os.system("clear")
'''
