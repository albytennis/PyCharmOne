# 08-Functions.py
import random

def my_print(string):
     print(string)

     
def hello_world_print():
    print('Hello world')

def getNumber(x):
    if x == 1:
        return '      The number is 1'
    elif x ==2:
        return '      The number is 2'
    elif x ==3:
        return '      The number is 3'
    elif x ==4:
        return '      The number is 4'
    elif x ==5:
        return '      The number is 5'
    

a='football'
my_print(a)

hello_world_print()

for i in range(0,5):
   random_number = random.randint(1,5)
   a = 'pick number: '+str(i+1)+')'
   my_print(a)
   pick = getNumber(random_number)
   print(pick)

# ==========================================