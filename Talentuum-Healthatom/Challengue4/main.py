def getFactorial(number:int) -> int:
    if number == 0 or number == 1:
        return 1
    else:
        factorial:int = 1
        counter:int = 1
        while counter <= number:
            factorial *= counter
            counter += 1
        return factorial

def getZeroToRight(number:int) -> int:
    ZERO:str = "0"
    numberString:str = str(number)
    counter:int = 0
    for letter in numberString:
        if letter == ZERO:
            counter += 1
    return counter

try:
    numberToGetFactorial:int = -1
    while numberToGetFactorial < 0 or type(numberToGetFactorial) != int:
        print("You should to insert a positive integer number")
        numberToGetFactorial:int = int(input("Enter a number: "))
    factorial:int = getFactorial(numberToGetFactorial)
    print(factorial)
    zeroToRight:int = getZeroToRight(factorial)
    print(zeroToRight)
    
except Exception as e:
    print(f"Error happened while inserting a number: {e}")
            
        