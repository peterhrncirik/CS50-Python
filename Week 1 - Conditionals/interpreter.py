userInput = input("Expression: ")

firstNum = int(userInput.strip().split(" ")[0])
secondNum = int(userInput.strip().split(" ")[2])
sign = userInput.strip().split(" ")[1]

# calculate the expression based on sign 
if sign == "+":
    print(f'{float(firstNum + secondNum):.1f}')
elif sign == "-":
    print(f'{float(firstNum - secondNum):.1f}')
elif sign == "*":
    print(f'{float(firstNum * secondNum):.1f}')
elif sign == "/" and secondNum != 0:
    print(f'{float(firstNum / secondNum):.1f}')
