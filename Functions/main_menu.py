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
            #basic.calc.py
            pass
        
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

main_menu()
        