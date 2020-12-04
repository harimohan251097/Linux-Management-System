#!/usr/bin/python2

import commands as sp
import cgi
print("content-type:  text/html")
print("")

print("<u>ENTER DETAIL FOR  HDFS SETUP</u>")


form  = cgi.FieldStorage()

nnode = form.getvalue("namenode")
dnode = form.getvalue("datanode")

print(nnode)
print(dnode)
print("<form action='hdfs_formed1.py?dnode={}'>".format(dnode))

print("""
<br />
<br />
<br />

<table border='5'>
<tr>
<td>enter ip address of node to be formed</td>
<td></td>
</tr>



<tr>
<td>NAMENODE1 IP</td>
<td><input name='namenode' /></td>
</tr>
                
""")




i=0
while True : 
	if int(i) == int(dnode) :
		break 
	i+=1
	print("""	
	<tr>
	<td>DATANODE{}  SERVICE</td>
	<td><input name='datanode{}' /></td>
	</tr>""".format(i,i))
	
print("""	
<td> cilck to submit</td>
<td>
<input type='submit' />

</td>
</tr>


</table>
""")


print("</form>")

                                                    
