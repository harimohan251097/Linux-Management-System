#!/usr/bin/python2

import commands as sp

print("content-type:  text/html")
print("")

print("<marquee><u>WELCOME TO HDFS SETUP</u></marquee>")



print("<form action='hdfs_enter.py'>")

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
<td>NAMENODE SERVICE</td>
<td><input name='namenode' /></td>
</tr>
                

<tr>
<td>DATANODE  SERVICE</td>
<td><input name='datanode' /></td>
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

                                                    
