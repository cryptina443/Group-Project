def temp_calc():
    temprature_convertion(get_temp())
    go_again()

def get_temp():
    temp_scales = input("Select (Fahrenheit) or (Celsius) as (F) or (C) or (back) to return: " )
    if temp_scales.lower() == 'f':
        return temp_scales
    elif temp_scales.lower() == 'c':
        return temp_scales
    elif temp_scales.lower() == 'back':
        print('Back')
        get_temp()
    else: 
        print('Not an option')
        get_temp()

    


def temprature_convertion(temp_scales):


    temp_source = float(input("What is the temperature you are trying to convert: " ))
    res = 0
    if temp_scales == "f":
        res = (temp_source - 32.0) * (5.0/9.0)
        
    
    elif temp_scales == "c":
        res = (temp_source * (9.0/5.0)) + 32.0

        
    
    if temp_scales == "f":
        print(f'{temp_source} degrees F is {res:.2f} degrees C')
    elif temp_scales == "c":
        print(f'{temp_source} degrees C is {res:.2f} degrees F')
  

def go_again():
    
    repeat = input('Convert another? (y/n) ')
    try:
        if repeat.lower() == 'y':
            temp_calc()
        elif repeat.lower() == 'n':
            print('main menu')
        else:
            print('Not a valid option!')
            go_again()
    except TypeError:
        print('Error')



#while temp_scales not in ("F", "C"):
#    temp_scales = input("Select (Fahrenheit) or (Celsius) as (F) or (C): ") # The pourpuse of this loop is to avoid closing the program 
#    print("Your selection is invalid and it needs to be (F) or (C)")        #and keep asking the user to enter the letters F or C otherwise it will keep printing
#
#temp_source = float(input("What is the temperature you are trying to convert: " ))
#
#defined_funtion = temprature_convertion(temp_scales, temp_source)
#
##This if elif statement is to print the correct information on display. If instead we use the print in one line like this print(source_temp, "degrees", temp_scales, "is", defined_funtion, "degrees", temp_scales) then the output
##with the letters indicating F or C will repeat and not print correctly. Doing an If elif statement we can change the output depending on the users input.
#if temp_scales == "F":
#    print(f'{temp_source} degrees F is {defined_funtion:.2f} degrees C')
#elif temp_scales == "C":
#    print(f'{temp_source} degrees C is {defined_funtion:.2f} degrees F')

go_again()