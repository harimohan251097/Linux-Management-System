#!/usr/bin/python2

import commands as sp
import cgi
print("content-type:  text/html")
print("")

print("<u>HDFS SETUP COMPLETE SUCESSFULLY</u>")

i=0
form  = cgi.FieldStorage()
while True:
	i+=1
	dnode=form.getvalue("datanode{}".format(i))
	if dnode == '' :
		break

print(dnode)



print("<form>")

print("""
<br />
<br />
<br />

<table border='5'>
<tr>
<td>no of node formed</td>
<td></td>
</tr>



<tr>
<td>NAMENODE</td>
<td>1</td>
</tr>
                
""")

print("""       
<tr>
<td>DATANODE</td>
<td>4</td>
</tr>""")

print(""" 
<tr>      
<td> cilck to return to hadoop setup page</td>
<td><a href='hadoop.py'> click here<a />
</td>
</tr>


</table>
""")


print("</form>")
                                           
