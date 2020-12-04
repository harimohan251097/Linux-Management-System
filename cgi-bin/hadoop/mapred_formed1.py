#!/usr/bin/python2

import commands as sp
import cgi

print("content-type:  text/html") 
print("")

fh = open('/var/www/cgi-bin/host/hosts', 'a')

print("<u>                            MANAGE MAPREDUCE  SETUP</u>")

form = cgi.FormContent()

for i in form.keys(): 
	
	if 'job' in i:
		fh.write("[job]\n")
		fh.write(form[i][0] + " ansible_ssh_user=root ansible_ssh_pass=123456\n")
                
	else:	
		fh.write("[task]\n")
		fh.write(form[i][0] + " ansible_ssh_user=root ansible_ssh_pass=123456\n")

fh.close()


print("<table border='5' align='center'>")

print("""
<tr>
<th>S.No.</th>
<th>IP address</th>
<th>Tracker</th>
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
	<td><a href='http://192.168.43.247:50030/machines.jsp?type=active'>click here</a> </td>
        <td><a href='mapred_start.py?ip={1},tracker={2}'>start</a></td>
        <td><a href='mapred_stop.py?ip={1},tracker={2}'>stop</a></td>
	</tr>
        """.format(k,form[i][0],i))


print("</table>")
y=sp.getoutput("ansible-playbook jt_hadoop.yml")

x=sp.getoutput("ansible-playbook  tt_hadoop.yml")

if 'JobTracker' in y :
	print("jobtracker started")

if 'TaskTracker' in  x :
	print("tasktracker started")
print("all done")

