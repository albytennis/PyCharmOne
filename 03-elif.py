#03-elif.py
x = input('Specify any number you want:  ')
x = int(x)
print(x)
if x > 0 and x < 10:
    print('input number: ' + str(x) + ' is between 0 and 10')
elif x> 9:
    print('input number: ' + str(x) + ' is greater than 9')
elif x == 0:
    print(x,' zero number entered. Comma to separate number,string')
else:
    print('input number: ' + str(x) + ' is smaller than zero')
# =====================================================================