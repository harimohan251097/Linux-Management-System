#!/usr/bin/python2

import commands as sp

print("content-type:  text/html")
print("")


print("<marquee><u>WELCOME TO HADOOP SETUP</u></marquee>")



print("<form>")

print("""
<br />
<br />
<br />

<table border='5'>
<tr>
<td>What do you want to setup</td>
<td></td>
</tr>

<tr>
<td>HDFS SERVICE</td>
<td><a href='hadoop_hdfs.py'>Click to SETUP HDFS SERVICE</a></td>
</tr>


<tr>
<td>MAPREDUCE SERVICE</td>
<td><a href='hadoop_mapred.py'>click to SETUP MAPREDUCE</a></td>
</tr>

</tr>

</table>
""")


print("</form>")

