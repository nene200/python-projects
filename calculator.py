instruction  = """"Enter 'add' for addition\n
Enter 'subtract' for subtraction\n 
Enter 'multiply' for multiplication\n
Enter 'divide' for division\n
Enter 'modulus' for remainder\n
Enter 'exponent' for raise to power\n"""

def add(n1, n2):
    sum = n1 + n2
    return sum

def subtract(n1, n2):
    sum = n1 - n2
    return sum 
    
def multiply(n1, n2):
    sum = n1 * n2
    return sum

def divide(n1, n2):
    sum = n1 / n2
    return sum

def modulus(n1, n2):
    sum = n1 % n2
    return sum

def  exponent(n1, n2):
    sum = n1 ** n2
    return sum

while True:
    try:
        while True:
            command = input('Enter command: ')

            if command == 'exit':
                break
            
            n1 = float(input('Enter first number: '))
            n2 = float(input('Enter second number: '))

            if command == 'add':
                print(add(n1, n2), '\n')

            elif command == 'subtract':
                print(subtract(n1, n2), '\n')

            elif command == 'multiply':
                print(multiply(n1, n2), '\n')

            elif command == 'divide':
                print(divide(n1, n2), '\n')

            elif command == 'modulus':
                print(modulus(n1, n2), '\n')

            elif command == 'exponent':
                print(exponent(n1, n2), '\n')

            else:
                print('none')

    except ValueError:
        print("Please enter a number")
        

