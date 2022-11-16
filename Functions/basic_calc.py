def print_calc_options():
    '''prints calculator options'''


    print('\nOPTIONS\n')
    print('(add) Addition')
    print('(sub) Subtraction')
    print('(mult) Multiplication')
    print('(div) Division')
    print('(exp) Exponents\n')


def get_choice():
    '''Get the user's choice'''

    choice = input('Choose an option: ').lower()
    if choice == 'add':
        pass
    elif choice == 'sub':
        pass
    elif choice == 'mult':
        pass
    elif choice == 'div':
        pass
    elif choice == 'exp':
        pass
    else:
        print('Not an option!')
        get_choice()