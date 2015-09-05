#!/usr/local/bin/python3

import os
import subprocess

print("1. clear")
os.system('rm -rf django_helloworld')

print("2. git clone")
os.system('git clone https://github.com/junho85/django_helloworld.git')
os.system('rm -rf django_helloworld/.git')

print("3. docker build")
os.system('docker build -t junho85/django .')

print("etc. if you want to run docker. just './run.py'")
