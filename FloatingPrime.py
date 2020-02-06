def isPrime( num ):
    num = int( num )
    if num <= 1:
        return False
    else:
        for i in range( 2 , num ):
            if num % i == 0:
                return False
        return True
    
def decimalPlaceCount( num ):
    stringNum = str(num)
    count = 1 
    for digit in str(num):
        if digit == '.':
            break
        
        count += 1
        
    return len(stringNum) - count

def moveDecimal( num ):
    numberOfDecimalPlace = decimalPlaceCount( num )
    
    if numberOfDecimalPlace > 12:
        return None
    
    for i in range( numberOfDecimalPlace ):
        num *= 10
        checkPrime = isPrime( num )
        
        if checkPrime:
            return True
        
    return False

def isFloatingPrime( inputNum ):
    floatingPrime = moveDecimal( inputNum )
    
    if floatingPrime:
        print("TRUE")
    elif not floatingPrime:
        print("FALSE")
    else:
        print("Decimal place longer than 12")

if __name__ == '__main__':
    while( True ):
        try:
            inputNum = float(input("Input Float: "))
            
            if inputNum == 0.0:
                print('end of program')
                break
            
            isFloatingPrime( inputNum )
        except ValueError:
            print('this is not a number')
    
