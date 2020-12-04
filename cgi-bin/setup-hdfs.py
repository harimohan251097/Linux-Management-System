#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")


print("welcome to hdfs page")
print("<br />")

print("""
<form action='setup-hdfs-cluster.py'>
<br />
No. Master NN <input type='text' name='nm' />
<br />
No. Slave DN <input type='text' name='ns' />
<br />
<input type='submit' />
<br />
</form>
""")



