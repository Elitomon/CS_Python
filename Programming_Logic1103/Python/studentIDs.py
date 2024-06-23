# dynamic array using lists, ordered, and allows duplicates

studentIDs = []
print ('student IDs', studentIDs)

thisID = int(input('what is the first student ID? '))
while thisID != 0:
    studentIDs.append(thisID)
    thisID = int(input('enter the next student ID: '))

print ('student IDs are', studentIDs)

studentIDs.pop()
print ('student IDs are now', studentIDs)