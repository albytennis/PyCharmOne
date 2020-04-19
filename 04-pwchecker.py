#04-pwchecker.py
# weird if running idle must say .py(3.7.4) bombs in python2
# going to push this comment
password = 'Rainbow'

while True:
    x = str(input('Enter the password: '))
    if x == password:
        break
    
print('Password correct')
print('Access granted')
# ==============================================================