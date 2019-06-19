#!/usr/bin/python
import subprocess
path = '.'
size = subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
print("Directory size: " + size)
