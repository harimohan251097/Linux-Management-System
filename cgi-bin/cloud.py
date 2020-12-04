#!/usr/bin/python2

import commands
import cgi

print("content-type: text/html")
print("")
'''print("""
<head>
<style>
first{
 background-color: #ccc;
 font-family: Arial, Helvetica, sans-serif;
 font-size: 36px;
 }
 
 text{
 background-color: #f1f1f1;
  color: #f9f9f9;
  font-style: italic;
  }
""")'''

print("<center><i><h1 style='background-color:#ccc' ></br> WELCOME TO OUR CLOUD SETUP </br></br></i></center>")

print("""
<p style='background-color:#f2f2f2'>
</br>
<table border='5' align = 'center' width='70%' height='60%' cellpadding='30px' margin-left='20px' >
<tr>
<td> SAAS </td>
<td><a href='cloud_saas.py'> Click here to set up </a>  </td>
</tr>

<tr>
<td> STAAS </td>
<td><a href='cloud_staas.py'> Click here to set up </a>  </td>
</tr>

<tr>
<td> CAAS </td>
<td><a href='docker.py'> Click here to set up </a>  </td>
</tr>

<tr>
<td> PAAS </td>
<td><a href=''> Click here to set up </a>  </td>
</tr>

</table>
</p>
""")

