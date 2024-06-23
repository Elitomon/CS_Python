# Meeting Hall
# Eli Monroe
# 2 Nov 2021

people = input('how many people will be attending? ')
days = input('how many days will the meeting last? ')

print (' ')

if int(people) >= 200:
    print ('there is a maximum capacity of 200 people')
    people = 200
if int(people) <= 10:
    print ('there is a minimum capacity of 10 people')
    people = 10

if int(days) >= 30:
    print ('there is a maximum of 30 days')
    days = 30

print (' ')

if int(people) >= 106:
    hall = 'C'
    cost = (int(days) * 275)
elif int(people) >= 31:
    hall = 'B'
    cost = (int(days) * 150)
else:
    hall = 'A'
    cost = (int(days) * 75)

print ('you have been given hall', hall, '\nyour total cost is', '$' + str(cost))
