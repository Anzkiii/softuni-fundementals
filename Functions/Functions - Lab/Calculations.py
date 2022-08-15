
operator = input()
firstNum = int(input())
secondNum = int(input())

def calculation(operator_, numOne, numTwo):
    if operator_ == "subtract":
        return int(numOne - numTwo)
    elif operator_ == "add":
        return int(numOne + numTwo)
    elif operator_ == "divide":
        return int( numOne / numTwo)
    elif operator_ == "multiply":
        return int(numOne * numTwo)

print(calculation(operator, firstNum, secondNum))
    
