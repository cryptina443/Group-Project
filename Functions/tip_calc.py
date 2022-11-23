def split_check(total):
    amt_ppl = int(input('Between how many people will you be splitting this check? '))
       
    tip = float(input('What percentage would you like to tip? '))

    tip = tip / 100
    tip_amt = total * tip / amt_ppl
    print(f'The tip amount per person would be ${tip_amt:.2f} making the new total of ${tip_amt * amt_ppl + total:.2f}')
    
def non_split():
    tip = float(input('What percentage would you like to tip? '))
    tip = tip / 100 
    tip_amt = total * tip
    print(f'The tip amount would be {tip_amt:.2f} making the new total {total + tip_amt:.2f}')
        



    
if __name__  == '__main__':

    print('Welcome to the Tip Calculator!')

    total = float(input('What is the total? '))
    choice = input('Will you splitting the check? Yes/No: ')

    if choice == 'yes':
        split_check(total)
    elif choice == 'no':
        non_split(total)
    else:
        print('Invalid choice. Try again!')


        

