#!/usr/bin/python36


import subprocess as sp
import os
import cgi
print("content-type: text/html\n")
#print("\t\t\t\tDISTRIBUTED COMPUTING")
#print("\t\t\t\t---------------------")
#print("hi")
a=cgi.FieldStorage()
sys=a.getvalue('sys')
ch=a.getvalue('ch')
jip=a.getvalue('jip')
mip=a.getvalue('mip')
rip=a.getvalue('rip')
rname=a.getvalue('rname')
rpass=a.getvalue('rpass')

#print(rpass)
#print(rip)
#print(rname)
#print(sys)
#print(ch)
#print(jip)
#print(mip)
#sys=input("enter where u want to set up distributed computing: ")

#ch=input("Enter ur choice: ")

if sys=="local":
	sw=sp.getoutput("sudo rpm -q jdk1.8")
	if "not" in sw:
		#print("java will be installed in a minute..")	
		sp.getoutput("sudo rpm -ivh /root/Desktop/jdk-8u171-linux-x64.rpm; sudo echo 'export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/' >> /root/.bashrc;sudo echo 'export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH' >> /root/.bashrc")

	#else:
		#print("java is already installed")	
		#ed=sp.getoutput("sudo java -version")	
		#print(ed)
		#print("\n")
		
	sw1=sp.getoutput("sudo rpm -q hadoop")
	if "not" in sw1:
		#print("hadoop will be installed in a minute..")	
		sp.getoutput("sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")		
	#else:
		#print("hadoop is already installed")	
		#ed=sp.getoutput("sudo hadoop version")	
		#print(ed)
		#print("\n")

	
	#jip=input("enter ip of jobtracker: ")

	if ch=="1" or ch=="3":
		#mip=input("Enter master ip: ")
		f2=open('/code/core-site.xml','w')
		f2.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value> 
</property>
</configuration>""".format(mip))
		f2.close()

		f1=open('/code/mapred-site.xml','w')
		f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>""".format(jip))		
		f1.close()			
		sp.getoutput("sudo mv /code/mapred-site.xml /etc/hadoop/")
		sp.getoutput("sudo mv /code/core-site.xml /etc/hadoop/")
		if ch=="1":
			sp.getoutput("sudo iptables -F;sudo setenforce 0;sudo hadoop-daemon.sh start jobtracker")
			jt=sp.getoutput("sudo jps | grep JobTracker")
			print(jt)
			if jt=='':
				print("Jobtracker not created")
			else:
				print("JobTracker created successfully!!")
		
			exit()
		else:
			print("Client configured successfully!!")
				
	elif ch=="2":
		#print("okay")
		f1=open('/code/mapred-site.xml','w')
		f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>""".format(jip))		
		f1.close()			
		sp.getoutput("sudo mv /code/mapred-site.xml /etc/hadoop/")
		sp.getoutput("sudo iptables -F;sudo setenforce 0;sudo hadoop-daemon.sh start tasktracker")
		tt=sp.getoutput("sudo jps | grep TaskTracker")
		print(tt)
		if tt=='':
			print("tasktracker not created")
		else:
			print("TaskTracker created successfully!!")
		
		exit()
	

elif sys=="remote":

	#rip=input("enter ip of remote: ")
	#rname=input("enter remote name: ")
	#rpass=input("eneer remote password: ")

	'''	sw=sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} rpm -q jdk1.8".format(rpass,rname,rip))
	if "not" in sw:
		print("java will be installed in a minute..")	
		sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {}rpm -ivh /root/Desktop/jdk-8u171-linux-x64.rpm".format(rpass,rname,rip))
		sp.getooutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} echo 'export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/' >> /root/.bashrc".format(rpass,rname,rip))
		sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} echo 'export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH' >> /root/.bashrc".format(rpass,rname,rip))

	else:
		print("java is already installed")	
		ed=sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {}java -version".format(rpass,rname,rip))	
		print(ed)
		print("\n")
		
	sw1=sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} rpm -q hadoop".format(rpass,rname,rip))
	if "not" in sw1:
		print("hadoop will be installed in a minute..")	
		sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {}rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(rpass,rname,rip))		
	else:
		print("hadoop is already installed")	
		ed=sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {}hadoop version".format(rpass,rname,rip))	
		print(ed)
		print("\n")
	'''
		
	
	if ch=="1" or ch=="3":
		#mip=input("Enter master ip: ")	
		f2=open('/code/core-site.xml','w')
		f2.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value> 
</property>
</configuration>""".format(mip))
		f2.close()

		f1=open('/code/mapred-site.xml','w')
		f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>""".format(rip))		
		f1.close()
		
		sp.getoutput("sudo sshpass -p {} scp /code/core-site.xml root@{}:/etc/hadoop/".format(rpass,rip))
		sp.getoutput("sudo sshpass -p {} scp /code/mapred-site.xml root@{}:/etc/hadoop/".format(rpass,rip))
		sp.getoutput("sudo rm -rf /code/mapred-site.xml")			
		sp.getoutput("sudo rm -rf /code/core-site.xml")			

		if ch=="1":
			sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} iptables -F".format(rpass,rname,rip))
			sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} setenforce 0".format(rpass,rname,rip))
			sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} hadoop-daemon.sh start jobtracker".format(rpass,rname,rip))
			jt=sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} jps | grep JobTracker".format(rpass,rname,rip))
			print(jt)
			if jt=='':
				print("Jobtracker not created")
			else:
				print("JobTracker created successfully!!")
		
			exit()
		else:
			print("Client configured successfully!!")
				
	elif ch=="2":
		f1=open('/code/mapred-site.xml','w')
		f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>""".format(jip))		
		f1.close()			
		sp.getoutput("sudo sshpass -p {} scp /code/mapred-site.xml {}:/etc/hadoop/".format(rpass,rip))
		sp.getoutput("sudo rm -rf /code/mapred-site.xml")	
		sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} iptables -F".format(rpass,rname,rip))
		sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} setenforce 0".format(rpass,rname,rip))
		sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} hadoop-daemon.sh start tasktracker".format(rpass,rname,rip))

		tt=sp.getoutput("sudo sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} jps | grep TaskTracker".format(rpass,rname,rip))
		print(tt)
		if tt=='':
			print("tasktracker not created")
		else:
			print("TaskTracker created successfully!!")
		
		exit()
				



