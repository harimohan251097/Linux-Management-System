#!/usr/bin/python2

print("content-type:  text/html\n")
#print("")

import commands as sp

print("<u> <center><h1>Welcome to our STAAS Setup</h1> </center> </u></br>")
print("""
<form action='cloud_staas_ansible.py'>
<table border='5' width=70%>
<tr>
<td> Enter your IP: </td>
<td> <input type='text' value=' ' name='ip' /></br></br> </td>
</tr>

<tr>
<td> Name of Directory: </td>
<td> <input type='text' value=' ' name='name' /></br></br> </td>
</tr>

<tr>
<td> Root Password: </td>
<td> <input type='password' value=' ' name='password' /></br></br> </td>
</tr>

<tr>
<td> Size : </td>
<td>100Mb <input type='range' min='100' max='1024' name='size' value=' ' /> 1024Mb</br></br> </td>
</tr>
</form>
</table>
</br></br>
"""
)
#print(" <input type='text' value=' ' name='ip' /></br></br>")
#print("Enter your folder name: <input type='text' value=' ' name='name'/> </br> </br>")
#print("Size </br>100Mb <input type='range' min='100' max='1024' name='size' value=' ' /> 1024Mb  </br></br>")
print("<input type='submit' name='submit' value='Submit' />") 
