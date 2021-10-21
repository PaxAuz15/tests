import random

ZERO:int = 0
FOUR:str = "4"
RESTRICTION:int = 10**100

def getRandomValues(valueCheck:int) -> list:
    values:list = []
    randomValue:int = 0
    while values!=None:
        randomValue:int = random.randint(ZERO,valueCheck)
        verifiedValue:bool = verifyFours(randomValue)
        if verifiedValue == True:
            otherValue:int = valueCheck - randomValue
            verifiedOtherValue:bool = verifyFours(otherValue)
            if verifiedOtherValue == True:
                values.append(randomValue)
                values.append(otherValue)
                return values
        
def verifyFours(number:int) -> bool:
    valueString:str = str(number)
    for letter in valueString:
        if letter == FOUR:
            return False
    return True   

def restriction(number:int) -> bool:
    if number >ZERO:
        if number <= RESTRICTION:
            return True
        else:
            return False
    else:
        return False

try:
    valueCheck:int = -1
    verificationConstraint:bool = False
    while verificationConstraint == False:
        print("You should to insert a positive integer number and less than 10^100")
        valueCheck:int = int(input("Enter a check value: "))
        verificationConstraint:bool = restriction(valueCheck)
    
    randomsValues:list = getRandomValues(valueCheck)
    print(randomsValues)
    
except Exception as e:
    print(f"Error happened while inserting a number: {e}")