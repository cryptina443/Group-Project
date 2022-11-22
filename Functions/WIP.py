def main_menu():
    '''Show the main menu options'''


    print('\n\n\n<Multi> Calculator!\n')
    print('MENU OPTIONS')
    print('(1) Basic Calculator')
    print('(2) Tip Calculator')
    print('(3) Temperature Converter')
    print('(4) Close program')

    try:
        user_choice = int(input('\nChoose function: '))

        if user_choice == 1:
            print_calc_options()
            get_choice()
            
        
        elif user_choice == 2:
            #Tip Calculator
            pass
        elif user_choice == 3:
            #temp converter
            pass
        elif user_choice == 4:
            print('Closing Calculator....\nGoodbye')
            exit()

    except ValueError:
        main_menu()

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


def get_choice():
    '''Get the user's choice'''

    choice = input('Choose an option: ').lower()
    if choice == 'add':
        print('\nAddition\n')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 + num2
        print(f'result: {res}\n\n')
        input('press enter to continue')
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
        main_menu()
    elif choice == 'exit':
        print('\nExiting...\nGood-bye!\n')
        exit()
    elif choice == '':
        print_calc_options()
        get_choice()
    else:
        print('Not an option!')
        get_choice()



main_menu()