# questionable for loops
# dont use in this course

for i in range (1, 10, 1):
    if i == 3 or i == 6:
        continue
    print ('i equals', i)

print ('loop complete')

print (' ') # break statement **************************

for i in range (1, 10, 1):
    if i == 3 or i == 6:
        break
    print ('i is now', i)

print ('loop finished')
