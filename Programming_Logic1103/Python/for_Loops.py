# basic for loops

for i in range (10):
    print ('i equals', i)

print ('out of loop')


print (' ') # start and end ******************************

for i in range (4, 10):
    print ('i is now', i)

print ('loop is now over')

print (' ') # start, end, and step ***********************

for i in range (4, 20, 3,):
    print ('i equals', i)

print ('loop done')

print (' ') # negative step ******************************

for i in range (10, 0, -1):
    print (i)

print ('blastoff')

print (' ') # census *************************************

for year in range (1980, 2040, 10):
    print ('census scheduled for', year)

print ('census complete')

print (' ') # modulus census *****************************

for year in range (1974, 2027):
#    print ('year', year)
    if year % 10 == 0:
        print ('year', year, 'is a census year')

print ('loop complete')

print (' ') # nested loops *******************************

cell = 0
rowStart = 2
colStart = 4
rowEnd = 6
colEnd = 9
for i in range (rowStart, rowEnd, 1):
    print ('in outer loop, i equals', i)
    for j in range (colStart, colEnd, 1):
        cell += 1
        print ('reset cell', cell, 'at row', i, \
               'and column', j)

print ('spreadsheet complete')
