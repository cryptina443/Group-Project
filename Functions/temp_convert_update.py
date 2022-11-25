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
        print('main_menu()')
    elif temp_scales.lower() == 'exit':
        print('\nExiting...\nGood-bye!\n')
        exit()
    else: 
        print('Not an option')
        get_temp()

    


def temprature_convertion(temp_scales):

    try:
        temp_source = float(input("What is the temperature you are trying to convert: " ))
    except ValueError:
        print('Temperature must be a number!')
        temprature_convertion(get_temp())

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
            print('main_menu()')
        else:
            print('Not a valid option!')
            go_again()
    except TypeError:
        print('Error')

