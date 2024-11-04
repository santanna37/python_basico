"""is_rain = True
is_cold = True

def condicions(this_rain: bool = False, this_cold: bool = False)->str:
    rain = this_rain
    cold = this_cold 

    if rain and cold:
        return f'Bring umbrella and jacket'
    elif rain and not(cold):
        return f'Bring umbrella'
    elif not(rain) and cold:
        return f'Bring jacket'
    else:
        return f'lets go'

print(condicions(this_rain= is_rain, this_cold= is_cold))

"""


# exercice 2 
''' 
print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def calculator(temp:float = None) -> str:
    num1 = float(input('digiti first number: '))
    num2 = float(input('digit seconde number: '))
    operation = str(input('digit the operatation symbol: '))
    
    if temp is not(None):
        temp_fahre = float((temp*9/5)+32)
        print(f" the conversion Celsius / fahrennheit this : {temp_fahre} F°")

    if operation == '+':
        return f' the sum is :{num1 + num2}'
    elif operation == '-':
        return f'the subtrain is: {num1 - num2}'
    elif operation == '*':
        return f' the multiplication is: {num1 * num2}'
    elif operation == '/':
        return f' the divison is: {num1 / num2}'


print(calculator(temp=23))

''' 



def num_days(month):

    if month in ['jan','mar','may','jul','aug','oct','dec'] :
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month in ['jun','sep','nov']:
        print('number of days in',month,'is',30)


num_days('jun')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
