number1 = float(input('please enter first number; '))
number2 = float(input('please enter second number; '))

operation = input("please enter the operation you would like to use: ")

if operation == '+':
    print( '{} + {} = '.format(number1, number2))
    print(number1 + number2)

elif operation == 'add':
    print( '{} + {} = '.format(number1, number2))
    print(number1 + number2)

elif operation == '-':
    print( '{} - {} = '.format(number1, number2))
    print(number1 - number2)

elif operation == '*':
    print( '{} * {} = '.format(number1, number2))
    print(number1 * number2)

elif operation == '/':
    print( '{} / {} = '.format(number1, number2))
    print(number1 / number2)

else:
    print("Invalid inputs")
