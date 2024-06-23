# string unpack
# nov 9 2021

myStr = input ('please enter your string: ')
print (myStr)

print ('there are', len(myStr), 'characters')

for ichar in range (0, len(myStr), 1):
    print ('Character', ichar, 'is', myStr[ichar])

print ('unpack complete')
