# basic array operations using lists

salaries = [480000.00, 72500.00, 66400.00, 39000.00, 54800.00]
#print (salaries[0])
#print (salaries[2])

print ('the length of array is', len(salaries))
for i in range (len(salaries)):
    print ('i equals', i, salaries[i])

print (' ') # better for loop

for salary in salaries:
    print (salary)

print ('salaries are', salaries)

salaries[2] = 88000.00
salaries[4] = 59000.00
print ('raised salaries are', salaries)
