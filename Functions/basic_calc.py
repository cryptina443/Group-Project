def print_calc_options():
    '''prints calculator options'''


    print('\nOPTIONS')
    print('(add) Addition')
    print('(sub) Subtraction')
    print('(mult) Multiplication')
    print('(div) Division')
    print('(exp) Exponents')
    print('(back) Go back to main menu')
    print('(exit) Exit the program\n')

def add_nums():
    '''Get two numbers and add them together'''

    print('\nAddition')
    try:

        
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 + num2
        print(f'result: {res}\n\n')
        input('press enter to continue')
    except ValueError:
        print('Must be a number!')
        add_nums()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()


def sub_nums():
    '''Get two numbers and subtract the second from the first'''

    
    try:  
        print('\nSubtraction')  
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 - num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
    except ValueError:
        print('Must be a number!')
        sub_nums()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()
    

def mult_nums():
    '''Get two numbers and multiply them together'''
    
    try:
        print('\nMultiplication\n')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 * num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
    except ValueError:
        print('Must be a number!')
        mult_nums()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()
    
def div_nums():
    '''Get two numbers and divide the second from the first'''

    try:
        print('\nDivision\n')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 / num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
    except ValueError:
        print('Must be a number!')
        div_nums()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()
    except ZeroDivisionError:
        print('Dividing by zero is illegallll')
        div_nums()

def exp_nums():
    '''Get two numbers. Raise the first number to the power of the second number'''

    try:
        print('\nExponent\n')
        num1 = float(input('Enter the base number: '))
        num2 = float(input('Enter the exponent: '))
        res = num1 ** num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
    except ValueError:
        print('Must be a number!')
        exp_nums()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()


def get_choice():
    '''Get the user's choice'''
    try:
        choice = input('Choose an option: ').lower()
        if choice == 'add':
            add_nums()
            print_calc_options()
            get_choice()

        elif choice == 'sub':
            sub_nums()
            print_calc_options()
            get_choice()

        elif choice == 'mult':
            mult_nums()
            print_calc_options()
            get_choice()

        elif choice == 'div':
            div_nums()
            print_calc_options()
            get_choice()

        elif choice == 'exp':
            exp_nums()
            print_calc_options()
            get_choice()

        elif choice == 'back':
            #main_menu_function
            pass
        elif choice == 'exit':
            print('\nExiting...\nGood-bye!\n')
            exit()
        elif choice == '':
            print_calc_options()
            get_choice()
        else:
            print('Not an option!')
            get_choice()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()

def simple_calc():
    '''Run the calculator function'''

    print_calc_options()
    get_choice()

