# test for integer input

testInt = input ('enter your integer: ')
print ('is digit gives',  testInt.isdigit())
while not testInt.isdigit():
    testInt = input('please enter integer ')

myInt = int(testInt)
print ('the integer is ', myInt)