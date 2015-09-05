#!/usr/local/bin/python3
import os
import subprocess

os.system("docker rm -f $(docker ps -a -q)")
