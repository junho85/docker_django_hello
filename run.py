#!/usr/local/bin/python3
import os
import subprocess

os.system('docker run -d -p 9999:8000 --name hello junho85/django')
ip = subprocess.check_output('docker-machine ip default', shell=True).rstrip().decode("utf-8")

port_info = subprocess.check_output('docker port hello', shell=True).rstrip().decode("utf-8")
port = port_info.split(":")[1]
print("http://%s:%s/hello" % (ip, port))
