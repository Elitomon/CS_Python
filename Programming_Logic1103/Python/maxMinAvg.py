# creating array
# finding max min & average
# Nov 6 2021

numList = []
num = (float(input('please enter your first number: ')))
numList.append(num)
avgNum = 0

while num != 0:
    avgNum += num
    num = float(input('please enter the next number: '))
    numList.append(num)
    

numList.pop()
print (numList)
print (avgNum / len(numList))

for minNum in numList:
    print ('minNum')
    
# have to relate each num in numlist to eachother in order to determine max or min

# for i in range (0, len(numList), 1):