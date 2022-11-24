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
            simple_calc()
            
        
        elif user_choice == 2:
            #Tip Calculator
            pass
        elif user_choice == 3:
            temp_calc()
            pass
        elif user_choice == 4:
            print('Closing Calculator....\nGoodbye')
            exit()

    except ValueError:
        main_menu()
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()

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
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()

def simple_calc():
    '''Run the calculator function'''
    print('\nBasic Calculator')
    print_calc_options()
    get_choice()


def temp_menu():
    print('\nTemperature Converter')
    print('(f) Fahrenheit')
    print('(c) Celcius')
    print('(back) Return to main menu')
    print('(exit) Exit program\n')

def temp_calc():
    temprature_convertion(get_temp())
    go_again()
    




def get_temp():
    
    temp_menu()
    temp_scales = input('Select your choice: ')
    
    if temp_scales.lower() == 'f':
        return temp_scales
    elif temp_scales.lower() == 'c':
        return temp_scales
    elif temp_scales.lower() == 'back':
        main_menu()
    elif temp_scales.lower() == 'exit':
        print('\nExiting...\nGood-bye!\n')
        exit()
    else: 
        print('Not an option')
        get_temp()

    


def temprature_convertion(temp_scales):


    temp_source = float(input("What is the temperature you are trying to convert: " ))
    
    if temp_scales == "f":
        res = (temp_source - 32.0) * (5.0/9.0)
        print(f'{temp_source} degrees F is {res:.2f} degrees C')
        
    
    elif temp_scales == "c":
        res = (temp_source * (9.0/5.0)) + 32.0
        print(f'{temp_source} degrees C is {res:.2f} degrees F')

        


def go_again():
    
    repeat = input('Convert another? (y/n) ')
    try:
        if repeat.lower() == 'y':
            temp_calc()
        elif repeat.lower() == 'n':
            main_menu()
        else:
            print('Not a valid option!')
            go_again()
    except TypeError:
        print('Error')

main_menu()