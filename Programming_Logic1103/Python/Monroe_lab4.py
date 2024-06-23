# Calculator.py
# Eli Monroe
# 4 Nov 2021
# this program will do simple calculations of numbers given by the user

calcType = input('Please select one option: add/subtract/multiply/divide: ')
print ('You chose: ' + calcType + '.')
firstNum = float(input('What is the first number? '))
secondNum = float(input('What is the second number? '))

if calcType == 'add':
    print (firstNum, '+', secondNum, '=', firstNum + secondNum)
elif calcType == 'subtract':
    print (firstNum, '-', secondNum, '=', firstNum - secondNum)
elif calcType == 'multiply':
    print (firstNum, '*', secondNum, '=', firstNum * secondNum)
elif calcType == 'divide':
    print (firstNum, '/', secondNum, '=', firstNum / secondNum)
else:
    print ('The option you chose (' + calcType + ') is not valid\nPlease try this program again.')
    
