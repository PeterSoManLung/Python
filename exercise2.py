symbol = input('please enter what symbol of operation you want to do ')

if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
    print('Error, you should enter "+", "-", "*", "/" ')
else:
    print("")
    num1 = float(input('please enter the first number: '))
    num2 = float(input('please enter the second number: '))
    if symbol == '+':
        print('%d + %d = ' %(num1,num2) + str(int(num1 + num2)))
    elif symbol == '-':
        print('%d - %d = ' %(num1,num2) + str(int(num1 - num2)))
    elif symbol == '*':
        print('%d * %d = ' %(num1,num2) + str(int(num1 * num2)))
    elif symbol == '/':
        print('%d / %d = ' %(num1,num2) + str(num1 / num2))