def main_menu():
    '''Show the main menu options'''


    print('\n<Multi> Calculator!\n')
    print('MENU OPTIONS')
    print('(1) Basic Calculator')
    print('(2) Tip Calculator')
    print('(3) Temperature Converter')
    print('(4) Close program')

    try:
        user_choice = int(input('\nChoose function: ')) ##get users choice for calculator options

        if user_choice == 1:
            simple_calc() ## call the simple calculator function
            
        
        elif user_choice == 2:
            tip_menu() ## calls the tip calculator

        elif user_choice == 3:
            temp_calc() ## calls the temperature calculator
            
        elif user_choice == 4:
            print('Closing Calculator....\nGoodbye')
            exit() ## clean program termination

    except ValueError:
        main_menu() ## restart the main menu if wrong value is given
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit() ## clean termination for keyboard interrupt

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
        res = num1 + num2  ## assign result to res to be used later
        print(f'result: {res}\n\n')
        input('press enter to continue')
    except ValueError: ## input validation
        print('Must be a number!') 
        add_nums()
    except KeyboardInterrupt: #clean exit
        print('Exiting program...\nGoodbye!')
        exit()


def sub_nums():
    '''Get two numbers and subtract the second from the first'''

    
    try:  
        print('\nSubtraction')   ## get the two numbers and subtract them
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        res = num1 - num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
    except ValueError: ##input validation
        print('Must be a number!')
        sub_nums()
    except KeyboardInterrupt: ## clean exit
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
    except ValueError: ## inputn validation
        print('Must be a number!')
        mult_nums()
    except KeyboardInterrupt: ## clea exit
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
    except ZeroDivisionError: ## cant break meeeeeee 
        print('Dividing by zero is illegallll')
        div_nums()

def exp_nums():
    '''Get two numbers. Raise the first number to the power of the second number'''

    try:
        print('\nExponent\n')
        num1 = float(input('Enter the base number: ')) ## the first number given will the be number used for the base
        num2 = float(input('Enter the exponent: ')) ## the second number is the power we raise that number to
        res = num1 ** num2
        print(f'Result: {res}\n\n')
        input('press enter to continue')
    except ValueError: ## input validation
        print('Must be a number!')
        exp_nums()
    except KeyboardInterrupt: ## clean exit
        print('Exiting program...\nGoodbye!')
        exit()


def get_choice():
    '''Get the user's choice'''
    try: ## get the users choice and call the appropriate function
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
            main_menu() ## user returns to main menu when back is entered
            
        elif choice == 'exit':
            print('\nExiting...\nGood-bye!\n')
            exit() ## clean exit
        elif choice == '':
            print_calc_options()
            get_choice() ## blank choice catch
        else:
            print('Not an option!')
            get_choice() #input validation
    except KeyboardInterrupt:
        print('Exiting program...\nGoodbye!')
        exit()

def simple_calc():
    '''Run the calculator function'''
    print('\nBasic Calculator') ##greetingsss
    print_calc_options() #prints calc menu
    get_choice() ##gets users choice for calculator, and then calls functions as needed. 


def temp_menu():
    '''Prints menu for temperature converter'''

    print('\nTemperature Converter')
    print('(f) Fahrenheit')
    print('(c) Celcius')
    print('(back) Return to main menu')
    print('(exit) Exit program\n')

def temp_calc():
    '''Actual temperature converter'''


    temprature_convertion(get_temp()) ##temperature conversion will use the value passed from get_temp to use the correct formula. 
    go_again() ## repeat. 
    




def get_temp():
    '''Shows temperature conversion options and recieves unit of temperature'''
    
    temp_menu() #show menu 
    temp_scales = input('Select your choice: ')
    
    if temp_scales.lower() == 'f':    ## lower() will allow f or F to be entered. 
        return temp_scales
    elif temp_scales.lower() == 'c': ## same as f 
        return temp_scales
    elif temp_scales.lower() == 'back': ## lower allows further use of shenanigan spellings. 
        main_menu()
    elif temp_scales.lower() == 'exit': ## leaves... byeeeee
        print('\nExiting...\nGood-bye!\n')
        exit() ## using exit() specifically tells the program to end. 
    else: 
        print('Not an option')
        get_temp() ## invalid input check, if an invalid option is made, the program will return the user to the start. 

    


def temprature_convertion(temp_scales):
    global temp_source ## temp source is first used within the function, using global allows it to be called from the main program. 
    try:
        temp_source = float(input("What is the temperature you are trying to convert: " )) ## automatically convert input to float, IF valid type. 
    except ValueError:
        print('Temperature must be a number!')
        temprature_convertion(get_temp())    ## If invalid type, restart the process from the beginning. 

    if temp_scales == "f": ##if temp scale was f, we use the fahr. to Celc. formula. 
        res = (temp_source - 32.0) * (5.0/9.0)
        print(f'{temp_source} degrees F is {res:.2f} degrees C')
    elif temp_scales == "c": ## Convert celcius to fahrenheit. 
        res = (temp_source * (9.0/5.0)) + 32.0
        print(f'{temp_source} degrees C is {res:.2f} degrees F')

        


def go_again():
    
    repeat = input('Convert another? (y/n) ') ## asks user if they would like to convert another temperature. 
    try:
        if repeat.lower() == 'y': ##if yes, call the temp calc function again
            temp_calc()
        elif repeat.lower() == 'n': ##if no, call the main menu function
            main_menu()
        else:
            print('Not a valid option!')
            go_again()
    except TypeError:
        print('Error') ## ?? We broke it, and then we fixed it, but we never commented why until now. ¯\_(ツ)_/¯

def tip_menu():
    '''Accepts input for tip'''
    choice = None
    while choice not in ('y','n'):
        choice= input('\nWill you be splitting the check? (y/n): ')
        #depending on choice, it will call appropriarte function
        #or ask to try again
        if choice.lower() == 'y':
            split_check()
        elif choice.lower() == 'n':
            non_split()
        else:
            print('Invalid choice. Try again!')


def split_check():
    '''Gets amount of people check will be split between'''
    amt_ppl = input('\nBetween how many people will you be splitting this check? ')
    #checking if amount of people is a number if yes it will pass that number to split_tip()
    if amt_ppl.isdigit():
        amt_ppl = int(amt_ppl)
        if amt_ppl > 0: ## split checks must be divided between a positive amount of people. 
            split_tip(amt_ppl)
        else:
            print('Not a valid amount. Enter a positive total.')
            split_check()
    #if not it will call the function again and ask the questin again until an 
    #appropriate value is inserted
    else:
        print('Please enter an approriate value.')
        split_check()



def split_tip(amt_ppl): 
    '''Calculates tip if total is split between 2 or more people'''
    try:
        
        total = float(input('\nWhat is the total of the check? '))
        #validating that total cannot be a negative number
        #if yes it will recall, and ask question again
        if total <= 0:
            print('Not a valid amount. Enter a positive total.')
            split_tip(amt_ppl)
        else:
            tip=input('\nWhat percentage would you like to tip? ')
            while tip.isdigit()==False:
                print('Please enter an appropriate value.')
                tip=input('\nWhat percentage would you like to tip? ')
                  
            
            tip = float(tip) ## convert input to float
            tip = tip / 100 ## divide the number by 100 to get the percentage value
            tip_amt = (total * tip) / amt_ppl ## tip amount calculation goes here
            total_split = total / amt_ppl 
            print(f'\nEach person would pay ${total_split:.2f} + tip amount of ${tip_amt:.2f}')
            print(f'The new total is ${tip_amt * amt_ppl + total:.2f}')
            re_cal_tip()
            
            

    except ValueError:
        print('Please insert an appropriate amount.')
        split_tip(amt_ppl) ##restart process if an incorrect input is given


def non_split():
    '''Calculates check without splitting'''
    try:
        total = float(input('\nWhat is the total of the check? '))
        if total <= 0: ##input validation for an incorrect check amount
            print('Not a valid amount. Enter a positive total.')
            non_split()
        else:
            tip=input('\nWhat percentage would you like to tip? ')
            while tip.isdigit()==False: ## if string is anything but a digit, it will continue to ask for the tip percentage. 
                print('\nPlease enter an appropriate value.')
                tip = input('\nWhat percentage would you like to tip? ')
    
            tip = float(tip) 
            tip = tip / 100
            tip_amt = total * tip #calculating tip
            print(f'\nThe tip amount would be ${tip_amt:.2f} making the new total ${total + tip_amt:.2f}') #displaying tip and total
            re_cal_tip()
        
    except ValueError:
        print('\nPlease insert an appropriate value.')
        non_split()

    

def re_cal_tip():
    '''Ask if the user wants to calculate another tip amount'''
    
    ans = None
    while ans not in ('y','n'): ## the only acceptable choices
        ans = input('\nWould you like to calculate the tip again? (y/n) ')
        if ans == 'y': ## if yes, recalls the tip menu function
          tip_menu()
        elif ans ==  'n': ## if no, go back to the main menu for further options 
          print('Exiting program. Back to Main Menu')
          main_menu()
        else:
          print('\nInvalid input. Please try again.')
          re_cal_tip() ##input validation


if __name__ == '__main__':
    main_menu()