def tip_menu():
    '''Accepts input for tip'''

    total = float(input('\nWhat is the total of the check? '))
    choice = input('\nWill you be splitting the check? (y/n): ') # should i  have an exit choice in here

    if choice.lower() == 'y':
        split_check(total)
    elif choice.lower() == 'n':
        non_split(total)
    else:
        print('Invalid choice. Try again!')



def split_check(total):
    '''Calculates check if split between 2 or more people'''

    amt_ppl = int(input('Between how many people will you be splitting this check? '))
       
    tip = float(input('\nWhat percentage would you like to tip? '))

    tip = tip / 100
    tip_amt = total * tip / amt_ppl
    print(f'\nThe tip amount per person would be ${tip_amt:.2f} making the new total of ${tip_amt * amt_ppl + total:.2f}')
    re_cal_tip()

    
def non_split(total):
    '''Calculates check without splitting'''

    tip = float(input('What percentage would you like to tip? '))
    tip = tip / 100 
    tip_amt = total * tip
    print(f'\nThe tip amount would be ${tip_amt:.2f} making the new total ${total + tip_amt:.2f}')
    re_cal_tip()

def re_cal_tip():
    ans = input('\nWould you like to calculate the tip again? (y/n) ')
    if ans == 'y':
        tip_menu()
    elif ans ==  'n':
        print('goodbye.. exiting programmain menu')
    else:
        print('Invalid input. Please try again.')



if __name__  == '__main__':

    print('Welcome to the Tip Calculator!')
    tip_menu()


        

