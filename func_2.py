
def getCalcPower2(x):
    '''
    calculate x power 2
    :param x: number to be pwoered by 2
    :return: x power 2
    '''
    #calculation = x ** 2
    #return calculation
    return x ** 2

xpower2 = getCalcPower2(5)
print(xpower2)

print(getCalcPower2(8))

l1 = [getCalcPower2(5), getCalcPower2(9)]
print(l1)

def isNumberEven(x):
    '''
    check if number is even or not
    :param x: number
    :return: True if number is even, False if not
    '''
    reminder = x % 2 #
    if reminder == 0:
        return True
    if not reminder == 0:
        return False

b = isNumberEven(9)

if isNumberEven(11):
    print('11 is even')
else:
    print('11 is odd')
    







