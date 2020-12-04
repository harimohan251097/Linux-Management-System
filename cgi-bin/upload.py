#!/usr/bin/python2

import commands as sp
import cgi
print("content-type:  text/html")
print("")

form = cgi.FieldStorage()
PATH = form.getvalue('PATH')

print("""<form action='hdfs_formed1.py>

<br />
<br />
<br />

<table border='5'>
<tr>
<td>
""")

cmd="hadoop fs -put {}".format(PATH)
print(" {} </td> </tr>".format(cmd))
output=sp.getstatusoutput(cmd)
print("<tr> <td> file uploaded </tr></td>".format(output))

print("""
</table>
""")
print("</form>")


