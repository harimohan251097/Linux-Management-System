#!/usr/bin/python2

print("content-type:  text/html")
print("")

import commands as sp
import cgi
#print("")

print("hii --started\n")
form=cgi.FieldStorage()
c_ip = form.getvalue('ip')
mk_name=form.getvalue('name')
size=form.getvalue('size')
password=form.getvalue("password")
print("value taken\n")
print("{} , {} , {} ".format(mk_name, size,c_ip))

fh=open("/code/cloud_staas_ansible.txt", 'w')
fh.write("""
size: {}
mk_name: {}
""".format(size, mk_name))

fh=open("/code/hosts", 'a')
fh.write("""
[grp]
{} ansible_ssh_user=root  ansible_ssh_pass={}
""".format(c_ip,password))

st = sp.getoutput("sudo ansible-playbook /ws/cloud_staas.yml -i /code/hosts")
print(st)
