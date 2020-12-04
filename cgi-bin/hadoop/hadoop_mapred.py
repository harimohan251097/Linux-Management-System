#!/usr/bin/python2

import commands as sp

print("content-type:  text/html")
print("")

print("<marquee><u>WELCOME TO MAPREDUCE SETUP</u></marquee>")



print("<form action='mapred_enter.py'>")

print("""
<br />
<br />
<br />

<table border='5'>
<tr>
<td>enter no of node to be formed</td>
<td></td>
</tr>

<tr>
<td>JOBTRACKER SERVICE</td>
<td><input name='jobtracker' /></td>
</tr>
                

<tr>
<td>TASKTRACKER  SERVICE</td>
<td><input name='tasktracker' /></td>
</tr>

<tr>
<td>submit</td>
<td>
<input type='submit' />

</td>
</tr>


</table>
""")


print("</form>")

                                                    
