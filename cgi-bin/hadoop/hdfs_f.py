#!/usr/bin/python2

import commands as sp

print("content-type:  text/html")
print("")

print("<u> HDFS SETUP FOR FILE UPLOAD</u>")



print("<form action='upload.py'>")

print("""
<br />
<br />
<br />

<table border='5'>
<tr>
<td>enter FULL PATH OF FILE WHICH YOU WANT TO UPLOAD </td>
<td></td>
</tr>

<tr>
<td>ENTER FILE PATH</td>
<td><input name='PATH' /></td>
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

                                                    
