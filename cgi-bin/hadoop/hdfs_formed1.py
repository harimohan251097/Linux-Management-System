#!/usr/bin/python2

import commands as sp
import cgi

print("content-type:  text/html") 
print("")

fh = open('/var/www/cgi-bin/host/hosts', 'w')

print("<u>                            MANAGE HDFS SETUP</u>")

form = cgi.FormContent()

for i in form.keys(): 
	
	if 'name' in i:
		fh.write("[master]\n")
		fh.write(form[i][0] + " ansible_ssh_user=root ansible_ssh_pass=123456\n")
                
	else:	
		fh.write("[slave]\n")
		fh.write(form[i][0] + " ansible_ssh_user=root ansible_ssh_pass=123456\n")

fh.close()


print("<table border='5' align='center'>")

print("""
<tr>
<th>S.No.</th>
<th>IP address</th>
<th>Node</th>
<th>Live status</th>
<th>Start</th>
<th>Stop</th>
</tr>
""")

k=0

for i in form.keys():
	k+=1
	print("""
        <tr>
	<td>{0}</td>
        <td>{1}</td>
        <td>{2}</td>
	<td><a href='http://192.168.43.247:50070/dfsnodelist.jsp?whatNodes=LIVE'>click here</a>
        <td><a href='hdfs_start.py?ip={1},node={2}'>start</a></td>
        <td><a href='hdfs_stop.py?ip={1},node={2}'>stop</a></td>
	</tr>
        """.format(k,form[i][0],i))


print("""<tr><td></td><td>to show  upload file click any live status then browsethe filesystem</a></td>
  </tr>        
""")
y=sp.getoutput("ansible-playbook  nn_hadoop.yml")

x=sp.getoutput("ansible-playbook  dd_hadoop.yml")

if 'NameNode' in y :
	print("namenode started")

if 'DataNode' in  x :
	print("datanode started")
print("all done")

