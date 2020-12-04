#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")


print("Welcome to our paas service")

print("""
<form action='docker_paas_setup.py'>
Enter ur platform name 
<select name='paasname'>
<option>python2</option>
<option>python3</option>
<option>java</option>
<option>scala</option>
</select>
<input type='submit' />
</form>
""")


