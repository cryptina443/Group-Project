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





def get_choice():
    '''Get the user's choice'''

    choice = input('Choose an option: ').lower()
    if choice == 'add':
        add_nums()
        print_calc_options()
        get_choice()

    elif choice == 'sub':
        print('\nSubtraction')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 - num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
        print_calc_options()
        get_choice()

    elif choice == 'mult':
        print('\nMultiplication\n')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 * num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
        print_calc_options()
        get_choice()

    elif choice == 'div':
        print('\nDivision\n')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 / num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
        print_calc_options()
        get_choice()

    elif choice == 'exp':
        print('\nExponent\n')
        num1 = float(input('Enter the base number: '))
        num2 = float(input('Enter the exponent: '))
        res = num1 ** num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
        print_calc_options()
        get_choice()

    elif choice == 'back':
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

print_calc_options()
get_choice()