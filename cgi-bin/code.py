#!/usr/bin/python36
import os
import subprocess


#subprocess.getoutput("rpm -q jdk-8u171-linux-x64.rpm")
#subprocess.getoutput("rpm -q hadoop-1.2.1-1.x86_64.rpm ")

choice = input("Where do you want to create : (local/remote) ")
print ("What do you want to set up master(m)/slave(s): ")
c = input("Enter your choice: ")
mip = input("Enter IP Address of master : ")

if choice =="l" :
	sw=os.path.exists("/usr/java/jdk1.8.0_171-amd64/bin/java")
	if sw==True:
		print("java is already installed !")
		e=subprocess.getoutput("java -version")
		print(e)
		print("\n")
	else:
		print("Please wait till the software is being installed....")
		subprocess.getoutput("rpm -ivh /root/Desktop/jdk-8u171-linux-x64.rpm")
		subprocess.getoutput("echo 'export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/ >> /root/.bashrc'" )
		subprocess.getoutput("echo 'export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH >> /root/.bashrc" )

	sw=os.path.exists("/usr/bin/hadoop")
	if sw==True:
		print("hadoop is already installed !")
		e=subprocess.getoutput("hadoop version")
		print(e)
		print("\n")
	else:
		print("Please wait till the software is being installed....")
		subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
	

	#mip=input("Enter the IP Address of Master: ")

	if c=='m':
		
		#if count==0:
		#rip=input("Enter the IP Address of Master")
		#dirname=input("Enter the name of directory : ")
		print("Master is being created ...")
		f=open('/etc/hadoop/hdfs-site.xml', 'w')
		f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name> 
<value>/nn1</value>         
</property>                 
</configuration>""")#. format (dirname))
		f.close()
		f1=open('/etc/hadoop/core-site.xml' , 'w')
		f1.write(""" <!-- <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> -->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration> """. format(mip))
		f1.close()
		#subprocess.getoutput("cp /root/Documents/Project01/hdfs-site1.xml /etc/hadoop/hdfs-site.xml". format (mip))
		#subprocess.getoutput("cp /root/Documents/Project01/core-site1.xml /etc/hadoop/core-site.xml". format(mip))
		#d=input("Enter the name of directory")
		#subprocess.getoutput("mkdir /{}". format(dirname))			
		subprocess.getoutput("iptables -F")			
		subprocess.getoutput("hadoop-daemon.sh start namenode")
		d= subprocess.getoutput("jps | grep NameNode")
		if d=='':
			print("NAMENODE NOT RUNNING !!")
	
		else:
			print("NAMENODE RUNNING ...")
		subprocess.getoutput("firefox {}:50070". format(mip))
		exit()
		'''elif count==1:
			print("Master already created ! ")
			input("enter to cont...")'''

	elif c=='s':
		#dirname=input("Enter the name of directory : ")
		print("Slave is being created ...")
		f=open('/etc/hadoop/hdfs-site.xml', 'w')
		f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name> 
<value>/data</value>         
</property>                 
</configuration> """)
		f.close()

		f1=open('/etc/hadoop/core-site.xml' , 'w')
		f1.write(""" <!-- <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> -->

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration> """. format(mip))

		f1.close()
		#subprocess.getoutput("scp /root/Documents/Project01/hdfs-site1.xml {}:/etc/hadoop/hdfs-site.xml". format (mip))
		#subprocess.getoutput("scp /root/Documents/Project01/core-site1.xml {}:/etc/hadoop/core-site.xml". format(mip))
		#d=input("Enter the name of directory")
		#subprocess.getoutput("mkdir /{}". format(dirname))			
		subprocess.getoutput("iptables -F")			
		subprocess.getoutput("hadoop-daemon.sh start datanode")
		d= subprocess.getoutput("jps | grep DataNode")
		if d=='':
			print("DATANODE NOT RUNNING !!")
			
		else:
			print("DATANODE RUNNING ...")
			subprocess.getoutput("firefox {}:50070". format(mip))
			exit()

	


elif choice == "remote":
	if c=='m':
		user=input("Enter your master username: ")
		password=input("Enter your master password: ")
		#mip=input("Enter the master's IP Address: ")
		sw=os.path.exists("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} /usr/java/jdk1.8.0_171-amd64/bin/java". format(password,user,mip))
		if sw==True:
			print("java is already installed !" )
			e=subprocess.getoutput("java -version")
			print(e)
			print("\n")
	
		else:
			print("Please wait till the software is being installed....")
			subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} rpm -ivh /root /Desktop/jdk-8u171-linux-x64.rpm". format(password,user,mip))
			subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} echo 'export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/ >> /root/.bashrc'". format(password,user,mip) )
			subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} echo 'export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH >> /root/.bashrc'". format(password,user,mip) )

		sw1=os.path.exists("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} /usr/bin/hadoop". format(password,user,mip))
		if sw1==True:
			print("hadoop is already installed !")
			e=subprocess.getoutput("hadoop version")
			print(e)
			print("\n")
		else:
			print("Please wait till the software is being installed....")
			subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force". format(password,user,mip))
	

		#print ("What do you want to set up master(m)/slave(s): ")

		#c=input("Enter your choice: ")
		#	if c=='m':
		#		if count==1:
		#			print("Master already created ! ")
		#			input("enter to cont...")
		#		elif count==0:
					#rip=input("Enter the IP Address of Master")	
		dirname=input("Enter the name of directory : ")
		print("Master is being created ...")
		f=open('/root/Documents/Project01/hdfs-site1.xml','w')
		f.write("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name> 
<value>/{}</value>         
</property>                 

</configuration> """. format(dirname))
		
		f.close()
		f1=open('/root/Documents/Project01/core-site1.xml','w')
		f1.write(""" <!-- <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> -->
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration> """. format(mip))
		f1.close()


		subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /root/Documents/Project01/hdfs-site1.xml {}:/etc/hadoop/hdfs-site.xml". format (mip))
		subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /root/Documents/Project01/core-site1.xml {}:/etc/hadoop/core-site.xml". format(mip))
				
				
		#d=input("Enter the name of directory")
		subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {}mkdir /{}". format(password,user,mip,dirname))			
		subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} iptables -F". format(password,user,mip))			
		subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} hadoop-daemon.sh start namenode". format(password,user,mip))
		subprocess.getoutput("rm /root/Documents/Project01/hdfs-site1.xml")
		subprocess.getoutput("rm /root/Documents/Project01/core-site1.xml")
		d= subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} 'jps | grep NameNode'". format(password,user,mip))
		if d=='':
			print("NAMENODE NOT RUNNING !!")
	
		else:
			print("NAMENODE RUNNING ...")
		count = 1
		subprocess.getoutput("firefox {}:50070". format(mip))
		exit()


	elif c=='s':
		
		a = input("How many slaves do you want to create: ")
		b = int(a) + 1
		for i in range (1,b):
			#k=i+1
			#print ("i : {} i+1 {}". format(i,k))
			user=input("Enter the username of slave {} : ". format (i))
			password=input("Enter your slave password {} : ". format (i))
			sip=input("Enter the IP Address of slave {} : ". format (i))
	
		#for j in range (1,b):
			dirname=input("Enter the name of directory : ")
			print("Slave is being created ...")
			f=open('/root/Documents/Project01/hdfs-site1.xml', 'w')
			f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name> 
<value>/{}</value>         
</property>                 
</configuration> """. format(dirname))
			f.close()
			f1=open('/root/Documents/Project01/core-site1.xml' , 'w')
			f1.write(""" <!-- <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> -->
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration> """. format(mip))
			f1.close()
			subprocess.getoutput("sshpass -p {} scp -o StrictKeyHostChecking=no -l {} {} /root/Documents/Project01/hdfs-site1.xml {}:/etc/hadoop/hdfs-site.xml". format (password,user,sip,mip))
			subprocess.getoutput("sshpass -p {} scp -o StrictKeyHostChecking=no -l {} {} /root/Documents/Project01/core-site1.xml {}:/etc/hadoop/core-site.xml". format(password,user,sip,mip))
			#d=input("Enter the name of directory")
			subprocess.getoutput("sshpass -p {} scp -o StrictKeyHostChecking=no -l {} {} mkdir /{}". format(password,user,sip,dirname))			
			subprocess.getoutput("sshpass -p {} scp -o StrictKeyHostChecking=no -l {} {} iptables -F". format(password,user,sip))			
			#subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l {} {} bash -c 'echo Y | hadoop namenode -format'".format(rpass,rname,rip))
			subprocess.getoutput("sshpass -p {} scp -o StrictKeyHostChecking=no -l {} {} hadoop-daemon.sh start datanode &". format(password,user,sip))
			d=subprocess.getoutput("sshpass -p {} scp -o StrictKeyHostChecking=no -l {} {} jps | grep DataNode". format(password,user,sip))
			if d=='':
				print("DATANODE NOT RUNNING !!")
		
			else:
				print("DATANODE RUNNING ...")
			#subprocess.getoutput("firefox {}:50070". format(mip)) 
		exit()
						

'''a = input("How many slaves do you want to create: ")
		b = int(a) + 1
		for i in range (1,b):
			k=i+1
			#print ("i : {} i+1 {}". format(i,k))
			sip=input("Enter the IP Address of slave {}". format (i))
	
		#for j in range (1,b):'''

'''fh= open("/etc/hadoop/hdfs-site.xml","a")
textList = ["One", "Two2", "Three3", "Four4", "Five5"]
for line in textList:
	write line to output file
	fh.write(line)
	fh.write("\n")
fh.close()'''
