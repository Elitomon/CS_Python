# simulated file read
# indefinite while loop

record = input ('what is the first record')
print (record)

while record != 'eof':
    print ('the record is', record)
    record = input ('please enter next record: ')

print ('file read')
