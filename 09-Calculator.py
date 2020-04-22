# 09-Calculator.py
# Simple Python Calculator
#Hong Github
def addition(x  , y):
   result =  x + y
   print('The result is: ' + str(result))

def subtraction(x , y):
    result  = x - y
    print('The result is: ' + str(result))

def multiplication(x , y):
    result = x * y
    print('The result is: ' + str(result))

def divide(x , y):
    result = x / y
    print('The result is: ' + str(result))

print('1. Addition')
print('2. Subtration')
print('3. Multiplication')
print('4. Division')
print('5. Exit')

while True:
    choice = int(input('Enter Choice (1-5): '))
    if (choice >=1 and choice <= 4):
        print('Enter two numbers')
        num1 = int(input('Enter first number:  '))
        num2 = int(input('Enter second number: '))
        if choice == 1:
          addition(num1,num2)
        elif choice == 2:
          subtraction(num1,num2)
        elif choice == 3:
          multiplication(num1,num2)
        else:
          divide(num1,num2)
    elif choice == 5:
        break
    else:
        print('You entered wrong choice!')
        
# =======================================================