def print_calc_options():
    '''prints calculator options'''


    print('\nOPTIONS\n')
    print('(add) Addition')
    print('(sub) Subtraction')
    print('(mult) Multiplication')
    print('(div) Division')
    print('(exp) Exponents\n')
    print('(back) Go back to main menu')
    print('(exit) Exit the program')


def get_choice():
    '''Get the user's choice'''

    choice = input('Choose an option: ').lower()
    if choice == 'add':
        nums = []
        num = input('Enter a number (press enter when done): ')
        while num != '':
            if num.isdigit():
                nums.append(int(num))
                num = input('Enter a number (press enter when done): ')
            else:
                print('Not a number!')
                num = input('Enter a number (press enter when done): ')

        print(f'Result: {sum(nums)}')
        print('\n')
        get_choice()

    elif choice == 'sub':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        res = num1 - num2
        print(f'Result: {res}'
        get_choice()
        
    elif choice == 'mult':
        pass
    elif choice == 'div':
        pass
    elif choice == 'exp':
        pass
    elif choice == '':
        pass
    elif choice == 'exit':
        print('Good-bye')
        exit()
    else:
        print('Not an option!')
        get_choice()
