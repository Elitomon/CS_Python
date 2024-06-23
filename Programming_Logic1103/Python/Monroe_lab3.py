# Eli Monroe
# Oct 28 2021
# Intro to Programming Lab3
'''
This program will calculate the total and individual
costs for one 3 credit hour class at columbus state
'''

print ('*' * 50)

print ('\tColumbus State Community College')
print ('\t550 East Spring Street')
print ('\tColumbus, OH 43215')

print ('-' * 50)

classAmount = 1
creditHrs = 3
bookPrice = (classAmount * 52.99)
labFees = (classAmount * 25.00)
tuitionCost = (creditHrs * 157.93)
totalFee = str(bookPrice + labFees + tuitionCost)

print ('\tProduct Name:\tProduct Price')
print ('\tBooks\t\t' + '$' + str(bookPrice))
print ('\tLab Fees\t' + '$' + str(labFees))
print ('\tTuition\t\t' + '$' + str(tuitionCost))

print ('-' * 50)

print ('\t' * 3 + 'Total\n' + '\t' * 3 + '$ ' + totalFee)

print ('-' * 50)
print (' ')
print ('   Thank you for being a Columbus State Student')
print ('*' * 50)
