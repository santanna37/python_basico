import random
import time
''' 
try:
    num=int(input('Enter a number between 1 and 30: '))
    num1 = 30/num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err,num, "Bad Value not between 1 and 30!")
except:
    print("Invalid Input!")
else:
    print("30 divided by",num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")

'''
#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed 

import random
import time


def numero_dado():
    jogar = 's'
    while jogar == 's':
        try: 
            numero = int(input('Jogo de dados - escolha um numero entre 1 e 6:   ->  '))
            numero = numero if numero in [1,2,3,4,5,6] else int(input(' entre 1 e 6:  ->>'))
            print('rodando o dado .... ')
            time.sleep(2)
            print('....')
            time.sleep(1)
            x = int(random.randint(1,6))
            print(f'o dado caiu no numero {x}')
            time.sleep(1)
            (print('voce acertou') if x == numero else print('voce errou'))
        except Exception as e:
            print(f'{e}, ocorreu um erro')
        
        finally:
            jogar = str(input(f' quer jogar novamente? s/n  -> ').lower())

numero_dado()