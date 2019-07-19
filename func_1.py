
import random

print( random.randint(1, 10) )

# method - from module somebody
# function - from no one
# no repitition
# share code

def sayHello():
    '''
    print greeting
    :return:
    '''
    print('say hello')
if 3 > 1:
    print()

def greet(name = 'mystery', fcolor = 'Yellow' ):
    '''
    Greet the person and print favorite color    
    :param name: the user name 
    :param fcolor: favorite color
    :return: 
    '''
    print(f'hello {name} favorite color {fcolor}')

greet('itay', 'Green')
greet(3.5)
greet()
greet(fcolor='Red')












