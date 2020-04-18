# 07-import.py
import os
import random
import subprocess

# generates 5 random numbers
for i in range(5):
    print(random.randint(1,100))

#  prints the dir cmd prompt not doing line breaks
output = subprocess.check_output('dir',shell=True)
print(output)


output = subprocess.check_output('cd',shell=True)
print(output)
# ==========================================================
