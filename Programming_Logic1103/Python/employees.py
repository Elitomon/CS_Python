# multiple types
# arrays are constrained to the same type values
# lists are not

employee1 = [4402, 'John Doe', 'marketing', 58000.00, '03/27/2013']
print('employee one')
for emp in employee1:
    print (emp)

print ('employee one\'s name is', employee1[1])
employee1[3] += 2500
print('employee one\'s salary is', employee1[3])

print (' ') # two dimensional arrays 

employees = []
employees.append (employee1)
print(employees)

employee2 = [9104, 'Susan Smith', 'IT', 67000.00, '11/19/2005']
employee3 = [4913, 'Carlos Roe', 'sales', 48000.00, '03/03/2009']

employees.append(employee2)
employees.append(employee3)

for emp in employees:
    print(emp)