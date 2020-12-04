#!/usr/bin/python2

import commands as sp
import cgi
print("content-type:  text/html")
print("")

print("<u>ENTER DETAIL FOR  MAPREDUCE  SETUP</u>")


form  = cgi.FieldStorage()

jtracker = form.getvalue("jobtracker")
ttracker = form.getvalue("tasktracker")


print("<form action='mapred_formed1.py?ttracker={}'>".format(ttracker))

print("""
<br />
<br />
<br />

<table border='5'>
<tr>
<td>enter ip address of tracker to be formed</td>
<td></td>
</tr>



<tr>
<td>JOBTRACKER1 IP</td>
<td><input name='jobtracker' /></td>
</tr>
                
""")




i=0
while True : 
	if int(i) == int(ttracker) :
		break 
	i+=1
	print("""	
	<tr>
	<td>TASKTRACKER{}  SERVICE</td>
	<td><input name='tasktracker{}' /></td>
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

                                                    
