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
        split_tip(amt_ppl)
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
                #FIXME: missing code to make percentage question appear again :)   
            
            tip = float(tip)
            tip = tip / 100
            tip_amt = total * tip / amt_ppl
            total_split = total / amt_ppl
            print(f'\nEach person would pay ${total_split:.2f} + tip amount of ${tip_amt:.2f}')
            print(f'The new total is ${tip_amt * amt_ppl + total:.2f}')
            re_cal_tip()
            
            

    except ValueError:
        print('Please insert an appropriate amount.')
        split_tip(amt_ppl)


def non_split():
    '''Calculates check without splitting'''
    try:
        total = float(input('\nWhat is the total of the check? '))
        if total <= 0:
            print('Not a valid amount. Enter a positive total.')
            non_split()
        else:
            tip=input('\nWhat percentage would you like to tip? ')
            while tip.isdigit()==False:
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
    
  ans = None
  while ans not in ('y','n'):
    ans = input('\nWould you like to calculate the tip again? (y/n) ')
    if ans == 'y':
      tip_menu()
    elif ans ==  'n':
      print('goodbye.. exiting program. back to Main Menu()')
    else:
      print('\nInvalid input. Please try again.')
      re_cal_tip()

if __name__  == '__main__':

    print('Welcome to the Tip Calculator!')
    tip_menu()


        

