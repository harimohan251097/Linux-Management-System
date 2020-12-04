#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")

cmd="sudo docker ps -a"

output = sp.getoutput(cmd)


print("<iframe  width='100%' name='diframe'></iframe>")

print("<table border='5' align='center'>")

print("""
<tr>
<th>Image name</th>
<th>Container Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Console</th>
</tr>
""")


for i in output.split("\n")[1:]:
	dimagename= i.split()[1]
	dname = i.split()[-1] 

	if "Exited" in i:
		d_status="stopped"

	elif "Up" in i:
		d_status="running"
	else:
		d_status="unknown"
	print("""
	<tr>
	<td>{0}</td>
	<td>{1}</td>
	<td>{2}</td>
	<td><a href='docker_c_start.py?x={1}'>start</a></td>
	<td><a href='docker_stop.py?x={1}'>stop</a></td>
	<td><a  target='diframe' href='http://192.168.0.105:5555'>Get Console</a></td>
	</tr>
	""".format(dimagename , dname,  d_status))



print("</table>")


print("<a href='docker.py'>click here to docker setup file</a>")
